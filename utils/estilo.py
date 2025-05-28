import streamlit as st

def aplicar_estilo():
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

            /* 🔹 Reduzir espaço interno da página */
            .block-container {
                padding-top: 1.5rem;
                padding-bottom: 1.5rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }

            .stMetric {
            background-color: #ffffff;
            border-radius: 16px;
            padding: 20px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            border: 1px solid #e6e6e6;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

            .stMetric:hover {
                transform: translateY(-4px);
                box-shadow: 0 8px 24px rgba(0, 0, 0, 0.12);
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