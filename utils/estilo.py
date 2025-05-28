import streamlit as st

def aplicar_estilo():
    st.markdown(
        """
        <style>
            /* 🔥 Logo fixa */
            .logo-fixed {
                position: fixed;
                top: 20px;
                right: 20px;
                z-index: 100;
            }

            /* 🔹 Espaçamento interno */
            .block-container {
                padding-top: 1.5rem;
                padding-bottom: 1.5rem;
                padding-left: 2rem;
                padding-right: 2rem;
                background-color: #FDF9F7; /* Fundo leve */
            }

            /* 🎯 Sidebar */
            [data-testid="stSidebar"] {
                background-color: #F9F6F3;
                border-right: 1px solid #ECECEC;
            }

            /* 🚀 Títulos */
            h1, h2, h3, h4 {
                color: #8B5E3C;
                font-family: 'Segoe UI', sans-serif;
            }

            /* 🔸 Texto padrão */
            p, label, span {
                color: #4A4A4A;
                font-family: 'Segoe UI', sans-serif;
            }

            /* 🎯 Métricas */
            .stMetric {
                background-color: #fdfdfd;
                border-radius: 12px;
                padding: 16px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.05);
                border: 1px solid #f0f0f0;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            .stMetric:hover {
                transform: translateY(-3px);
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.1);
            }

            .stMetric > label {
                color: #8B5E3C;
                font-size: 0.85rem;
                font-weight: 500;
            }

            .stMetric > div {
                color: #D66BA0;
                font-size: 1.8rem;
                font-weight: 700;
            }

            /* 🔘 Botões */
            button {
                background-color: #D66BA0;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                transition: background-color 0.2s ease;
            }

            button:hover {
                background-color: #8B5E3C;
                color: white;
            }

            /* 🔘 Checkboxes e selects */
            .stSelectbox, .stDateInput, .stRadio, .stCheckbox {
                background-color: #FFFFFF;
                border-radius: 8px;
                padding: 8px;
                border: 1px solid #E0E0E0;
            }

            /* 🔥 Remover linhas extras */
            hr {
                border: none;
                border-top: 1px solid #EAEAEA;
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