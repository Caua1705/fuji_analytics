import streamlit as st

def exibir_abas():
    aba1, aba2 = st.tabs(["Visão Financeira", "Evolução Mensal"])

    tipo_visualizacao = st.radio(
        "Qual forma de visualização?",
        ["📊 Valores absolutos", "📉 Proporção percentual"],
        horizontal=True,
        label_visibility="collapsed")
        
    if tipo_visualizacao == "📉 Proporção percentual":
        agrupar_outros = True
    else:
        agrupar_outros = False
    return aba1,aba2,agrupar_outros