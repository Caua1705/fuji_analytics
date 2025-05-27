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
st.set_page_config(layout="wide")

# Logo Fixa
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

        /* 🔸 Divisor fino, discreto e elegante */
        hr {
            margin-top: 5px;
            margin-bottom: 5px;
            border: none;
            border-top: 1px solid #DADADA;
        }

        /* 🔹 Reduzir espaço interno da página (opcional) */
        .block-container {
            padding-top: 1rem;
            padding-bottom: 1rem;
        }

        /* 🔸 Títulos mais próximos, sem espaço extra */
        h1, h2, h3, h4, h5, h6 {
            margin-bottom: 0.5rem;
            margin-top: 0.5rem;
        }

        /* 🔹 Bordas e caixas mais suaves */
        .stMetric {
            background-color: #F9F9F9;
            border-radius: 8px;
            padding: 10px;
            border: 1px solid #E0E0E0;
        }

    </style>

    <div class="logo-fixed">
        <img 
            src="https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png" 
            width="100">
    </div>
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