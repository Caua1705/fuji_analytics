import streamlit as st

def aplicar_estilo_pagina():
    # Oculta os warnings de "Streamlit is in development mode"
    st.set_option('deprecation.showPyplotGlobalUse', False)

    html_css_content = """
<style>
    /* 1. Esconde o cabeçalho padrão do Streamlit (com os ícones de Share, Edit, etc.) */
    .stApp > header {
        display: none !important;
    }

    /* 2. Estilos gerais para o html e body: fundo branco, sem margens padrão */
    html, body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        font-family: Arial, sans-serif;
        background-color: #ffffff; /* Fundo GERAL da página para BRANCO */
    }

    /* 3. Estilo da Logo FUJI no Canto Superior Direito (posição fixa) */
    .fuji-logo-top-right {
        position: fixed;
        top: 10px;       /* Distância do topo da tela */
        right: 20px;     /* Distância da direita da tela */
        height: 40px;    /* Altura da logo - ajuste conforme necessário */
        z-index: 10000;  /* Garante que a logo fique acima de tudo */
        /* Opcional: Remova qualquer sombra ou borda da própria imagem se ela tiver */
        box-shadow: none;
        border: none;
    }

    /* 4. Ajusta o espaçamento do conteúdo principal do Streamlit.
       Este é o espaço que vai empurrar o conteúdo para baixo da logo.
       Ele parecerá "branco" porque o fundo do body é branco. */
    .st-emotion-cache-1jm6gvw { /* Classe comum para o contêiner principal em versões recentes */
        padding-top: 80px !important; /* <--- AJUSTE ESTE VALOR para descer mais o conteúdo */
    }
    .main { /* Classe alternativa para o contêiner principal */
        padding-top: 80px !important; /* <--- AJUSTE ESTE VALOR TAMBÉM */
    }
    /* O .block-container é mais para margens laterais e inferiores,
       e seu padding-top pode ser sobrescrito pelos de cima se forem mais específicos. */
    .block-container {
        /* padding-top: 1.5rem; <--- Este pode ser removido ou zerado se os de cima funcionarem */
        padding-bottom: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* Estilos para as métricas (st.metric) - mantidos como estão */
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
