import streamlit as st
# Carregar Dados
from utils.dados_em_sessao import obter_dados
from utils.estilo import aplicar_estilo_pagina
from view.sidebar import exibir_sidebar
from processamento.filtrar import filtrar_por_filial,processar_filial
from view.metricas import exibir_metricas_desempenho_produtos
from view.insights import insight_produtos_sem_vendas,produtos_em_decadencia,produtos_em_ascensao
from view.graficos import criar_grafico_produtos

aplicar_estilo_pagina(
    titulo="Análise de Desempenho de Produtos",
    metricas_config = [
        {"bg_color": "#e8f5e9", "border_color": "#4CAF50"}, 
        {"bg_color": "#e3f2fd", "border_color": "#2196F3"},  
        {"bg_color": "#fff3e0", "border_color": "#FF9800"},  
        {"bg_color": "#ede7f6", "border_color": "#9C27B0"}, 
    ]
)

#Carregar Dados
df_receitas,df_despesas,df_catalogo=obter_dados()

# Sidebar 
data_inicio,data_fim,filial=exibir_sidebar()

# Filtrar por Filial
dict_receitas = filtrar_por_filial(df_receitas)
dict_despesas = filtrar_por_filial(df_despesas)

# Filtrar Filial por Data
df_receitas_filtrado,df_despesas_filtrado,df_receitas_anterior,df_despesas_filtrado_anterior = processar_filial(
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

#Métricas
exibir_metricas_desempenho_produtos(df_receitas_filtrado)

tab1,tab2,tab3,tab4=st.tabs(["📈 Resumo","🍽️ Comidas","🍷 Bebidas","💼 Lucratividade"])
with tab1:
    col1,col2,col3=st.columns(3)
    with col1:
        insight_produtos_sem_vendas(df_receitas_filtrado,df_catalogo,data_inicio,data_fim)
    with col2:
        produtos_em_ascensao(df_receitas_filtrado,df_receitas_anterior,data_inicio,data_fim)
    with col3:
        produtos_em_decadencia(df_receitas_filtrado,df_receitas_anterior,data_inicio,data_fim)
        
    criar_grafico_produtos(df_receitas, "Produto", "Quantidade", "Valor", "Decadência")