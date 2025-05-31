import streamlit as st
# Carregar Dados
from carregamento.carregar_dados import carregar_dataframes
# Formatar Dados
from utils.formatar import formatar_dataframe
from utils.config_formatacao import config_receitas, config_despesas
from utils.estilo import aplicar_estilo,inserir_logo,linha_divisoria
# Filtrar Dados
from processamento.filtrar import filtrar_por_filial, processar_filial
# Exibir Métricas
from view.metricas import exibir_metricas_financeiras
# Agrupar Dados
from processamento.agrupar import agrupar_receitas_por_categoria,agrupar_despesas_por_categoria
# Exibir Gráficos
from view.graficos import exibir_graficos
from view.insights import insight_receitas

# Configuração da Página
st.set_page_config(layout="wide")
aplicar_estilo()

# Logo Fixa
inserir_logo("https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png", 100)

# Título
st.markdown("## 🍣 **Visão Estratégica | Fuji Analytics**")

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

# Filtrar por Data
df_receitas_filtrado, df_despesas_filtrado = processar_filial(
    dict_receitas,
    dict_despesas,
    df_receitas,
    df_despesas,
    filial,
    data_inicio,
    data_fim
)

#Métricas Financeiras
exibir_metricas_financeiras(df_receitas_filtrado, df_despesas_filtrado)
linha_divisoria()

modo_percentual = st.toggle("📊 Mostrar em proporção (%)", value=False)
if modo_percentual:
    agrupar_outros=True
else:
    agrupar_outros=False

# Agrupar por Categoria
df_receitas_por_categoria = agrupar_receitas_por_categoria(df_receitas_filtrado, "Grupo", "Valor","Quantidade",agrupar_outros)
df_despesas_por_categoria = agrupar_despesas_por_categoria(df_despesas_filtrado, "Centro_Custo", "Valor_Pago/Recebido",agrupar_outros)

# Gráficos
exibir_graficos(df_receitas_por_categoria, df_despesas_por_categoria,filial,agrupar_outros)
insight_receitas(df_receitas_por_categoria)