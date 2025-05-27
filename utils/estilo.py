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

            /* 🔸 Divisor fino, discreto e elegante */
            hr {
                margin-top: 5px;
                margin-bottom: 5px;
                border: none;
                border-top: 1px solid #DADADA;
            }

            /* 🔹 Reduzir espaço interno da página */
            .block-container {
                padding-top: 1.5rem;
                padding-bottom: 1.5rem;
                padding-left: 2rem;
                padding-right: 2rem;
            }

            /* 🎯 Reduz espaço da sidebar */
            [data-testid="stSidebar"] > div:first-child {
                padding-top: 1rem;
                padding-bottom: 1rem;
            }

            /* 🧽 Remove espaçamentos desnecessários */
            .stMarkdown {
                margin-bottom: 0.5rem;
            }

            /* 🎨 Ajusta títulos */
            h1 {
                font-size: 2.2rem;
                margin-bottom: 0.2rem;
            }
            h2 {
                font-size: 1.8rem;
                margin-bottom: 0.2rem;
            }
            h3 {
                font-size: 1.4rem;
                margin-bottom: 0.2rem;
            }
            h4, h5, h6 {
                margin-bottom: 0.1rem;
            }

            /* 🌈 Fonte geral mais clean */
            html, body, [class*="css"] {
                font-family: 'Inter', sans-serif;
                font-size: 0.95rem;
            }

            /* 🔳 Bordas dos containers */
            .stContainer {
                border-radius: 8px;
            }

            /* 🔗 Remove underline dos links */
            a {
                text-decoration: none;
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
    """Adiciona uma linha divisória discreta."""
    st.markdown(
        """
        <hr style="
            margin-top: 5px;
            margin-bottom: 5px;
            border: none;
            border-top: 1px solid rgba(0,0,0,0.15);
        ">
        """,
        unsafe_allow_html=True
    )