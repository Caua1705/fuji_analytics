import streamlit as st
# Carregar Dados
from carregamento.carregar_dados import carregar_e_preparar_dados
#Estilizar a Página
from utils.estilo import aplicar_estilo_pagina,linha_divisoria
# Filtrar Dados
from processamento.filtrar import filtrar_por_filial, processar_filial
#Exibir Sidebar:
from view.sidebar import exibir_sidebar
# Exibir Métricas
from view.metricas import exibir_metricas_visao_geral
# Agrupar Dados
from processamento.agrupar import agrupar_receitas_por_categoria,agrupar_despesas_por_categoria
# Exibir Gráficos
from view.graficos import criar_graficos_barra,criar_graficos_pizza
from view.insights import insight_receitas,insight_despesas



# Configuração da Página
st.set_page_config(layout="wide",page_icon="🍣")
aplicar_estilo_pagina(
    titulo="Dashboard de Análise",
    metricas_config=[
        {"bg_color": "#e8f5e9", "border_color": "#4CAF50"},  
        {"bg_color": "#ffebee", "border_color": "#F44336"},  
        {"bg_color": "#e3f2fd", "border_color": "#2196F3"},  
        {"bg_color": "#ede7f6", "border_color": "#9C27B0"},  
    ]
)

# Sidebar 
data_inicio,data_fim,filial=exibir_sidebar()

# Carregar Dados
df_receitas, df_despesas = carregar_e_preparar_dados()

# Filtrar por Filial
dict_receitas = filtrar_por_filial(df_receitas)
dict_despesas = filtrar_por_filial(df_despesas)

# Filtrar Filial por Data
df_receitas_filtrado,df_despesas_filtrado,df_receitas_filtrado_anterior,df_despesas_filtrado_anterior = processar_filial(
    dict_receitas,
    dict_despesas,
    filial,
    data_inicio,
    data_fim
)
#Verifica se há Dados
if df_receitas_filtrado.empty and df_despesas_filtrado.empty:
    st.warning("⚠️ **Aviso:** Nenhum dado disponível para o período selecionado. Verifique os parâmetros e refaça a consulta.")
    st.stop()

#Métricas Financeiras
exibir_metricas_visao_geral(df_receitas_filtrado, df_despesas_filtrado)
linha_divisoria()

modo_percentual = st.toggle("Mostrar em proporção (%)", value=False)
if modo_percentual:
    agrupar_outros=True
else:
    agrupar_outros=False

# Agrupar por Categoria
df_receitas_por_categoria = agrupar_receitas_por_categoria(df_receitas_filtrado, "Grupo", "Valor","Quantidade",agrupar_outros)
df_despesas_anterior_por_categoria = agrupar_despesas_por_categoria(df_despesas_filtrado_anterior, "Centro_Custo", "Valor Pago",agrupar_outros)
df_despesas_por_categoria = agrupar_despesas_por_categoria(df_despesas_filtrado, "Centro_Custo", "Valor Pago",agrupar_outros)

# Gráficos
col1, col2 = st.columns(2)
with col1:
    insight_receitas(df_receitas_por_categoria,data_inicio,data_fim)
    if not df_receitas_por_categoria.empty:
        st.subheader(f"Receitas por Categoria")
        if agrupar_outros:
            criar_graficos_pizza(df_receitas_por_categoria, "Receitas", "Grupo", "Valor", filial)
        else:
            criar_graficos_barra(df_receitas_por_categoria, "Receitas", "Grupo", "Valor", filial)

with col2:
    insight_despesas(df_despesas_por_categoria,df_despesas_anterior_por_categoria,data_inicio,data_fim)
    if not df_despesas_por_categoria.empty:
        st.subheader("Despesas por Centro de Custo")
        if agrupar_outros:
            criar_graficos_pizza(df_despesas_por_categoria, "Despesas", "Centro_Custo", "Valor Pago", filial)
        else:
            criar_graficos_barra(df_despesas_por_categoria, "Despesas", "Centro_Custo", "Valor Pago", filial)

    