import streamlit as st

def exibir_abas(filial):
    # Título centralizado, sem espaço extra
    st.markdown(
        f"""
        <h3 style='text-align: center; margin-bottom: 0; margin-top: 0;'>
            Distribuição de Receita e Despesas | {filial}
        </h3>
        """,
        unsafe_allow_html=True
    )
    st.markdown("""
    <style>
    h3 {
        margin-top: -50px;
        margin-bottom: 0px;
    }
    </style>
""", unsafe_allow_html=True)

    # Toggle alinhado à direita
    col1, col2, col3 = st.columns([8, 1, 1])
    with col3:
        modo_percentual = st.toggle("📊 %", help="Mostrar proporção percentual")

    if modo_percentual:
        tipo_visualizacao = "Proporção percentual"
        agrupar_outros = True
    else:
        tipo_visualizacao = "Valores absolutos"
        agrupar_outros = False

    return tipo_visualizacao, agrupar_outros