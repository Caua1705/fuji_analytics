import streamlit as st

def aplicar_estilo_pagina():
    st.markdown(
    """
    <style>
        /* Resetar margens e paddings padrão */
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        /* Estilos gerais para o html e body */
        html, body {
            width: 100%;
            height: 100%;
            font-family: Arial, sans-serif;
            background-color: #ffffff;
        }

        /* 🔥 Logo fixa no topo direito */
        .logo-fixed {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 100;
        }

        /* 🔹 Reduzir espaço interno da página */
        .block-container {
            padding-top: 3rem;
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

        /* 🚨 SOLUÇÃO MAIS AGRESSIVA E ABRANGENTE PARA REMOVER O BOTÃO "GERENCIAR APLICATIVO" 🚨 */
        /* Tenta esconder o widget de status onde o botão pode estar */
        section[data-testid="stStatusWidget"] {
            display: none !important;
        }
        /* Tenta esconder o botão pelo data-testid mais comum */
        button[data-testid="manage-app-button"] {
            display: none !important;
        }
        /* Tenta esconder qualquer elemento button ou div cuja classe comece com '_terminalButton_' */
        [class^="_terminalButton_"] { /* Mira em qualquer elemento que comece com essa classe */
            display: none !important;
        }
        /* Mira o contêiner inferior do Streamlit onde esse botão costuma aparecer */
        .st-emotion-cache-1jc7l8v { /* Classe que geralmente contém o botão flutuante */
            display: none !important;
        }
        .st-emotion-cache-v065m3 { /* Outra variação de classe comum para o botão flutuante */
            display: none !important;
        }
        .st-emotion-cache-15r3q2k { /* Mais uma variação de classe comum */
            display: none !important;
        }
        .st-emotion-cache-r423a2 { /* Mais uma variação de classe comum */
            display: none !important;
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

def criar_bloco_insight(tipo,conteudo_html):
    if tipo == "Info":
        bg = "#e8f0fe"
        borda = "#4285f4"
    elif tipo == "Receitas":
        bg = "#e6f4ea"
        borda = "#34a853"
    elif tipo == "Despesas":
        bg = "#fdecea"
        borda = "#f44336"

    html_msg = f"""
        <div style="background-color:{bg}; padding:16px; border-left:6px solid {borda}; border-radius:8px;">
            {conteudo_html}
        </div>
    """
    st.markdown(html_msg, unsafe_allow_html=True)
