import streamlit as st

def exibir_abas():
    col1, col2 = st.columns([6, 1.5])

    with col1:
        st.subheader("🔍 Distribuição de Receita e Despesas")

    with col2:
        modo_percentual = st.toggle("📊 Proporção", value=False)
    if modo_percentual:
        tipo_visualizacao = "Proporção percentual"
    else:
        tipo_visualizacao = "Valores absolutos"

    if tipo_visualizacao == "Proporção percentual":
        agrupar_outros = True
    else:
        agrupar_outros = False
    return tipo_visualizacao,agrupar_outros

