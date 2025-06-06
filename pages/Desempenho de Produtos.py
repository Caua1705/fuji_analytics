import streamlit as st
# Carregar Dados
from utils.dados_em_sessao import obter_dados
from utils.estilo import aplicar_estilo_pagina
from view.sidebar import exibir_sidebar
from processamento.filtrar import filtrar_por_filial,processar_filial,pegar_30_dias_anteriores
from view.metricas import exibir_metricas_desempenho_produtos
from processamento.agrupar import criar_curva_abc,agrupar_por_produto
from view.insights import insight_produtos_sem_vendas,produtos_em_decadencia

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

#Métricas
exibir_metricas_desempenho_produtos(df_receitas_filtrado)

tab1,tab2,tab3,tab4=st.tabs(["📈 Resumo","🍽️ Comidas","🍷 Bebidas","💼 Lucratividade"])
with tab1:
    col1,col2,col3=st.columns(3)
    with col1:
        df_receitas_por_produto=agrupar_por_produto(df_receitas_filtrado,"Produto","Quantidade","Valor")
        insight_produtos_sem_vendas(df_receitas_por_produto,df_catalogo,data_inicio,data_fim)
    with col2:
        df_filtrado_30_dias=pegar_30_dias_anteriores(df_receitas,"Data",data_inicio)

        df_receitas_por_produto=agrupar_por_produto(df_receitas_filtrado,"Produto","Quantidade","Valor")
        df_30_dias_por_produto=agrupar_por_produto(df_filtrado_30_dias,"Produto","Quantidade","Valor")

        produtos_em_decadencia(df_receitas_por_produto,df_30_dias_por_produto)
    with col3:
        pass
    df_receitas_curva_abc=criar_curva_abc(df_receitas_filtrado)
    st.write(df_receitas_curva_abc)