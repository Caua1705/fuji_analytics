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
            background-color: #ffffff; /* Fundo GERAL da página para branco */
        }

        /* 🛑 ESCONDE O CABEÇALHO PADRÃO DO STREAMLIT (Share, Edit, etc.) 🛑 */
        /* Isso vai limpar o canto superior direito */
        .stApp > header {
            display: none !important;
        }

        /* ✨ ESTILO DA LOGO FUJI NO CANTO SUPERIOR DIREITO ✨ */
        /* Esta classe posicionará sua logo lá */
        .fuji-logo-top-right {
            position: fixed; /* Fixa a logo na tela */
            top: 10px;       /* Distância do topo - ajuste se precisar */
            right: 20px;     /* Distância da direita - ajuste se precisar */
            height: 40px;    /* Altura da logo (ajuste conforme necessário) */
            z-index: 10000;  /* Garante que a logo fique acima de tudo */
            box-shadow: none; /* Remove qualquer sombra */
            border: none;    /* Remove qualquer borda */
        }

        /* 🔥 Logo fixa no topo direito (do seu código original) - COMENTADO, POIS AGORA USAMOS .fuji-logo-top-right */
        /*
        .logo-fixed {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 100;
        }
        */

        /* 🔹 Reduzir espaço interno da página */
        .block-container {
            /* Mantenha seu padding-top original aqui.
               A logo fixa vai flutuar sobre ele, então o conteúdo não será empurrado mais para baixo por ela.
               Ajuste o valor '3rem' se quiser mais espaço entre o topo e o início do seu conteúdo. */
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

        /* IMPORTANTE: Redefinir padding-top em outras classes do Streamlit que podem interferir */
        .stAppViewContainer, .stMainBlockContainer, .st-emotion-cache-*, .main {
            padding-top: 0 !important; /* Zera qualquer padding-top nessas classes */
        }

    </style>

    <img src="https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png" alt="FUJI" class="fuji-logo-top-right">
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
