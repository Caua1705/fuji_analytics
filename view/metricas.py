import streamlit as st

def calcular_receita_total(df_receitas):
    return df_receitas["Valor"].sum()
    
def calcular_despesa_total(df_despesas):
    return df_despesas["Valor_Pago/Recebido"].sum()

def calcular_resultado(receitas,despesas):
    return receitas-despesas

def calcular_margem_lucro(resultado,receitas):
    return (resultado/receitas) * 100

def exibir_metricas_financeiras(df_receitas,df_despesas):
    receita_total=calcular_receita_total(df_receitas)
    despesa_total=calcular_despesa_total(df_despesas)
    resultado=calcular_resultado(receita_total,despesa_total)
    margem_lucro=calcular_margem_lucro(resultado,receita_total)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Receita Total",f"R$ {receita_total:,.2f}")
    with col2:
        st.metric("Despesa Total",f"R$ {despesa_total:,.2f}")
    with col3:
        st.metric("Resultado Financeiro",f"R${resultado:,.2f}")
    with col4:
        st.metric("Margem de Lucro",f"{margem_lucro:,.2f}%")


        
