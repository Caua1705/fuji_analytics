import streamlit as st
from utils.formatadores import formatar_moeda,formatar_porcentagem,formatar_unidade

def calcular_receita_total(df_receitas):
    return df_receitas["Valor"].sum()
    
def calcular_despesa_total(df_despesas):
    return df_despesas["Valor Pago"].sum()

def calcular_resultado(receitas,despesas):
    return receitas-despesas

def calcular_margem_lucro(resultado,receitas):
    return (resultado/receitas) * 100

def exibir_metricas_visao_geral(df_receitas,df_despesas):
    receita_total=calcular_receita_total(df_receitas)
    despesa_total=calcular_despesa_total(df_despesas)
    resultado=calcular_resultado(receita_total,despesa_total)
    margem_lucro=calcular_margem_lucro(resultado,receita_total)
    st.write(df_despesas)
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
    df_quantidade_produtos = df_receitas.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False)
    return df_quantidade_produtos.index[0]

def produto_maior_faturamento(df_receitas):
    df_valor_produtos= df_receitas.groupby("Produto")["Valor"].sum().sort_values(ascending=False)
    return df_valor_produtos.index[0]

def calcular_total_unidades(df_receitas):
    df_quantidade_produtos= df_receitas.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False).reset_index()
    return df_quantidade_produtos["Quantidade"].sum()

def calcular_ticket_medio(df_receitas,quantidade_total_produtos):
    df_valor_produtos= df_receitas.groupby("Produto")["Valor"].sum().sort_values(ascending=False).reset_index()
    valor_total_produtos=df_valor_produtos["Valor"].sum()
    return valor_total_produtos/quantidade_total_produtos

def exibir_metricas_desempenho_produtos(df_receitas):
    top1_quantidade=produto_mais_vendido(df_receitas)
    top1_faturamento=produto_maior_faturamento(df_receitas)
    total_unidades_vendidas=calcular_total_unidades(df_receitas)
    ticket_medio=calcular_ticket_medio(df_receitas,total_unidades_vendidas)
    col1,col2,col3,col4=st.columns(4)
    with col1:
        st.metric("Produto Mais Vendido",f"{top1_quantidade}")
    with col2:
        st.metric("Produto de Maior Faturamento",f"{top1_faturamento}")
    with col3:
        st.metric("Total Geral de Unidades Vendidas",f"{formatar_unidade(total_unidades_vendidas)}")
    with col4:
        st.metric("Ticket Médio dos Produtos",f"{formatar_moeda(ticket_medio)}")






        
