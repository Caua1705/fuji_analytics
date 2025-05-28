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

            /* 🔹 Página */
            .block-container {
                padding: 1.5rem 2rem;
                background-color: #F3F4F6;
            }

            /* 🎯 Sidebar */
            [data-testid="stSidebar"] {
                background-color: #FFFFFF;
                border-right: 1px solid #E0E0E0;
            }

            /* 🚀 Títulos */
            h1, h2, h3, h4 {
                color: #164863;
                font-family: 'Segoe UI', sans-serif;
                font-weight: 600;
            }

            /* 🔸 Texto padrão */
            p, label, span, div {
                color: #1B1B1B;
                font-family: 'Segoe UI', sans-serif;
            }

            /* 🎯 Métricas */
            .stMetric {
                background-color: #FFFFFF;
                border-radius: 12px;
                padding: 16px;
                box-shadow: 0 2px 6px rgba(0,0,0,0.05);
                border: 1px solid #E0E0E0;
                transition: transform 0.2s ease, box-shadow 0.2s ease;
            }

            .stMetric:hover {
                transform: translateY(-3px);
                box-shadow: 0 6px 16px rgba(0, 0, 0, 0.08);
            }

            .stMetric > label {
                color: #6B7280;
                font-size: 0.85rem;
                font-weight: 500;
            }

            .stMetric > div {
                color: #164863;
                font-size: 1.9rem;
                font-weight: 700;
            }

            /* 🔘 Botões */
            button {
                background-color: #164863;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 8px 16px;
                transition: background-color 0.2s ease;
            }

            button:hover {
                background-color: #113549;
                color: white;
            }

            /* 🔘 Inputs */
            .stSelectbox, .stDateInput, .stRadio, .stCheckbox {
                background-color: #FFFFFF;
                border-radius: 8px;
                padding: 8px;
                border: 1px solid #D1D5DB;
            }

            /* 🔥 Linhas */
            hr {
                border: none;
                border-top: 1px solid #E5E7EB;
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