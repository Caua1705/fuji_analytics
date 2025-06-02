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

        /* 🚨 NOVO: ESTILOS PERSONALIZADOS PARA CADA CAIXA DE MÉTRICA 🚨 */

        /* Estilo base para todas as métricas para as propriedades compartilhadas */
        .stMetric {
            background-color: #f9f9f9; /* Fundo padrão, será sobrescrito por cores específicas */
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0 0 5px rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            color: #111827; /* Cor do texto mais escura (preto suave) */
        }

        /* Efeito ao passar o mouse - aplicado a todas as métricas */
        .stMetric:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }

        /* Estilo para a 1ª Métrica (Receita Total) - VERDE */
        div.stMetric:nth-child(1) { /* Seleciona a primeira métrica dentro de suas colunas */
            background-color: #e8f5e9; /* Verde muito claro */
            border-left: 5px solid #4CAF50; /* Uma barra lateral verde mais forte */
        }

        /* Estilo para a 2ª Métrica (Despesa Total) - VERMELHO */
        div.stMetric:nth-child(2) { /* Seleciona a segunda métrica */
            background-color: #ffebee; /* Vermelho muito claro */
            border-left: 5px solid #F44336; /* Uma barra lateral vermelha mais forte */
        }

        /* Estilo para a 3ª Métrica (Resultado Financeiro) - AZUL (neutro/informativo) */
        div.stMetric:nth-child(3) { /* Seleciona a terceira métrica */
            background-color: #e3f2fd; /* Azul muito claro */
            border-left: 5px solid #2196F3; /* Uma barra lateral azul mais forte */
        }

        /* Estilo para a 4ª Métrica (Margem de Lucro) - ROXO (para diferenciar e indicar insights) */
        div.stMetric:nth-child(4) { /* Seleciona a quarta métrica */
            background-color: #ede7f6; /* Roxo muito claro */
            border-left: 5px solid #9C27B0; /* Uma barra lateral roxa mais forte */
        }

        /* Opcional: Estilizar o label e o valor dentro da métrica */
        .stMetric > div:nth-child(1) > div:first-child { /* Label da métrica */
            color: #555; /* Cor um pouco mais escura para o label */
            font-size: 0.9em;
        }

        .stMetric > div:nth-child(1) > div:nth-child(2) { /* Valor da métrica */
            font-size: 1.8em; /* Aumentar o tamanho do valor */
            font-weight: bold;
            color: #333; /* Cor mais escura para o valor */
        }

        /* Isso é para ocultar o botão "Gerenciar Aplicativo" (tentativa final) */
        /* Mantendo os seletores mais agressivos que geralmente funcionam */
        section[data-testid="stStatusWidget"] {
            display: none !important;
        }
        button[data-testid="manage-app-button"] {
            display: none !important;
        }
        [class^="_terminalButton_"] {
            display: none !important;
        }
        .st-emotion-cache-1jc7l8v, .st-emotion-cache-v065m3, .st-emotion-cache-15r3q2k, .st-emotion-cache-r423a2 {
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
