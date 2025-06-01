import streamlit as st
import pandas as pd
from utils.estilo import criar_bloco_insight

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

        conteudo_html=f'''📈 <strong>Receita líder</strong> do dia <strong>{data_inicio_formatada}</strong>: 
                🥇 <strong>{top_categorias[0]}</strong>'''
        
        criar_bloco_insight("Receitas",conteudo_html)

    elif 1 < diferenca_dias < 28:

        conteudo_html=f'''🍽️ <strong>Top 3 Receitas</strong> (de <strong>{data_inicio_formatada}</strong> a <strong>{data_fim_formatada}</strong>): 
                    🥇 <strong>{top_categorias[0]}</strong>, 🥈 <strong>{top_categorias[1]}</strong> e 🥉 <strong>{top_categorias[2]}</strong>'''
        
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

        conteudo_html = f'''✅ A categoria <strong>{categoria_selecionada["Grupo"]}</strong> teve poucas vendas (<strong>{categoria_selecionada["Quantidade"]:.0f}</strong>),
                         mas com ticket médio alto (<strong>R${categoria_selecionada["Valor por Item"]:.2f}</strong>), indicando bom potencial.'''
        
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

        conteudo_html = f'''📉 <strong>Despesa mais alta</strong> do dia <strong>{data_inicio_formatada}</strong>: 
                        <strong>🧾 {top_centro_de_custo[0]}</strong>'''

        criar_bloco_insight("Despesas",conteudo_html)

    elif 1 < diferenca_dias < 28:

        conteudo_html = f'''💸 <strong>Top 3 Despesas</strong> (de <strong>{data_inicio_formatada}</strong> a <strong>{data_fim_formatada}</strong>):
                        🥇 <strong>{top_centro_de_custo[0]}</strong>, 🥈 <strong>{top_centro_de_custo[1]}</strong> e 🥉 <strong>{top_centro_de_custo[2]}</strong>'''
        
        criar_bloco_insight("Despesas",conteudo_html)


    elif diferenca_dias in (28, 29, 30, 31):
        
        df_comparacao = pd.merge(
            df_despesas_por_categoria,
            df_despesas_anterior_por_categoria,
            on='Centro_Custo',
            suffixes=('_atual', '_anterior'),
            how='inner'  # Apenas centros presentes nos dois períodos
    )
        df_comparacao["Diferença"]=df_comparacao["Valor_Pago/Recebido_atual"] - df_comparacao["Valor_Pago/Recebido_anterior"]

        df_comparacao=df_comparacao.sort_values(by="Diferença",ascending=False)

        maior_aumento=df_comparacao.iloc[0]

        conteudo_html = f'''🔺 O centro <strong>{maior_aumento["Centro_Custo"]}</strong> registrou aumento de <strong>{maior_aumento["Diferença"]}</strong>,
                passando de <strong>{maior_aumento["Valor_Pago/Recebido_anterior"]}</strong> para <strong>{maior_aumento["Valor_Pago/Recebido_atual"]}</strong>.'''
        
        criar_bloco_insight("Despesas",conteudo_html)