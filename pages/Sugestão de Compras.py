import streamlit as st
import pandas as pd
from utils.dados_em_sessao import obter_dados
from processamento.filtrar import filtrar_por_filial,processar_filial
from datetime import timedelta

st.markdown("### 📅 Desempenho Diário")

df_receitas,df_despesas,_=obter_dados()

with st.sidebar:
    st.markdown("### 🏢 **Filial**")
    filial = st.selectbox("Selecione a filial", ["Todas", "Aldeota", "Cambeba"])
    
# Filtrar por Filial
dict_receitas = filtrar_por_filial(df_receitas)
dict_despesas = filtrar_por_filial(df_despesas)