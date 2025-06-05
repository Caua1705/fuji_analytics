import streamlit as st
from carregamento.carregar_dados import carregar_e_preparar_dados

def obter_dados():
    if "df_receitas" not in st.session_state or "df_despesas" not in st.session_state or "df_catalogo" not in st.session_state:
        df_receitas, df_despesas, df_catalogo= carregar_e_preparar_dados()
        st.session_state.df_receitas = df_receitas
        st.session_state.df_despesas = df_despesas
        st.session_state.df_catalogo = df_catalogo
    else:
        df_receitas = st.session_state.df_receitas
        df_despesas = st.session_state.df_despesas
        df_catalogo = st.session_state.df_catalogo 

    return df_receitas, df_despesas, df_catalogo