import streamlit as st

def exibir_abas(filial):
    col1, col2, col3 = st.columns([1, 6, 1])

    with col2:
        st.subheader(f"Distribuição de Receita e Despesas | {filial}")

    col_esquerda, col_toggle, col_direita = st.columns([10, 1, 1])
    with col_toggle:
        modo_percentual = st.toggle("📊 %", help="Mostrar proporção percentual")

    if modo_percentual:
        tipo_visualizacao = "Proporção percentual"
        agrupar_outros = True
    else:
        tipo_visualizacao = "Valores absolutos"
        agrupar_outros = False

    return tipo_visualizacao, agrupar_outros
