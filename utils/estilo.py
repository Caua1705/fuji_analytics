import streamlit as st

def aplicar_estilo_pagina(titulo, metricas_config):
    # Configuração padrão se não for passada
    if metricas_config is None:
        metricas_config = [
            {"bg_color": "#e8f5e9", "border_color": "#4CAF50"},  # Verde
            {"bg_color": "#ffebee", "border_color": "#F44336"},  # Vermelho
            {"bg_color": "#e3f2fd", "border_color": "#2196F3"},  # Azul
            {"bg_color": "#ede7f6", "border_color": "#9C27B0"},  # Roxo
        ]

    # Gera o CSS específico para as métricas
    metricas_css = ""
    for i, m in enumerate(metricas_config, start=1):
        metricas_css += f"""
        [data-testid="stColumn"]:nth-of-type({i}) .stMetric {{
            background-color: {m['bg_color']};
            border-left: 5px solid {m['border_color']};
        }}
        """

    # CSS geral
    st.markdown(
    f"""
    <style>
        .logo-fixed {{
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 100;
        }}

        .block-container {{
            padding-top: 3rem;
            padding-bottom: 1.5rem;
            padding-left: 2rem;
            padding-right: 2rem;
        }}

        .stMetric {{
            background-color: #f9f9f9;
            border-radius: 10px;
            padding: 10px;
            box-shadow: 0 0 5px rgba(0,0,0,0.05);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            color: #111827;
        }}

        .stMetric:hover {{
            transform: translateY(-3px);
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
        }}

        {metricas_css}

        .dashboard-main-title {{
            font-family: 'Arial', sans-serif;
            font-size: 2.2em;
            font-weight: 700;
            color: #333333;
            text-align: left;
            margin-top: 20px;
            margin-bottom: 25px;
            padding-left: 20px;
        }}
    </style>

    <h1 class='dashboard-main-title'>{titulo}</h1>
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

def criar_bloco_insight(tipo, conteudo_html): 
    bg = ""
    borda = ""
    icone = "" 
    cor_texto = "#333333"

    if tipo == "Info":
        bg = "#e0f2f7"
        borda = "#64b5f6"
        icone = "ℹ️" 
        estilo_borda_extra = "border: 1px solid;"
    elif tipo == "Receitas":
        bg = "#e0ffe6"
        borda = "#66bb6a"
        icone = "📈" 
        estilo_borda_extra = "border: 1px solid;"
    elif tipo == "Despesas":
        bg = "#ffebe6"
        borda = "#ef5350" 
        icone = "⚠️" 
        estilo_borda_extra = "border: 1px solid;"
    elif tipo == "Alerta":
        bg = "#fff8e1"
        borda = "#ffb300"
        icone = "🔍"
        estilo_borda_extra = "border: 1px solid;"

    icone_html = f'<span style="margin-right: 8px; font-size: 1.2em;">{icone}</span>'

    html_msg = f"""
        <div style="
            background-color:{bg};
            padding:12px;
            border-radius:6px;
            font-size: 0.9em;
            color: {cor_texto};
            {estilo_borda_extra} border-color: {borda};
            box-shadow: none;
        ">
            {icone_html} {conteudo_html}
        </div>
    """
    st.markdown(html_msg, unsafe_allow_html=True)