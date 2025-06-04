import streamlit as st
from utils.formatadores import formatar_moeda,formatar_porcentagem

def calcular_receita_total(df_receitas):
    return df_receitas["Valor"].sum()
    
def calcular_despesa_total(df_despesas):
    return df_despesas["Valor Pago"].sum()

def calcular_resultado(receitas,despesas):
    return receitas-despesas

def calcular_margem_lucro(resultado,receitas):
    return (resultado/receitas) * 100

def exibir_metricas_financeiras_visao_geral(df_receitas,df_despesas):
    receita_total=calcular_receita_total(df_receitas)
    despesa_total=calcular_despesa_total(df_despesas)
    resultado=calcular_resultado(receita_total,despesa_total)
    margem_lucro=calcular_margem_lucro(resultado,receita_total)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Receita Total",f"{formatar_moeda(receita_total)}")
    with col2:
        st.metric("Despesa Total",f"{formatar_moeda(despesa_total)}")
    with col3:
        st.metric("Resultado Financeiro",f"{formatar_moeda(resultado)}")
    with col4:
        st.metric("Margem de Lucro",f"{formatar_porcentagem(margem_lucro)}")

def produto_mais_vendido(df_receitas):
    pass


        
