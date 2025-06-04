import pandas as pd
import streamlit as st
from pathlib import Path
from utils.config_formatacao import config_receitas, config_despesas
from utils.formatadores import formatar_dataframe,formatar_quantidade

dir_raiz=Path(__file__).parents[1]

@st.cache_data

def carregar_e_preparar_dados():
    df_receitas=pd.read_excel(dir_raiz / "data" / "receitas.xlsx")
    df_despesas = pd.read_excel(dir_raiz / "data" / "despesas.xlsx")

    df_receitas = formatar_dataframe(df_receitas, **config_receitas)
    df_receitas = formatar_quantidade(df_receitas,"Quantidade")
    df_despesas = formatar_dataframe(df_despesas, **config_despesas)

    st.session_state.df_receitas=df_receitas
    st.session_state.df_despesas=df_despesas
    
    return df_receitas,df_despesas