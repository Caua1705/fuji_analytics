import streamlit as st

def exibir_abas():
    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Análise de Receitas")
    with col2:
        st.subheader("Análise de Despesas")
        modo_percentual = st.toggle("Mostrar proporção (%)", value=False)
    if modo_percentual:
        tipo_visualizacao = "Proporção percentual"
        agrupar_outros = True
    else:
        tipo_visualizacao = "Valores absolutos"
        agrupar_outros = False
    return tipo_visualizacao,agrupar_outros

