import streamlit as st

def aplicar_estilo_pagina():
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
    background-color: #f9f9f9;
    border-radius: 10px;
    padding: 10px;
    box-shadow: 0 0 5px rgba(0,0,0,0.05);
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    color: #111827; /* 🔥 Cor do texto mais escura (preto suave) */
}

/* 🌟 Efeito ao passar o mouse */
.stMetric:hover {
    transform: translateY(-3px);
    box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
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

def mostrar_insight(tipo, emoji, texto_markdown):
    cor = {
        "erro": "#fdecea",     # vermelho claro
        "sucesso": "#e6f4ea",  # verde claro
        "info": "#e8f0fe",     # azul claro
    }.get(tipo, "#f9f9f9")

    st.markdown(
        f"""
        <div style="background-color:{cor}; padding: 16px; border-radius: 8px; border-left: 6px solid #ccc;">
            <span style="font-size: 1.1rem;">{emoji} {texto_markdown}</span>
        </div>
        """,
        unsafe_allow_html=True
    )