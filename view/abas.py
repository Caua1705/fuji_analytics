import streamlit as st

def exibir_abas():
    aba1, aba2 = st.tabs(["Visão Financeira", "Evolução Mensal"])
    with aba1:
        tipo_visualizacao = st.radio(
            "Qual forma de visualização?",
            ["📊 Valores absolutos", "📉 Proporção percentual"],
            horizontal=True,
            label_visibility="collapsed")

        if tipo_visualizacao == "📉 Proporção percentual":
            agrupar_outros = True
        else:
            agrupar_outros = False
    with aba2:
        st.write("Nada Ainda")
    return tipo_visualizacao,agrupar_outros