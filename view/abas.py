import streamlit as st

def exibir_abas(filial):
    col_esquerda, col_titulo, col_botao = st.columns([1, 6, 1])

    with col_titulo:
        st.subheader(f"Distribuição de Receita e Despesas | {filial}")

    with col_botao:
        modo_percentual = st.toggle("📊 %", help="Mostrar proporção percentual")

    if modo_percentual:
        tipo_visualizacao = "Proporção percentual"
        agrupar_outros = True
    else:
        tipo_visualizacao = "Valores absolutos"
        agrupar_outros = False

    return tipo_visualizacao, agrupar_outros