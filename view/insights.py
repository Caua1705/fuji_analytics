import streamlit as st
import pandas as pd

def insight_receitas(df_receitas_por_categoria,data_inicio,data_fim):
    df_insight_receitas=df_receitas_por_categoria.copy()

    data_inicio_formatada = data_inicio.strftime("%d-%m")
    data_fim_formatada = data_fim.strftime("%d-%m")

    diferenca_dias=(data_fim-data_inicio).days+1

    top_categorias=df_insight_receitas["Grupo"].head(3).tolist()

    if diferenca_dias==0:
        st.success(
        f"🍽️ **Top 1 Receita** do dia **{data_inicio_formatada}**: "
        f"🥇 **{top_categorias[0]}**")

    elif diferenca_dias<7:
        st.success(
    f"🍽️ **Top 3 Receitas** (de **{data_inicio_formatada}** a **{data_fim_formatada}**): "
    f"🥇 **{top_categorias[0]}**, 🥈 **{top_categorias[1]}** e 🥉 **{top_categorias[2]}**")
        
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
        st.success(f'''🟢 **{categoria_selecionada["Grupo"]}**:
📦 Vende apenas **{categoria_selecionada["Quantidade"]:.0f} itens**, 
💰 mas com ticket médio de **R${categoria_selecionada["Valor por Item"]:.2f}**.
🚀 É segmento estratégico de **alto valor**!''')

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
    st.error(
        f"🔺 O centro de custo **{maior_aumento['Centro_Custo']}** teve o **maior aumento nas despesas**, "
        f"com acréscimo de **R${maior_aumento['Diferença']:,.2f}**, "
        f"subindo de **R${maior_aumento['Valor_Pago/Recebido_anterior']:,.2f}** para **R${maior_aumento['Valor_Pago/Recebido_atual']:,.2f}**."
    )