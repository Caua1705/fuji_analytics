import streamlit as st

def exibir_abas(filial):
    # Título centralizado
    st.markdown(
        f"<h3 style='text-align: center;'>Distribuição de Receita e Despesas | {filial}</h3>",
        unsafe_allow_html=True
    )

    # Toggle alinhado à direita
    col_esquerda, col_toggle = st.columns([10, 1])
    with col_toggle:
        modo_percentual = st.toggle("📊 %", help="Mostrar proporção percentual")

    # Definindo tipo de visualização
    if modo_percentual:
        tipo_visualizacao = "Proporção percentual"
        agrupar_outros = True
    else:
        tipo_visualizacao = "Valores absolutos"
        agrupar_outros = False

    return tipo_visualizacao, agrupar_outros
