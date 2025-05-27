import streamlit as st

def exibir_abas():
    col1, col2 = st.columns([4, 1.8])

    with col1:
        st.markdown("### 🔍 Distribuição de Receita e Despesas")

    with col2:
        tipo_visualizacao = st.radio(
            label="",
            options=["Valores absolutos", "Proporção percentual"],
            horizontal=True
        )

    if tipo_visualizacao == "Proporção percentual":
        agrupar_outros = True
    else:
        agrupar_outros = False
    return tipo_visualizacao,agrupar_outros

