import streamlit as st

def aplicar_estilo_pagina():
    custom_css = """
<style>
    /* Estilos gerais para o html e body para remover margens padrão */
    html, body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        font-family: Arial, sans-serif;
        background-color: #f4f7fa; /* Cor de fundo geral da página */
    }

    /* Esconde o cabeçalho padrão do Streamlit (Share, Edit, etc.) */
    .stApp > header {
        display: none !important;
    }

    /* Estilo da Logo Fuji no Canto Superior Direito */
    .fuji-logo-top-right {
        position: fixed;
        top: 10px;       /* Distância do topo */
        right: 20px;     /* Distância da direita */
        height: 40px;    /* Altura da logo (ajuste conforme necessário) */
        z-index: 10000;  /* Garante que a logo fique acima de tudo */
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

    /* Efeito ao passar o mouse nas métricas */
    .stMetric:hover {
        transform: translateY(-3px);
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
    }

    /* 🚨 NOVO: Estilo para a barra de "padding" visível no topo 🚨 */
    /* Este div será inserido no Streamlit para criar o espaço com fundo */
    .top-spacer-bar {
        height: 80px; /* <--- AJUSTE ESTE VALOR para a altura da barra de "espaço" */
        background-color: #ffffff; /* <--- Cor de fundo para a barra de espaço. Use a cor que desejar. */
        width: 100%;
        position: relative; /* Importante para que o conteúdo abaixo seja empurrado */
        z-index: 999; /* Um z-index alto, mas menor que a logo */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); /* Opcional: sombra sutil */
    }

    /* Resetar paddings padrão que podem estar causando espaço extra */
    .block-container {
        padding-top: 0 !important; /* Remove o padding-top padrão do block-container */
        padding-bottom: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .st-emotion-cache-1jm6gvw { /* Ou .main */
        padding-top: 0 !important; /* Remove o padding-top dessas classes também */
    }
</style>
"""

# Injetar o CSS
    st.markdown(custom_css, unsafe_allow_html=True)

# Injetar a logo no canto superior direito
    st.markdown(
    f'<img src="https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png" alt="FUJI" class="fuji-logo-top-right">',
    unsafe_allow_html=True
    )

# 🚨 NOVO: Insere a barra de espaço visual no topo 🚨
# Este div é o que cria a "área preenchida" que empurra o conteúdo para baixo.
    st.markdown('<div class="top-spacer-bar"></div>', unsafe_allow_html=True)
    
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
