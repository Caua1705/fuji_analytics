import streamlit as st
# Carregar Dados
from carregamento.carregar_dados import carregar_dataframes
# Formatar Dados
from utils.formatadores import formatar_dataframe
from utils.config_formatacao import config_receitas, config_despesas
from utils.estilo import aplicar_estilo,inserir_logo,linha_divisoria
# Filtrar Dados
from processamento.filtrar import filtrar_por_filial, processar_filial
#Exibir Sidebar:
from view.sidebar import exibir_sidebar
# Exibir Métricas
from view.metricas import exibir_metricas_financeiras
# Agrupar Dados
from processamento.agrupar import agrupar_receitas_por_categoria,agrupar_despesas_por_categoria
# Exibir Gráficos
from view.graficos import criar_graficos_barra,criar_graficos_pizza
from view.insights import insight_receitas

# Configuração da Página
st.set_page_config(layout="wide")
aplicar_estilo()

# Logo Fixa
inserir_logo("https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png", 100)

# Título
st.markdown("## 🍣 **Visão Estratégica | Fuji Analytics**")

# Sidebar 
data_inicio,data_fim,filial=exibir_sidebar()

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
col1, col2 = st.columns(2)

with col1:
    # st.subheader("Receitas por Categoria")
    insight_receitas(df_receitas_por_categoria)
    if agrupar_outros:
        criar_graficos_pizza(df_receitas_por_categoria, "Receitas", "Grupo", "Valor", filial)
    else:
        criar_graficos_barra(df_receitas_por_categoria, "Receitas", "Grupo", "Valor", filial)

with col2:
    st.subheader("Despesas por Centro de Custo")
    if agrupar_outros:
        criar_graficos_pizza(df_despesas_por_categoria, "Despesas", "Centro_Custo", "Valor_Pago/Recebido", filial)
    else:
        criar_graficos_barra(df_despesas_por_categoria, "Despesas", "Centro_Custo", "Valor_Pago/Recebido", filial)
