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

    /* 🛑 ESCONDE OS ELEMENTOS PADRÃO DO CABEÇALHO DO STREAMLIT 🛑 */
    /* Esconde o cabeçalho padrão do Streamlit (Share, Edit, etc.) no canto direito */
    .stApp > header {
        display: none !important;
    }

    /* Esconde o ícone de "seta para trás" e o título/nome do arquivo padrão no canto superior esquerdo */
    .stAppHeader > div:first-child {
        display: none !important;
    }


    /* ✨ ESTILO DA LOGO FUJI NO CANTO SUPERIOR ESQUERDO (DENTRO DO HEADER) ✨ */
    /* A logo será injetada e movida para cá via JavaScript */
    .fuji-logo-top-left-in-header {
        height: 40px; /* Altura da logo */
        z-index: 10001; /* Z-index alto para garantir que apareça */
        /* Remova qualquer sombra ou borda da própria imagem se ela tiver */
        box-shadow: none;
        border: none;
        margin-right: 10px; /* Espaço à direita da logo, se houver outros elementos ou texto */
    }

    /* Configuração da barra de cabeçalho padrão do Streamlit (stAppHeader) */
    .stAppHeader {
        background-color: #ffffff; /* Fundo branco para a barra */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05); /* Sombra sutil, se quiser */
        padding: 0 20px; /* Ajusta o padding interno da barra */
        display: flex; /* Transforma em um container flexível */
        justify-content: flex-start; /* Alinha o conteúdo (sua logo) ao início */
        align-items: center; /* Alinha verticalmente */
        height: 60px; /* Altura da barra padrão, ajuste se precisar */
        position: fixed; /* A barra já é fixa por padrão, mas reforçamos */
        width: 100%;
        top: 0;
        left: 0;
        z-index: 1000; /* Garante que ela fique no topo, abaixo da sua logo se precisar de uma no canto direito */
    }

    /* Redefinição de paddings para o conteúdo principal */
    /* O stAppHeader já lida com o padding-top por padrão. */
    .stAppViewContainer, .stMainBlockContainer, .st-emotion-cache-*, .block-container, .main {
        padding-top: 0px !important; /* Mantenha zerado para evitar padding extra */
        padding-bottom: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* 🚨 TRUQUE PARA EMPURRAR O CONTEÚDO PRINCIPAL PARA BAIXO DO CABEÇALHO FIXO 🚨 */
    /* Adiciona uma margem superior ao contêiner principal de conteúdo.
       A altura deve ser igual ou maior que a altura do stAppHeader (60px). */
    .stAppViewContainer { /* Ou .stMainBlockContainer, se for mais eficaz */
        margin-top: 60px !important; /* <--- AJUSTE ESTE VALOR: Altura do stAppHeader para empurrar o conteúdo */
    }
    /* Alternativa caso o stAppViewContainer não funcione bem: */
    /* .stApp > div:first-child > div:nth-child(1) {
        margin-top: 60px !important;
    } */

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

    /* ESTILO PARA O TÍTULO PRINCIPAL DO DASHBOARD (QUE FICARÁ ABAIXO DO HEADER) */
    .dashboard-main-title {
        font-family: 'Arial', sans-serif; /* Fonte similar à padrão do Streamlit */
        font-size: 2.2em; /* Tamanho do título, ajuste conforme necessário */
        font-weight: 700; /* Negrito para destaque */
        color: #333333; /* Cor cinza escuro para profissionalismo */
        text-align: left; /* Alinhamento à esquerda */
        margin-top: 20px; /* Espaço acima do título (ajuste) */
        margin-bottom: 25px; /* Espaço abaixo do título (ajuste) */
        padding-left: 20px; /* Alinha com o conteúdo principal, se block-container tiver padding */
    }
</style>

<img id="custom-fuji-logo-left" src="https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png" alt="FUJI" class="fuji-logo-top-left-in-header"/>

<script>
    const intervalLeft = setInterval(function() {
        const header = document.querySelector('.stAppHeader');
        const logoLeft = document.getElementById('custom-fuji-logo-left');
        if (header && logoLeft && !header.contains(logoLeft)) {
            // Insere a logo como o PRIMEIRO filho do header
            header.insertBefore(logoLeft, header.firstChild);
            // Ajusta o posicionamento da logo dentro do flexbox do header
            logoLeft.style.position = 'relative';
            logoLeft.style.top = 'auto';
            logoLeft.style.left = 'auto';
            logoLeft.style.transform = 'none';
            logoLeft.style.marginRight = '10px'; // Espaçamento entre logo e outros elementos no header
            clearInterval(intervalLeft);
        }
    }, 100); // Tenta a cada 100ms
</script>
"""

# Injetar o HTML/CSS no Streamlit
    st.markdown(html_css_content, unsafe_allow_html=True)

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
