import pandas as pd
from utils.estilo import criar_bloco_insight
from utils.formatadores import formatar_moeda,formatar_porcentagem
import streamlit as st

def insight_receitas(df_receitas_por_categoria,data_inicio,data_fim):

    if data_inicio.month != data_fim.month or data_inicio.year != data_fim.year:
        conteudo_html = "📘 <strong>Selecione datas dentro do mesmo mês</strong> para exibir os insights"
        criar_bloco_insight("Info",conteudo_html)
        return
    
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

    elif 1 < diferenca_dias < 28:

        top_categorias=df_insight_receitas["Grupo"].head(3).tolist()

        conteudo_html = f'''<strong>Top 3 Receitas</strong> (de {data_inicio_formatada} a {data_fim_formatada}):  
                🥇 <strong>{top_categorias[0]}</strong>, 🥈 {top_categorias[1]} e 🥉 {top_categorias[2]}'''
        
        criar_bloco_insight("Receitas",conteudo_html)

    elif diferenca_dias in (28, 29, 30, 31):
    
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
<strong>{categoria_selecionada["Quantidade"]}</strong> unidades, mas teve ticket médio alto de 
<strong>{formatar_moeda(categoria_selecionada["Valor por Item"])}</strong> — indica boa margem.'''
        
        criar_bloco_insight("Receitas",conteudo_html)

def insight_despesas(df_despesas_por_categoria,df_despesas_anterior_por_categoria,data_inicio,data_fim):

    if data_inicio.month != data_fim.month or data_inicio.year != data_fim.year:
        conteudo_html = "📘 <strong>Selecione datas dentro do mesmo mês</strong> para exibir os insights"
        criar_bloco_insight("Info",conteudo_html)
        return
    
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


    elif diferenca_dias in (28, 29, 30, 31):
        
        df_comparacao = pd.merge(
            df_despesas_por_categoria,
            df_despesas_anterior_por_categoria,
            on='Centro_Custo',
            suffixes=('_atual', '_anterior'),
            how='inner'  # Apenas centros presentes nos dois períodos
    )
        if df_comparacao.empty:
            criar_bloco_insight(
                "Despesas", 
                "Não foi possível gerar comparação de despesas, pois não há dados suficientes do mês anterior."
            )
            return
    
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

    data_inicio_formatada = data_inicio.strftime("%d-%m")
    data_fim_formatada = data_fim.strftime("%d-%m")
    df_receitas_filtrado=df_receitas_filtrado.sort_values(by="Produto")
    df_catalogo_produtos=df_catalogo_produtos.sort_values(by="Produto")
    st.write(df_receitas_filtrado)
    st.write(df_catalogo_produtos)
    df_concatenado=df_catalogo_produtos.merge(
        df_receitas_filtrado,
        on="Produto",
        how="left",
        indicator=True
    )

    produtos_sem_venda=df_concatenado.loc[df_concatenado["_merge"]=="left_only","Produto"]
    st.write(df_receitas_filtrado)
    st.write(produtos_sem_venda)
    
    conteudo_html = (f'''
        Entre <strong>{data_inicio_formatada}</strong> e <strong>{data_fim_formatada}</strong>, 
        <strong>{len(produtos_sem_venda)} produtos</strong> do catálogo não registraram nenhuma venda.'''
    )
        
    criar_bloco_insight("Despesas",conteudo_html)
    with st.expander("🔍 Ver produtos sem vendas"):
        for produto in produtos_sem_venda:
            st.markdown(f"- {produto}")

def produtos_em_decadencia(df_receitas_por_produto,df_30_dias_por_produto):

    if df_30_dias_por_produto.empty:
        st.write("Sem dados")
    else:
        df_concatenado = df_receitas_por_produto[["Produto","Valor"]].merge(
        df_30_dias_por_produto[["Produto","Valor"]],
        on="Produto",
        how="inner", 
        suffixes=("_atual", "_anterior")  
    )
    df_concatenado["Diferença"]=df_concatenado["Valor_atual"] - df_concatenado["Valor_anterior"]
    df_concatenado["Percentual_Diferença"]=df_concatenado["Diferença"] / df_concatenado["Valor_anterior"] * 100
    df_decadentes = df_concatenado[df_concatenado["Diferença"] < 0]

    df_decadentes["Diferença"] = df_decadentes["Diferença"].abs()
    df_decadentes["Percentual_Diferença"] = df_decadentes["Percentual_Diferença"].abs()

    df_decadentes=df_decadentes.sort_values(by="Diferença",ascending=False)

    top1 = df_decadentes.iloc[0]
    diferenca=top1["Diferença"]
    percentual_diferenca=top1["Percentual_Diferença"]

    conteudo_html = (
    f'<strong>{top1["Produto"]}</strong> caiu {formatar_porcentagem(percentual_diferenca)} '
    f'({formatar_moeda(diferenca)}) nas últimas 4 semanas.'
)
    criar_bloco_insight("Despesas", conteudo_html)

    with st.expander("🔍 Ver mais produtos em decadência"):
        produtos_decadencia = df_decadentes.iloc[1:11][["Produto", "Diferença", "Percentual_Diferença"]]

        for _, linha in produtos_decadencia.iterrows():
            produto = linha["Produto"]
            valor = formatar_moeda(linha["Diferença"])
            perc = formatar_porcentagem(linha["Percentual_Diferença"])

            st.markdown(f"- <strong>{produto}</strong>: queda de {perc} ({valor})", unsafe_allow_html=True)