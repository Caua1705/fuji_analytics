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

            /* 🚨 NOVO: ESTILOS PERSONALIZADOS PARA CADA CAIXA DE MÉTRICA 🚨 */

            /* Estilo base para todas as métricas */
            .stMetric {
                background-color: #f9f9f9; /* Fundo padrão, será sobrescrito por cores específicas */
                border-radius: 10px;
                padding: 15px; /* Aumentado o padding para mais "ar" */
                box-shadow: 0 1px 3px rgba(0,0,0,0.12), 0 1px 2px rgba(0,0,0,0.24); /* Sombra mais sutil */
                transition: all 0.3s cubic-bezier(.25,.8,.25,1); /* Transição para o hover */
                color: #111827; /* Cor do texto padrão para todas as métricas */
            }

            /* 🌟 Efeito ao passar o mouse - aplicado a todas as métricas */
            .stMetric:hover {
                transform: translateY(-2px); /* Levanta um pouco menos */
                box-shadow: 0 14px 28px rgba(0,0,0,0.25), 0 10px 10px rgba(0,0,0,0.22); /* Sombra mais pronunciada ao hover */
            }

            /* Estilo para a 1ª Métrica (Receita Total) - VERDE */
            /* Isso mira a 1ª coluna e, dentro dela, o contêiner .stMetric */
            [data-testid="stColumn"]:nth-of-type(1) .stMetric {
                background-color: #e8f5e9; /* Verde muito claro */
                border-left: 5px solid #4CAF50; /* Barra lateral verde mais forte */
            }

            /* Estilo para a 2ª Métrica (Despesa Total) - VERMELHO */
            /* Isso mira a 2ª coluna e, dentro dela, o contêiner .stMetric */
            [data-testid="stColumn"]:nth-of-type(2) .stMetric {
                background-color: #ffebee; /* Vermelho muito claro */
                border-left: 5px solid #F44336; /* Barra lateral vermelha mais forte */
            }

            /* Estilo para a 3ª Métrica (Resultado Financeiro) - AZUL (neutro/informativo) */
            /* Isso mira a 3ª coluna e, dentro dela, o contêiner .stMetric */
            [data-testid="stColumn"]:nth-of-type(3) .stMetric {
                background-color: #e3f2fd; /* Azul muito claro */
                border-left: 5px solid #2196F3; /* Barra lateral azul mais forte */
            }

            /* Estilo para a 4ª Métrica (Margem de Lucro) - ROXO (para diferenciar e indicar insights) */
            /* Isso mira a 4ª coluna e, dentro dela, o contêiner .stMetric */
            [data-testid="stColumn"]:nth-of-type(4) .stMetric {
                background-color: #ede7f6; /* Roxo muito claro */
                border-left: 5px solid #9C27B0; /* Barra lateral roxa mais forte */
            }

            /* Opcional: Estilizar o label e o valor dentro da métrica (geral para todas) */
            /* Esses seletores são mais genéricos e devem funcionar */
            .stMetric > div > div:first-child { /* Label da métrica */
                color: #555; /* Cor um pouco mais escura para o label */
                font-size: 0.9em;
                margin-bottom: 5px;
            }

            .stMetric > div > div:nth-child(2) { /* Valor da métrica */
                font-size: 1.8em; /* Aumentar o tamanho do valor */
                font-weight: bold;
                color: #333; /* Cor mais escura para o valor */
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
