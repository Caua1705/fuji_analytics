import streamlit as st
# Carregar Dados
from carregamento.carregar_dados import carregar_dataframes
# Formatar Dados
from utils.formatar import formatar_dataframe
from utils.config_formatacao import config_receitas, config_despesas
# Filtrar Dados
from processamento.filtrar import filtrar_por_filial, processar_filial
# Exibir Métricas
from view.metricas import exibir_metricas_financeiras
# Agrupar Dados
from processamento.agrupar import agrupar_por_categoria
# Exibir Abas
from view.abas import exibir_abas
# Exibir Gráficos
from view.graficos import exibir_graficos

# Configuração da Página

# Logo Fixa
st.markdown(
    """
    <style>
        .logo-fixed {
            position: fixed;
            top: 20px;
            right: 20px;
            z-index: 100;
        }
    </style>

    <div class="logo-fixed">
        <img 
            src="https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png" 
            width="110">
    </div>
    """,
    unsafe_allow_html=True
)
st.set_page_config(
    page_title="Fuji Analytics",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>

    /* 🌑 Background geral (Dark elegante) */
    .stApp {
        background-color: #0f1117;
        color: #f5f5f5;
    }

    /* 🎨 Sidebar */
    [data-testid="stSidebar"] {
        background-color: #1a1d23;
    }
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    /* 🎯 Títulos */
    h1, h2, h3, h4, h5, h6 {
        color: #f5f5f5;
        margin-bottom: 0.3rem;
    }

    /* 🔗 Links */
    a {
        color: #6ab7ff;
        text-decoration: none;
    }

    /* ✨ Texto */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        color: #f5f5f5;
        font-size: 0.95rem;
    }

    /* 🔳 Caixa dos componentes (como metrics) */
    .stMetric {
        background-color: #161921;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 0 6px rgba(0,0,0,0.6);
    }

    /* 📊 Dataframes */
    .stDataFrame {
        background-color: #161921;
        border-radius: 10px;
    }

    /* 🔥 Divisor */
    hr {
        border: none;
        border-top: 1px solid rgba(255, 255, 255, 0.2);
        margin-top: 6px;
        margin-bottom: 6px;
    }

    /* 🚫 Remove padding exagerado da página */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* 🔳 Bordas de containers e widgets */
    .stContainer {
        border-radius: 8px;
    }

    /* 🎯 Selectbox, buttons e inputs */
    button, .stButton>button {
        background-color: #21252b;
        color: #f5f5f5;
        border: 1px solid #2c2f36;
        border-radius: 8px;
    }
    button:hover {
        background-color: #2a2e36;
        color: #fff;
    }

    .stSelectbox, .stTextInput, .stDateInput, .stMultiSelect {
        background-color: #161921;
        color: #f5f5f5;
        border-radius: 8px;
    }

    /* ✅ Checkbox e radio */
    .stCheckbox > label, .stRadio > label {
        color: #f5f5f5;
    }

    </style>
    """,
    unsafe_allow_html=True
)
st.markdown(
    """
    <style>
    /* 🔧 Reduz o padding geral da página */
    .block-container {
        padding-top: 1.5rem;
        padding-bottom: 1.5rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }

    /* 🎯 Reduz espaço da sidebar */
    [data-testid="stSidebar"] > div:first-child {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }

    /* 🧽 Remove espaçamentos desnecessários entre os elementos */
    .stMarkdown {
        margin-bottom: 0.5rem;
    }

    /* 🎨 Ajusta títulos */
    h1 {
        font-size: 2.2rem;
        margin-bottom: 0.2rem;
    }

    h2 {
        font-size: 1.8rem;
        margin-bottom: 0.2rem;
    }

    h3 {
        font-size: 1.4rem;
        margin-bottom: 0.2rem;
    }

    h4, h5, h6 {
        margin-bottom: 0.1rem;
    }

    /* 🔸 Estilo dos divisores */
    hr {
        border: none;
        border-top: 1px solid rgba(0,0,0,0.15);
        margin-top: 6px;
        margin-bottom: 6px;
    }

    /* 🌈 Fonte geral mais clean */
    html, body, [class*="css"] {
        font-family: 'Inter', sans-serif;
        font-size: 0.95rem;
    }

    /* 🔳 Bordas dos containers */
    .stContainer {
        border-radius: 8px;
    }

    /* 🔗 Remove underline dos links */
    a {
        text-decoration: none;
    }

    /* 💠 Caixa das métricas */
    .stMetric {
        background-color: #f9f9f9;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 0 0 5px rgba(0,0,0,0.05);
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Título
st.markdown("## 🍣 **Visão Estratégica | Fuji Analytics**")

# Linha depois do título
st.markdown(
    """
    <hr style="
        margin-top: 5px;
        margin-bottom: 5px;
        border: none;
        border-top: 1px solid rgba(0,0,0,0.15);
    ">
    """,
    unsafe_allow_html=True
)

# Sidebar – Filtros
with st.sidebar:
    st.markdown("### 🏢 **Filial**")
    filial = st.selectbox("Selecione a filial", ["Todas", "Aldeota", "Cambeba"])

    st.markdown("### 📅 **Período**")
    data_inicio = st.date_input("Data de início")
    data_fim = st.date_input("Data de fim")

# Carregar Dados
df_receitas, df_despesas = carregar_dataframes()

# Formatar Dados
df_receitas = formatar_dataframe(df_receitas, **config_receitas)
df_despesas = formatar_dataframe(df_despesas, **config_despesas)

# Filtrar por Filial
dict_receitas = filtrar_por_filial(df_receitas)
dict_despesas = filtrar_por_filial(df_despesas)

# Filtrar por Data e Filial
df_receitas_filtrado, df_despesas_filtrado = processar_filial(
    dict_receitas,
    dict_despesas,
    df_receitas,
    df_despesas,
    filial,
    data_inicio,
    data_fim
)

# 🔥 Métricas Financeiras
exibir_metricas_financeiras(df_receitas_filtrado, df_despesas_filtrado)

# Linha depois das métricas
st.markdown(
    """
    <hr style="
        margin-top: 5px;
        margin-bottom: 5px;
        border: none;
        border-top: 1px solid rgba(0,0,0,0.15);
    ">
    """,
    unsafe_allow_html=True
)

# 🔍 Título dos Gráficos
st.markdown("#### 🔍 Distribuição de Receita e Despesas")

# Abas
tipo_visualizacao, agrupar_outros = exibir_abas()

# Agrupar por Categoria
df_receitas_por_categoria = agrupar_por_categoria(
    df_receitas_filtrado, "Grupo", "Valor", agrupar_outros
)
df_despesas_por_categoria = agrupar_por_categoria(
    df_despesas_filtrado, "Centro_Custo", "Valor_Pago/Recebido", agrupar_outros
)

# Gráficos
exibir_graficos(
    tipo_visualizacao, df_receitas_por_categoria, df_despesas_por_categoria
)