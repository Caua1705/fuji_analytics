import streamlit as st
#Carregar Dados
from carregamento.carregar_dados import carregar_dataframes
#Formatar Dados
from utils.formatar import formatar_dataframe
from utils.config_formatacao import config_receitas,config_despesas
#Filtrar Dados
from processamento.filtrar import filtrar_por_filial,processar_filial
#Exibir Métricas
from view.metricas import exibir_metricas_financeiras
#Agrupar Dados
from processamento.agrupar import agrupar_por_categoria
#Exibir abas:
from view.abas import exibir_abas
#Exibir Gráficos
from view.graficos import exibir_graficos

st.set_page_config(layout="wide")
st.markdown("## 📊 Visão Geral do Negócio")

#Filtros Sidebar
with st.sidebar:
    st.subheader("Filial")
    filial=st.sidebar.selectbox("Selecione a filial",["Todas","Aldeota","Cambeba"])
    st.subheader("📅 Filtros de Período")
    data_inicio = st.date_input("Data de início")
    data_fim = st.date_input("Data de fim")

#Carregar Dados
df_receitas,df_despesas=carregar_dataframes()

#Formatar dados
df_receitas=formatar_dataframe(df_receitas,**config_receitas)
df_despesas=formatar_dataframe(df_despesas,**config_despesas)

#Filtrar por filial:
dict_receitas=filtrar_por_filial(df_receitas)
dict_despesas=filtrar_por_filial(df_despesas)

#Filtrar por Data
df_receitas_filtrado,df_despesas_filtrado=processar_filial(dict_receitas,
                                                           dict_despesas,
                                                           df_receitas,
                                                           df_despesas,
                                                           filial,
                                                           data_inicio,
                                                           data_fim)
#Métricas
exibir_metricas_financeiras(df_receitas_filtrado,df_despesas_filtrado)

#Abas
tipo_visualizacao,agrupar_outros=exibir_abas()

#Agrupar por Categoria
df_receitas_por_categoria = agrupar_por_categoria(df_receitas_filtrado, "Grupo", "Valor", agrupar_outros)
df_despesas_por_categoria = agrupar_por_categoria(df_despesas_filtrado, "Centro_Custo", "Valor_Pago/Recebido", agrupar_outros)

#Exibir Gráficos:
exibir_graficos(tipo_visualizacao,df_receitas_por_categoria,df_despesas_por_categoria)

    

