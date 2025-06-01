import streamlit as st

def insight_receitas(df_receitas_por_categoria,data_inicio,data_fim):
    if (data_fim-data_inicio).days>7:
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
        st.success(f'''🟢 **{categoria_selecionada["Grupo"]}**:
            Vende apenas **{categoria_selecionada["Quantidade"]:.0f} itens**,
            mas com ticket médio de **R${categoria_selecionada["Valor por Item"]:.2f}**.
            É Segmento estratégico de **alto valor**!''')
    else:
        st.info("Para insights estratégicos, selecione um período de pelo menos 7 dias.")
def insight_despesas(df_despesas_por_categoria):
    st.write(df_despesas_por_categoria)