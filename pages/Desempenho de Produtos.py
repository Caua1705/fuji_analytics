import streamlit as st
from carregamento.carregar_dados import carregar_dataframes
from utils.estilo import aplicar_estilo_pagina
from view.sidebar import exibir_sidebar

if "df_receitas" not in st.session_state:
    df_receitas=carregar_dataframes()
    st.session_state.df_receitas = df_receitas
else:
    df_receitas=st.session_state.df_receitas

aplicar_estilo_pagina(
    titulo="Análise de Desempenho de Produtos",
    metricas_config=[
        {"bg_color": "#e8f5e9", "border_color": "#4CAF50"},  
        {"bg_color": "#ffebee", "border_color": "#F44336"},  
        {"bg_color": "#e3f2fd", "border_color": "#2196F3"},  
        {"bg_color": "#ede7f6", "border_color": "#9C27B0"},  
    ]
)

data_inicio,data_fim,filial=exibir_sidebar()

st.write(df_receitas)