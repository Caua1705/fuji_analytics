import pandas as pd
from utils.estilo import criar_bloco_insight
from utils.formatadores import formatar_moeda,formatar_porcentagem,formatar_unidade,formatar_datas_sidebar
from processamento.agrupar import agrupar_por_produto,produtos_sem_vendas,produto_com_maior_variacao
import streamlit as st

def insight_receitas(df_receitas_por_categoria,data_inicio,data_fim):

    df_insight_receitas=df_receitas_por_categoria.copy()
    
    if df_insight_receitas.empty:
        criar_bloco_insight("Receitas", "⚠️ Nenhuma receita encontrada no período.")
        return

    data_inicio_formatada = data_inicio.strftime("%d-%m")
    data_fim_formatada = data_fim.strftime("%d-%m")

    diferenca_dias=(data_fim-data_inicio).days+1

    top_categorias=df_insight_receitas["Grupo"].head(3).tolist()

    if diferenca_dias==1:
        categoria_dia = df_insight_receitas["Grupo"].iloc[0]
        conteudo_html = f'''<strong>Receita líder</strong> do dia {data_inicio_formatada}: 
                🥇 <strong>{categoria_dia}</strong>'''
        criar_bloco_insight("Receitas",conteudo_html)
        return 
    elif 1 < diferenca_dias < 28:
        top_categorias=df_insight_receitas["Grupo"].head(3).tolist()
        conteudo_html = f'''<strong>Top 3 Receitas</strong> (de {data_inicio_formatada} a {data_fim_formatada}):  
                🥇 <strong>{top_categorias[0]}</strong>, 🥈 {top_categorias[1]} e 🥉 {top_categorias[2]}'''
        criar_bloco_insight("Receitas",conteudo_html)
        return

    elif diferenca_dias >=28:
    
        df_insight_receitas["Valor por Item"]=df_insight_receitas["Valor"] / df_insight_receitas["Quantidade"]
        media_valor_por_item=df_insight_receitas["Valor por Item"].mean()
        media_quantidade=df_insight_receitas["Quantidade"].mean()
        categoria_selecionada = (
            df_insight_receitas
            .loc[
                (df_insight_receitas["Quantidade"] < media_quantidade) &
                (df_insight_receitas["Valor por Item"] > media_valor_por_item)
            ]
            .sort_values(by="Valor por Item", ascending=False)
            .iloc[0]
        )

        conteudo_html = f'''A categoria <strong>{categoria_selecionada["Grupo"]}</strong> vendeu só 
<strong>{formatar_unidade(categoria_selecionada["Quantidade"])}</strong> unidades, mas teve ticket médio alto de 
<strong>{formatar_moeda(categoria_selecionada["Valor por Item"])}</strong> — indica boa margem.'''
        
        criar_bloco_insight("Receitas",conteudo_html)

def insight_despesas(df_despesas_por_categoria,df_despesas_anterior_por_categoria,data_inicio,data_fim):

    if df_despesas_por_categoria.empty:
        criar_bloco_insight("Despesas", "Nenhuma despesa encontrada no período.")
        return
    
    data_inicio_formatada = data_inicio.strftime("%d-%m")
    data_fim_formatada = data_fim.strftime("%d-%m")

    diferenca_dias=(data_fim-data_inicio).days+1

    if diferenca_dias==1:
        
        centro_custo_dia = df_despesas_por_categoria["Centro_Custo"].iloc[0]

        conteudo_html = f'''<strong>Despesa mais alta</strong> do dia {data_inicio_formatada}: 🧾 <strong>{centro_custo_dia}</strong>'''

        criar_bloco_insight("Despesas",conteudo_html)

    elif 1 < diferenca_dias < 28:
        top_centro_de_custo=df_despesas_por_categoria["Centro_Custo"].head(3).tolist()

        conteudo_html = f'''<strong>Top 3 Despesas</strong> (de {data_inicio_formatada} a {data_fim_formatada}):  
                🥇 <strong>{top_centro_de_custo[0]}</strong>, 🥈 {top_centro_de_custo[1]} e 🥉 {top_centro_de_custo[2]}'''
        
        criar_bloco_insight("Despesas",conteudo_html)


    elif diferenca_dias >=28:
        
        df_comparacao = pd.merge(
            df_despesas_por_categoria,
            df_despesas_anterior_por_categoria,
            on='Centro_Custo',
            suffixes=('_atual', '_anterior'),
            how='inner'  # Apenas centros presentes nos dois períodos
    )
    
        df_comparacao["Diferença"]=df_comparacao["Valor Pago_atual"] - df_comparacao["Valor Pago_anterior"]

        df_comparacao=df_comparacao.sort_values(by="Diferença",ascending=False)

        maior_aumento=df_comparacao.iloc[0]

        percentual_aumento=(maior_aumento["Diferença"] / maior_aumento["Valor Pago_anterior"]) * 100

        conteudo_html = f'''O centro <strong>{maior_aumento["Centro_Custo"]}</strong> registrou aumento de 
<strong>{formatar_porcentagem(percentual_aumento)}</strong> 
({formatar_moeda(maior_aumento["Diferença"])}), <strong>nos últimos {diferenca_dias} dias</strong>, 
passando de {formatar_moeda(maior_aumento["Valor Pago_anterior"])} para 
{formatar_moeda(maior_aumento["Valor Pago_atual"])}.'''
        
        criar_bloco_insight("Despesas",conteudo_html)

