import streamlit as st

def exibir_abas():
    st.subheader("Distribuição de Receita e Despesas")
    modo_percentual = st.toggle("📊 Mostrar proporção percentual", value=False)
    if modo_percentual:
        tipo_visualizacao = "Proporção percentual"
        agrupar_outros = True
    else:
        tipo_visualizacao = "Valores absolutos"
        agrupar_outros = False
    return tipo_visualizacao,agrupar_outros

