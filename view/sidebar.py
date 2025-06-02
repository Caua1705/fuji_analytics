import streamlit as st
from datetime import date
def exibir_sidebar():
    with st.sidebar:
        st.markdown("### 🏢 **Filial**")
        filial = st.selectbox("Selecione a filial", ["Todas", "Aldeota", "Cambeba"])
        st.markdown("### 📅 **Período**")

        data_hoje=date.today()
        primeiro_dia_mes = data_hoje.replace(day=1)

        data_inicio = st.date_input("Data de início",value=primeiro_dia_mes,format="DD/MM/YYYY")
        data_fim = st.date_input("Data de fim",value=data_hoje,format="DD/MM/YYYY")
    return data_inicio,data_fim,filial