import streamlit as st

def aplicar_estilo():
    """Aplica CSS global para o app."""
    st.markdown(
        """
        <style>
            /* 🔥 Logo fixa no topo direito */
            .logo-fixed {
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 100;
            }

            /* 💠 Caixa das métricas */
            .stMetric {
                background-color: #f9f9f9;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0 0 5px rgba(0,0,0,0.05);
            }
        </style>
        """,
        unsafe_allow_html=True
    )

def inserir_logo(url_logo: str, tamanho: int = 100):
    """Insere logo fixa no topo direito."""
    st.markdown(
        f"""
        <div class="logo-fixed">
            <img src="{url_logo}" width="{tamanho}">
        </div>
        """,
        unsafe_allow_html=True
    )

def linha_divisoria():
    st.markdown(
        """
        <hr style="
            margin-top: 0.5rem;
            margin-bottom: 1rem;
            border: none;
            border-top: 1px solid rgba(0,0,0,0.15);
        ">
        """,
        unsafe_allow_html=True
    )