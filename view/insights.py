import pandas as pd
from utils.estilo import criar_bloco_insight
from utils.formatadores import formatar_moeda,formatar_porcentagem

def insight_receitas(df_receitas_por_categoria,data_inicio,data_fim):

    if data_inicio.month != data_fim.month or data_inicio.year != data_fim.year:
        conteudo_html = "📘 <strong>Selecione datas dentro do mesmo mês</strong> para exibir os insights"
        criar_bloco_insight("Info",conteudo_html)
        return
    
    df_insight_receitas=df_receitas_por_categoria.copy()

    data_inicio_formatada = data_inicio.strftime("%d-%m")
    data_fim_formatada = data_fim.strftime("%d-%m")

    diferenca_dias=(data_fim-data_inicio).days+1

    top_categorias=df_insight_receitas["Grupo"].head(3).tolist()

    if diferenca_dias==1:

        conteudo_html = f'''<strong>Receita líder</strong> do dia {data_inicio_formatada}: 
                🥇 <strong>{top_categorias[0]}</strong>'''
        
        criar_bloco_insight("Receitas",conteudo_html)

    elif 1 < diferenca_dias < 28:

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

        conteudo_html = f'''A categoria <strong>{categoria_selecionada["Grupo"]}</strong> vendeu apenas 
{categoria_selecionada["Quantidade"]} unidades, mas com ticket médio alto de 
{formatar_moeda(categoria_selecionada["Valor por Item"])} — bom potencial.'''
        
        criar_bloco_insight("Receitas",conteudo_html)

def insight_despesas(df_despesas_por_categoria,df_despesas_anterior_por_categoria,data_inicio,data_fim):

    if data_inicio.month != data_fim.month or data_inicio.year != data_fim.year:
        conteudo_html = "📘 <strong>Selecione datas dentro do mesmo mês</strong> para exibir os insights"
        criar_bloco_insight("Info",conteudo_html)
        return
    
    data_inicio_formatada = data_inicio.strftime("%d-%m")
    data_fim_formatada = data_fim.strftime("%d-%m")

    diferenca_dias=(data_fim-data_inicio).days+1

    top_centro_de_custo=df_despesas_por_categoria["Centro_Custo"].head(3).tolist()


    if diferenca_dias==1:

        conteudo_html = f'''<strong>Despesa mais alta</strong> do dia {data_inicio_formatada}: 🧾 <strong>{top_centro_de_custo[0]}</strong>'''

        criar_bloco_insight("Despesas",conteudo_html)

    elif 1 < diferenca_dias < 28:

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
        df_comparacao["Diferença"]=df_comparacao["Valor Pago_atual"] - df_comparacao["Valor Pago_anterior"]

        df_comparacao=df_comparacao.sort_values(by="Diferença",ascending=False)

        maior_aumento=df_comparacao.iloc[0]

        percentual_aumento=(maior_aumento["Diferença"] / maior_aumento["Valor Pago_anterior"]) * 100

        conteudo_html = f'''O centro <strong>{maior_aumento["Centro_Custo"]}</strong> registrou aumento de 
<strong>{formatar_porcentagem(percentual_aumento)}</strong> 
({formatar_moeda(maior_aumento["Diferença"])}), passando de 
{formatar_moeda(maior_aumento["Valor Pago_anterior"])} para 
{formatar_moeda(maior_aumento["Valor Pago_atual"])}.'''
        
        criar_bloco_insight("Despesas",conteudo_html)