def insight_produtos_sem_vendas(df_receitas_filtrado,df_catalogo_produtos,data_inicio,data_fim):

    data_inicio_formatada,data_fim_formatada=formatar_datas_sidebar(data_inicio,data_fim)
    produtos_sem_venda=produtos_sem_vendas(df_receitas_filtrado,df_catalogo_produtos)

    conteudo_html = (f'''
        Entre <strong>{data_inicio_formatada}</strong> e <strong>{data_fim_formatada}</strong>, 
        <strong>{len(produtos_sem_venda)} produtos</strong> do catálogo não registraram nenhuma venda.'''
    )
        
    criar_bloco_insight("Alerta",conteudo_html)
    with st.expander("🔍 Ver produtos sem vendas"):
        for produto in produtos_sem_venda:
            st.markdown(f"- {produto}")

def produtos_em_ascensao(df_receitas, df_receitas_anterior, data_inicio, data_fim):

    data_inicio_formatada, data_fim_formatada = formatar_datas_sidebar(data_inicio, data_fim)
    diferenca_dias = (data_fim - data_inicio).days + 1

    if df_receitas_anterior.empty:
        conteudo_html = '''<strong>Sem dados disponíveis</strong> — não há registros suficientes para realizar a análise.'''
        criar_bloco_insight("Info", conteudo_html)
        return
    
    df_receitas_agrupado,top1,top3 = agrupar_por_produto(df_receitas, "Produto", "Quantidade", "Valor", "Ascendência")

    if diferenca_dias == 1:
        conteudo_html = f'''<strong>Produto mais vendido</strong> do dia {data_inicio_formatada}: 
                <strong>{top1}</strong>'''
        criar_bloco_insight("Receitas", conteudo_html)
        return

    elif 1 < diferenca_dias < 7:
        conteudo_html = f'''<strong>Top 3 Produtos mais vendidos</strong> (de {data_inicio_formatada} a {data_fim_formatada}):  
                🥇 <strong>{top3[0]}</strong>, 🥈 {top3[1]} e 🥉 {top3[2]}'''
        criar_bloco_insight("Receitas", conteudo_html)
        return

    elif diferenca_dias >= 7:
        df_anterior_agrupado, _, _= agrupar_por_produto(df_receitas_anterior, "Produto", "Quantidade", "Valor", "Ascendência")
        top1_variacao, diferenca, percentual_diferenca, demais_produtos = produto_com_maior_variacao(
            df_receitas_agrupado, df_anterior_agrupado, "Ascendência"
        )
        conteudo_html = f'''
        <strong>{top1_variacao["Produto"]}</strong> subiu {formatar_porcentagem(percentual_diferenca)} 
        ({formatar_moeda(diferenca)}) nos últimos {diferenca_dias} dias.'''
        criar_bloco_insight("Receitas", conteudo_html)

        with st.expander("🔍 Ver mais produtos em ascensão"):
            for _, linha in demais_produtos.iterrows():
                produto = linha["Produto"]
                valor = formatar_moeda(linha["Diferença"])
                perc = formatar_porcentagem(linha["Percentual_Diferença"])
                st.markdown(f"- <strong>{produto}</strong>: aumento de {perc} ({valor})", unsafe_allow_html=True)

def produtos_em_decadencia(df_receitas, df_receitas_anterior, data_inicio, data_fim):

    data_inicio_formatada, data_fim_formatada = formatar_datas_sidebar(data_inicio, data_fim)
    diferenca_dias = (data_fim - data_inicio).days + 1

    if df_receitas_anterior.empty:
        conteudo_html = '''<strong>Sem dados disponíveis</strong> — não há registros suficientes para realizar a análise.'''
        criar_bloco_insight("Info", conteudo_html)
        return
    
    df_receitas_agrupado,top1,top3 = agrupar_por_produto(df_receitas, "Produto", "Quantidade", "Valor", "Decadência")

    if diferenca_dias == 1:
        conteudo_html = f'''<strong>Produto menos vendido</strong> do dia {data_inicio_formatada}: 
                 <strong>{top1}</strong>'''
        criar_bloco_insight("Despesas", conteudo_html)
        return

    elif 1 < diferenca_dias < 7:
        conteudo_html = f'''<strong>Top 3 Produtos menos vendidos</strong> (de {data_inicio_formatada} a {data_fim_formatada}):  
                🥇 <strong>{top3[0]}</strong>, 🥈 {top3[1]} e 🥉 {top3[2]}'''
        criar_bloco_insight("Despesas", conteudo_html)
        return

    elif diferenca_dias >= 7:
        df_anterior_agrupado, _, _= agrupar_por_produto(df_receitas_anterior, "Produto", "Quantidade", "Valor", "Decadência")
        top1_variacao, diferenca, percentual_diferenca, demais_produtos = produto_com_maior_variacao(
            df_receitas_agrupado, df_anterior_agrupado, "Decadência"
        )
        conteudo_html = f'''
        <strong>{top1_variacao["Produto"]}</strong> caiu {formatar_porcentagem(percentual_diferenca)} 
        ({formatar_moeda(diferenca)}) nos últimos {diferenca_dias} dias.'''
        criar_bloco_insight("Despesas", conteudo_html)

        with st.expander("🔍 Ver mais produtos em decadência"):
            for _, linha in demais_produtos.iterrows():
                produto = linha["Produto"]
                valor = formatar_moeda(linha["Diferença"])
                perc = formatar_porcentagem(linha["Percentual_Diferença"])
                st.markdown(f"- <strong>{produto}</strong>: diminuição de {perc} ({valor})", unsafe_allow_html=True)

