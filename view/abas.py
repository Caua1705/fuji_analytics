import streamlit as st

def exibir_abas(filial):
    st.markdown(
        f"<h3 style='text-align: center;'>Distribuição de Receita e Despesas | {filial}</h3>",
        unsafe_allow_html=True
    )
    _, col_toggle, _ = st.columns([5, 1, 5])
    with col_toggle:
        modo_percentual = st.toggle("📊 %", help="Mostrar proporção percentual")

    if modo_percentual:
        tipo_visualizacao = "Proporção percentual"
        agrupar_outros = True
    else:
        tipo_visualizacao = "Valores absolutos"
        agrupar_outros = False

    return tipo_visualizacao, agrupar_outros

