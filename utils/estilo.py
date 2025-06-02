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

    /* 🚨 MUDANÇA PRINCIPAL: Estilizando o stAppHeader (barra padrão do Streamlit) 🚨 */
    .stAppHeader {
        background-color: #ffffff; /* Garante que a barra seja branca */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); /* Opcional: Adiciona uma sombra sutil se quiser */
        padding: 0 20px; /* Ajusta o padding interno da barra */
        display: flex; /* Usa flexbox para alinhamento */
        justify-content: space-between; /* Alinha a seta/título à esquerda e sua logo à direita */
        align-items: center; /* Alinha verticalmente */
        height: 60px; /* Altura padrão da barra, ajuste se precisar */
        position: fixed; /* A barra já é fixa por padrão, mas reforçamos */
        width: 100%;
        top: 0;
        left: 0;
        z-index: 1000; /* Garante que ela fique no topo */
    }

    /* Esconde o ícone de "seta para trás" e outros elementos de navegação iniciais da barra */
    /* Este seletor mira o primeiro div dentro do header que geralmente contém a seta e o título do arquivo */
    .stAppHeader > div:first-child {
        display: none !important; /* Esconde o ícone da seta e o título do app */
    }

    /* Esconde a área de botões "Share", "Edit", "Settings", etc. */
    /* Este seletor mira o div que contém esses botões no lado direito */
    .stAppHeader > div:nth-child(2) {
         display: none !important; /* Esconde todos os botões padrão à direita */
    }

    /* ✨ LOGO FUJI AGORA POSICIONADA DENTRO DO stAppHeader ✨ */
    .fuji-logo-in-header {
        height: 40px; /* Altura da logo */
        margin-left: auto; /* Empurra a logo para a direita se estiver no flexbox */
        /* Opcional: ajuste top/right se não ficar perfeito com margin-left auto */
        /* position: absolute; */
        /* top: 50%; */
        /* right: 20px; */
        /* transform: translateY(-50%); */
    }

    /* Redefinição de paddings para o conteúdo principal */
    /* O Streamlit já adiciona padding-top automaticamente com o header padrão */
    .stAppViewContainer, .stMainBlockContainer, .st-emotion-cache-*, .block-container, .main {
        /* Garante que o padding-top seja suficiente para o conteúdo começar abaixo do header */
        padding-top: 80px !important; /* Ajuste este valor (altura do stAppHeader + um pouco de espaço) */
        padding-bottom: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
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

"""

# Injetar o HTML/CSS no Streamlit
    st.markdown(html_css_content, unsafe_allow_html=True)

# 🚨 TRUQUE PARA INSERIR A LOGO DENTRO DO HEADER DO STREAMLIT 🚨
# Vamos usar JavaScript para mover a sua imagem logo que ela for renderizada.
# Isso é uma forma de "inserir" a logo dentro de um elemento existente do Streamlit.
    st.markdown(
    """
    <script>
        const interval = setInterval(function() {
            const header = document.querySelector('.stAppHeader');
            const logo = document.getElementById('custom-fuji-logo');
            if (header && logo && !header.contains(logo)) {
                header.appendChild(logo);
                logo.style.position = 'relative'; /* Ajusta o posicionamento dentro do flexbox */
                logo.style.top = 'auto';
                logo.style.right = 'auto';
                logo.style.transform = 'none';
                logo.style.marginLeft = 'auto'; /* Empurra para a direita */
                clearInterval(interval);
            }
        }, 100); // Tenta a cada 100ms
    </script>
    <img id="custom-fuji-logo" src="https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png" alt="FUJI" style="height: 40px; z-index: 10000;"/>
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
