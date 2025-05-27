import streamlit as st

def exibir_abas():
    col1, col2 = st.columns([3, 2])  # Ajusta a proporção de espaço

    with col1:
        st.markdown("### 🔍 Distribuição de Receita e Despesas")

    with col2:
        tipo_visualizacao = st.radio(
            "", 
            ["Valores absolutos", "Proporção percentual"], 
            horizontal=True
        )