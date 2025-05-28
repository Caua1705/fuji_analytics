import streamlit as st

def exibir_abas(filial):
    col1, col2 = st.columns([5, 1])
    with col1:
        st.subheader(f"Distribuição de Receita e Despesas | {filial}")
    with col2:
        proporcao = st.toggle("📊 %", help="Mostrar proporção percentual")
    if modo_percentual:
        tipo_visualizacao = "Proporção percentual"
        agrupar_outros = True
    else:
        tipo_visualizacao = "Valores absolutos"
        agrupar_outros = False
    return tipo_visualizacao,agrupar_outros

