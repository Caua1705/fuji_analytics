import streamlit as st
from carregamento.carregar_dados import carregar_dataframes

if "df_receitas" not in st.session_state:
    df_receitas=carregar_dataframes()
    st.session_state.df_receitas = df_receitas
else:
    df_receitas=st.session_state.df_receitas

st.write(df_receitas)