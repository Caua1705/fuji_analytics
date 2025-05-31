import streamlit as st
from datetime import date,timedelta 
def exibir_sidebar():
    with st.sidebar:
        st.markdown("### 🏢 **Filial**")
        filial = st.selectbox("Selecione a filial", ["Todas", "Aldeota", "Cambeba"])
        st.markdown("### 📅 **Período**")
        data_hoje=date.today()
        data_inicio = st.date_input("Data de início",value=data_hoje-timedelta(days=30),format="DD/MM/YYYY")
        data_fim = st.date_input("Data de fim",value=data_hoje,format="DD/MM/YYYY")
        data_inicio_formatada=data_inicio.strftime("%Y/%m/%d")
        data_fim_formatada=data_fim.strftime("%Y/%m/%d")
    return data_inicio_formatada,data_fim_formatada,filial