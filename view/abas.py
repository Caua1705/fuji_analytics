import streamlit as st

def exibir_abas(filial):
    col1, col2, col3 = st.columns([5, 2, 1])

    with col1:
        st.markdown(f"<h3 style='text-align: center;'>Distribuição de Receita e Despesas | {filial}</h3>", unsafe_allow_html=True)

    with col3:
        modo_percentual = st.toggle("📊 %", help="Mostrar proporção percentual")

    if modo_percentual:
        tipo_visualizacao = "Proporção percentual"
        agrupar_outros = True
    else:
        tipo_visualizacao = "Valores absolutos"
        agrupar_outros = False

    return tipo_visualizacao, agrupar_outros