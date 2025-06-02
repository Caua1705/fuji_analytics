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

        /* 🚨 SOLUÇÃO ROBUSTA PARA REMOVER O BOTÃO "GERENCIAR APLICATIVO" 🚨 */
        /* Tenta esconder o botão pelo data-testid */
        button[data-testid="manage-app-button"] {
            display: none !important;
        }
        /* Tenta esconder o contêiner pai do botão, que muitas vezes tem esta classe */
        .stActionButton { /* Esta classe é comum para botões de ação do Streamlit */
            display: none !important;
        }
        /* Tenta esconder o contêiner geral onde o botão pode estar */
        .stBottom { /* Esta classe pode ser para a barra inferior */
            display: none !important;
        }
        /* Seletor mais genérico para evitar que o botão apareça */
        div[data-testid="stToolbar"] { /* Às vezes o botão está numa toolbar escondida */
            display: none !important;
        }
        /* Oculta qualquer elemento com a classe relacionada ao botão flutuante */
        .css-1jc7l8v { /* Exemplo de uma classe gerada para o contêiner do botão flutuante */
             display: none !important;
        }
        .st-emotion-cache-1jc7l8v { /* Outro exemplo de classe gerada */
            display: none !important;
        }


    </style>
    """,
    unsafe_allow_html=True)

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
