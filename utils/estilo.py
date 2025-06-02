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

            .stMetric {
                background-color: #f9f9f9;
                border-radius: 10px;
                padding: 10px;
                box-shadow: 0 0 5px rgba(0,0,0,0.05);
                transition: transform 0.2s ease, box-shadow 0.2s ease;
                color: #111827;
            }

            /* 🌟 Efeito ao passar o mouse */
            .stMetric:hover {
                transform: translateY(-3px);
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
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

def criar_bloco_insight(tipo, conteudo_html, icone=None): # Adicionado parâmetro 'icone'
    bg = ""
    borda = ""
    cor_texto = "#333333" # Cor de texto padrão para insights

    if tipo == "Info":
        bg = "#f0f8ff"  # Tom de azul muito mais claro
        borda = "#a9d9f5" # Borda mais clara
        estilo_borda_extra = "border: 1px solid;" # Borda mais fina e visível em vez de border-left grossa
    elif tipo == "Receitas":
        bg = "#f0fff4"  # Verde muito mais claro/pastel
        borda = "#a7e9b4" # Borda mais clara
        estilo_borda_extra = "border: 1px solid;"
    elif tipo == "Despesas":
        bg = "#fff0f0"  # Vermelho muito mais claro/pastel
        borda = "#f5c6cb" # Borda mais clara
        estilo_borda_extra = "border: 1px solid;"
        
    # Ícone, se fornecido
    icone_html = f'<span style="margin-right: 8px; font-size: 1.2em;">{icone}</span>' if icone else ''

    html_msg = f"""
        <div style="
            background-color:{bg};
            padding:12px; /* Padding um pouco menor */
            border-radius:6px; /* Cantos menos arredondados */
            font-size: 0.9em; /* Fonte ligeiramente menor */
            color: {cor_texto};
            {estilo_borda_extra} border-color: {borda}; /* Aplica a borda fina com a cor */
            box-shadow: none; /* Remove qualquer sombra para um visual mais plano */
        ">
            {icone_html} {conteudo_html}
        </div>
    """
    st.markdown(html_msg, unsafe_allow_html=True)
