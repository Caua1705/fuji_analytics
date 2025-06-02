import streamlit as st

def aplicar_estilo_pagina():
    st.markdown(
    """
    <style>
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

            /* Estilo base para todas as métricas */
            .stMetric {
                /* APENAS COR DE FUNDO PADRÃO AQUI, SEM SOMBRA, BORDA OU TRANSITION */
                background-color: #f9f9f9; /* Fundo padrão, será sobrescrito por cores específicas */
                border-radius: 10px;
                padding: 10px;
                color: #111827; /* Cor do texto padrão */
                /* Removidos: box-shadow, transition, e estilos de hover */
            }

            /* Removendo completamente o efeito ao passar o mouse */
            .stMetric:hover {
                transform: none; /* Garante que não haja levantamento */
                box-shadow: none; /* Remove a sombra ao passar o mouse */
            }

            /* Estilo para a 1ª Métrica (Receita Total) - APENAS VERDE */
            [data-testid="stColumn"]:nth-of-type(1) .stMetric {
                background-color: #e8f5e9; /* Verde muito claro */
                border-left: none; /* Removida a barra lateral */
            }

            /* Estilo para a 2ª Métrica (Despesa Total) - APENAS VERMELHO */
            [data-testid="stColumn"]:nth-of-type(2) .stMetric {
                background-color: #ffebee; /* Vermelho muito claro */
                border-left: none; /* Removida a barra lateral */
            }

            /* Estilo para a 3ª Métrica (Resultado Financeiro) - APENAS AZUL */
            [data-testid="stColumn"]:nth-of-type(3) .stMetric {
                background-color: #e3f2fd; /* Azul muito claro */
                border-left: none; /* Removida a barra lateral */
            }

            /* Estilo para a 4ª Métrica (Margem de Lucro) - APENAS ROXO */
            [data-testid="stColumn"]:nth-of-type(4) .stMetric {
                background-color: #ede7f6; /* Roxo muito claro */
                border-left: none; /* Removida a barra lateral */
            }

            /* Removendo qualquer sombra ou transição dos valores internos das métricas também */
            .stMetric > div > div:first-child, /* Label da métrica */
            .stMetric > div > div:nth-child(2) { /* Valor da métrica */
                transition: none;
                box-shadow: none;
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
