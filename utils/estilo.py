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

        /* 🔥 Logo fixa no topo direito (se você a estiver usando) */
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

        /* 🚨 ESTILOS PERSONALIZADOS PARA CADA CAIXA DE MÉTRICA (st.metric) 🚨 */

        /* Estilo base para todas as métricas */
        .stMetric {
            background-color: #f9f9f9; /* Fundo padrão, será sobrescrito por cores específicas */
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0 0 5px rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            color: #111827; /* Cor do texto padrão para todas as métricas */
        }

        /* Efeito ao passar o mouse - aplicado a todas as métricas */
        .stMetric:hover {
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }

        /* Estilo para a 1ª Métrica (Receita Total) - VERDE */
        [data-testid="stColumn"]:nth-of-type(1) .stMetric {
            background-color: #e8f5e9;
            border-left: 5px solid #4CAF50;
        }

        /* Estilo para a 2ª Métrica (Despesa Total) - VERMELHO */
        [data-testid="stColumn"]:nth-of-type(2) .stMetric {
            background-color: #ffebee;
            border-left: 5px solid #F44336;
        }

        /* Estilo para a 3ª Métrica (Resultado Financeiro) - AZUL */
        [data-testid="stColumn"]:nth-of-type(3) .stMetric {
            background-color: #e3f2fd;
            border-left: 5px solid #2196F3;
        }

        /* Estilo para a 4ª Métrica (Margem de Lucro) - ROXO */
        [data-testid="stColumn"]:nth-of-type(4) .stMetric {
            background-color: #ede7f6;
            border-left: 5px solid #9C27B0;
        }

        /* Opcional: Estilizar o label e o valor dentro da métrica (geral para todas) */
        .stMetric > div > div:first-child { /* Label da métrica */
            color: #555;
            font-size: 0.9em;
            margin-bottom: 5px;
        }

        .stMetric > div > div:nth-child(2) { /* Valor da métrica */
            font-size: 1.8em;
            font-weight: bold;
            color: #333;
        }

        /* 🎯 NOVO: ESTILOS PARA AS CAIXAS DE INSIGHTS (st.info / st.warning / st.success) 🎯 */
        /* Estas são as classes que o Streamlit usa para caixas de alerta/informação */
        .stAlert { /* Este é um contêiner genérico para st.info, st.success, st.warning */
            border-radius: 5px; /* Cantos menos arredondados que as métricas */
            padding: 10px 15px; /* Padding interno */
            box-shadow: none; /* Sem sombra para parecer mais plano */
            border: 1px solid rgba(0,0,0,0.1); /* Borda fina e sutil */
            font-size: 0.9em; /* Texto ligeiramente menor */
            line-height: 1.4;
            transition: none; /* Remove efeito de hover se houver algum padrão */
            transform: none; /* Remove transformações padrão */
        }

        /* Estilo específico para st.success (Receita líder) */
        .stAlert.success {
            background-color: #d4edda; /* Verde padrão do Streamlit para sucesso */
            border-color: #28a745; /* Borda mais escura para combinar */
            color: #155724; /* Texto mais escuro */
        }

        /* Estilo específico para st.error (Despesa mais alta - se for st.error ou st.warning) */
        .stAlert.error, .stAlert.warning { /* Se for st.warning ou st.error */
            background-color: #f8d7da; /* Vermelho padrão do Streamlit para erro/aviso */
            border-color: #dc3545;
            color: #721c24;
        }


        /* Linha para remover o botão "Gerenciar aplicativo" (mantida) */
        button[data-testid="manage-app-button"] {
            display: none !important;
        }
        section[data-testid="stStatusWidget"] {
            display: none !important;
        }
        [class^="_terminalButton_"] {
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
