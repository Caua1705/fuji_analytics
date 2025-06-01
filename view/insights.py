import streamlit as st
import pandas as pd

def insight_receitas(df_receitas_por_categoria,data_inicio,data_fim):
    df_insight_receitas=df_receitas_por_categoria.copy()

    data_inicio_formatada = data_inicio.strftime("%d-%m")
    data_fim_formatada = data_fim.strftime("%d-%m")

    diferenca_dias=(data_fim-data_inicio).days+1

    top_categorias=df_insight_receitas["Grupo"].head(3).tolist()

    if diferenca_dias==0:

        html_msg = f"""
            <div style="background-color:#e6f4ea; padding:16px; border-left:6px solid #34a853; border-radius:8px;">
                🍽️ <strong>Top 1 Receita</strong> do dia <strong>{data_inicio_formatada}</strong>: 
                🥇 <strong>{top_categorias[0]}</strong>
            </div>
        """
        st.markdown(html_msg, unsafe_allow_html=True)

    elif diferenca_dias<7:

        html_msg = f"""
            <div style="background-color:#e6f4ea; padding:16px; border-left:6px solid #34a853; border-radius:8px;">
                🍽️ <strong>Top 3 Receitas</strong> (de <strong>{data_inicio_formatada}</strong> a <strong>{data_fim_formatada}</strong>): 
                🥇 <strong>{top_categorias[0]}</strong>, 🥈 <strong>{top_categorias[1]}</strong> e 🥉 <strong>{top_categorias[2]}</strong>
            </div>
        """
        st.markdown(html_msg, unsafe_allow_html=True)
        
    else:
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

        html_msg = f"""
    <div style="background-color:#e6f4ea; padding:16px; border-left:6px solid #34a853; border-radius:8px;">
        🟢 <strong>{categoria_selecionada["Grupo"]}</strong> vende pouco (<strong>{categoria_selecionada["Quantidade"]:.0f} itens</strong>), 
        mas com ticket médio de <strong>R${categoria_selecionada["Valor por Item"]:.2f}</strong>.<br>
        🚀 É um segmento estratégico de <strong>alto valor</strong>!
    </div>
"""
        st.markdown(html_msg, unsafe_allow_html=True)

def insight_despesas(df_despesas_por_categoria,df_despesas_anterior_por_categoria,data_inicio,data_fim):

    diferenca_dias=(data_fim-data_inicio).days+1

    if diferenca_dias==30:
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

        html_msg = f"""
            <div style="background-color:#fdecea; padding:16px; border-left:6px solid #f44336; border-radius:8px;">
                🔺 O centro <strong>{maior_aumento["Centro_Custo"]}</strong> registrou aumento de <strong>{maior_aumento["Diferença"]}</strong>,
                passando de <strong>{maior_aumento["Valor_Pago/Recebido_anterior"]}</strong> para <strong>{maior_aumento["Valor_Pago/Recebido_atual"]}</strong>.
            </div>
            """
        st.markdown(html_msg, unsafe_allow_html=True)