import streamlit as st

def aplicar_estilo_pagina():
    html_css_content = """
<style>
    /* Resetar todas as margens e paddings padrão no início para evitar conflitos */
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
    /* Usamos a classe exata identificada na inspeção: stAppHeader */
    .stAppHeader { /* */
        display: none !important;
    }

    /* Estilo da Logo Fuji no Canto Superior Direito */
    .fuji-logo-top-right {
        position: fixed;
        top: 10px;
        right: 20px;
        height: 40px; /* Altura da logo */
        z-index: 10000;
        box-shadow: none;
        border: none;
    }

    /* BARRA FIXA SUPERIOR INVISÍVEL (que empurra o conteúdo) */
    .top-spacer-bar {
        /* ESTE É O VALOR QUE DEFINE O TAMANHO TOTAL DA BARRA FIXA NO TOPO */
        height: 120px; /* <--- AJUSTE ESTE VALOR PARA O ESPAÇO DESEJADO (ex: 80px, 100px, 150px) */
        background-color: #ffffff; /* Mesma cor de fundo da página */
        width: 100%;
        position: fixed;
        top: 0;
        left: 0;
        z-index: 9999; /* Alto, mas menor que a logo */
        box-shadow: none; /* Sem sombra */
    }

    /* Redefinição agressiva de padding-top para os principais contêineres do Streamlit */
    /* Isso garante que o conteúdo não tenha padding-top extra do Streamlit */
    /* ZERA PADDING-TOP EM QUASE TUDO NO TOPO para evitar conflitos */
    .stAppViewContainer, .stMainBlockContainer, .st-emotion-cache-*, .block-container, .main { /* */
        padding-top: 0px !important;
    }

    /* 🚨 🚨 🚨 NOVO: MARGIN-TOP FORÇADO NO CONTÊINER PRINCIPAL DO APP 🚨 🚨 🚨 */
    /* Usamos a classe exata do stAppViewContainer ou stMainBlockContainer */
    /* Este é o método mais robusto para empurrar o conteúdo para baixo. */
    /* A altura deve ser igual à altura da .top-spacer-bar para um alinhamento perfeito. */
    .stAppViewContainer { /* */
        margin-top: 120px !important; /* <--- AJUSTE ESTE VALOR PARA DESCER O CONTEÚDO */
    }
    /* Alternativa, se a anterior não funcionar tão bem, use esta em vez de stAppViewContainer */
    .stMainBlockContainer { /* */
        /* margin-top: 120px !important; */
    }


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

<img src="https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png" alt="FUJI" class="fuji-logo-top-right">

<div class="top-spacer-bar"></div>
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
