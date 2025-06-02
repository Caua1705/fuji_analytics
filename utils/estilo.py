import streamlit as st

def aplicar_estilo_pagina():
    html_css_content = """
<style>
    /* Estilos gerais para o html e body para remover margens padrão */
    html, body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        font-family: Arial, sans-serif;
        background-color: #ffffff; /* Fundo GERAL da página para branco */
    }

    /* Esconde o cabeçalho padrão do Streamlit (Share, Edit, etc.) */
    .stApp > header {
        display: none !important;
    }

    /* Estilo da Logo Fuji no Canto Superior Direito */
    .fuji-logo-top-right {
        position: fixed;
        top: 10px;
        right: 20px;
        height: 40px;
        z-index: 10000; /* Garante que a logo fique acima de tudo */
    }

    /* Estilos para as métricas (st.metric) */
    .stMetric {
        background-color: #f9f9f9; /* Fundo das métricas pode continuar um off-white para destaque */
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

    /* 🚨 MUDANÇA AQUI: Estilo para a barra de "espaço" visual no topo - AGORA FIXA! 🚨 */
    .top-spacer-bar {
        height: 120px; /* <--- Ajuste esta altura para o espaço que você quer */
        background-color: #ffffff; /* Mesma cor de fundo da página */
        width: 100%;
        position: fixed; /* <--- MUDANÇA: AGORA É FIXA! */
        top: 0;          /* <--- MUDANÇA: Começa no topo da tela */
        left: 0;         /* <--- MUDANÇA: Começa na esquerda da tela */
        z-index: 9999;   /* <--- MUDANÇA: Z-index alto para ficar acima do conteúdo, mas abaixo da logo */
        box-shadow: none; /* Sem sombra para ser imperceptível */
    }

    /* Precisamos resetar o padding-top das classes do Streamlit para que o conteúdo
       comece logo abaixo da nossa barra fixa, sem espaço extra. */
    .block-container {
        padding-top: 0 !important;
        padding-bottom: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }
    .st-emotion-cache-1jm6gvw {
        padding-top: 0 !important;
    }
    .main {
        padding-top: 0 !important;
    }
</style>

<img src="https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png" alt="FUJI" class="fuji-logo-top-right">

<div class="top-spacer-bar"></div>
"""

# Injetar o HTML/CSS no Streamlit usando a variável
    st.markdown(html_css_content, unsafe_allow_html=True)

# --- Conteúdo principal do seu Dashboard Streamlit ---
# Precisamos adicionar um "padding" no primeiro elemento do Streamlit para que ele não fique
# embaixo da barra fixa. Vamos usar um st.write com altura ou um st.empty.
# A altura deve ser igual ou maior que a height da .top-spacer-bar
    st.markdown(f"<div style='height: 120px;'></div>", unsafe_allow_html=True)
    
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
