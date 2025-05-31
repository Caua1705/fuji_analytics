import streamlit as st

def insight_receitas(df_receitas_por_categoria):
    df_insight_receitas=df_receitas_por_categoria.copy()
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
    st.subheader(" 📊 Principais Descobertas")
    st.markdown(f'''🟢 Categoria **{categoria_selecionada["Grupo"]}**:
        menor volume ({categoria_selecionada["Quantidade"]:.0f} itens),
        mas alta receita média por item (R${categoria_selecionada["Valor por Item"]:.2f}).
        Um segmento estratégico de *alto valor*!''')

def insight_despesas(df_despesas_por_categoria):
    st.write(df_despesas_por_categoria)