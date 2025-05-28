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

            /* 🎯 Estilo das Métricas */
            .stMetric {
                background-color: #fdfdfd;
                border-radius: 12px;
                padding: 16px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.05);
                border: 1px solid #f0f0f0;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            /* 🌟 Hover Suave */
            .stMetric:hover {
                transform: translateY(-3px);
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
            }

            /* 🏷️ Label da métrica */
            .stMetric > label {
                color: #8B5E3C; /* Marrom Fuji */
                font-size: 0.85rem;
                font-weight: 500;
            }

            /* 💰 Valor da métrica */
            .stMetric > div {
                color: #D66BA0; /* Rosa Fuji */
                font-size: 1.8rem;
                font-weight: 700;
            }

            /* 🔸 Subtexto da métrica */
            .stMetric small {
                color: #999999;
                font-size: 0.75rem;
            }
        </style>
        """,
        unsafe_allow_html=True
    )


def inserir_logo(url_logo,tamanho):
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