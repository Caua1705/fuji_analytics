import streamlit as st
from carregamento.carregar_dados import carregar_e_preparar_dados
from utils.estilo import aplicar_estilo_pagina
from view.sidebar import exibir_sidebar
from processamento.filtrar import filtrar_por_filial,processar_filial
from view.metricas import exibir_metricas_desempenho_produtos

if "df_receitas" not in st.session_state:
    df_receitas=carregar_e_preparar_dados()
    st.session_state.df_receitas = df_receitas
else:
    df_receitas=st.session_state.df_receitas

aplicar_estilo_pagina(
    titulo="Análise de Desempenho de Produtos",
    metricas_config = [
        {"bg_color": "#e8f5e9", "border_color": "#4CAF50"}, 
        {"bg_color": "#e3f2fd", "border_color": "#2196F3"},  
        {"bg_color": "#fff3e0", "border_color": "#FF9800"},  
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

exibir_metricas_desempenho_produtos(df_receitas)