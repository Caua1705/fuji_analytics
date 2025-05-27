import streamlit as st

def exibir_abas():
    tipo_visualizacao = st.radio(
        "Qual forma de visualização?",
        ["📊 Valores absolutos", "📉 Proporção percentual"],
        horizontal=True,
        label_visibility="collapsed")

    if tipo_visualizacao == "📉 Proporção percentual":
        agrupar_outros = True
    else:
        agrupar_outros = False
    return tipo_visualizacao,agrupar_outros