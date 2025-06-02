import streamlit as st

def aplicar_estilo_pagina():
    html_css_content = """
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
        background-color: #ffffff; /* Fundo GERAL da página para branco */
    }

    /* 🚨 MUDANÇA PRINCIPAL: NÃO ESCONDEMOS O stAppHeader INTEIRO! 🚨 */
    /* Apenas removemos seus elementos internos */

    /* Esconde o ícone de "seta para trás" (se presente) e outros elementos de navegação iniciais */
    .stAppHeader > div:first-child {
        display: none !important;
    }

    /* Esconde a área de botões "Share", "Edit", "Settings", etc. */
    /* O seletor pode variar ligeiramente, mas este tenta cobrir a maioria */
    .stAppHeader > div:nth-child(2) > div:nth-child(1) { /* A área com os botões */
         display: none !important;
    }
    /* Específico para o botão "Manage app" que pode ser externo a essa div */
    button[data-testid="manage-app-button"] {
        display: none !important;
    }


    /* ✨ ESTILO DA LOGO FUJI AGORA DENTRO DA BARRA PADRÃO ✨ */
    .fuji-logo-top-right-in-header {
        position: absolute; /* Posição absoluta DENTRO do header fixo */
        top: 50%; /* Alinha verticalmente no centro */
        right: 20px; /* Distância da direita */
        transform: translateY(-50%); /* Ajuste fino para centralizar verticalmente */
        height: 40px; /* Altura da logo */
        z-index: 10000; /* Garante que a logo fique acima de tudo */
        box-shadow: none;
        border: none;
    }

    /* Redefinição de paddings para o conteúdo principal - deve ser menos agressivo agora */
    /* A barra Streamlit já fornece padding no topo */
    .stAppViewContainer, .stMainBlockContainer, .st-emotion-cache-*, .block-container, .main {
        padding-top: 0px !important; /* Mantenha zerado para evitar padding extra */
        padding-bottom: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* O stAppHeader já é fixo por padrão, então não precisamos de .top-spacer-bar ou margin-top */
    /* Removemos o .top-spacer-bar e o margin-top agressivo */


    /* Estilos para as métricas (st.metric) */
    .stMetric {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 0 5px rgba(0,0,0,0.05);
        transition: transform 0.2s ease, box-shadow 0.2s ease;
        color: #111827;
    }
    .stMetric:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }
</style>

<img src="https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png" alt="FUJI" class="fuji-logo-top-right-in-header">
"""

# Injetar o HTML/CSS no Streamlit
    st.markdown(html_css_content, unsafe_allow_html=True)

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
