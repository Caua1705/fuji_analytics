import plotly.express as px
from plotly.colors import qualitative
import streamlit as st

def criar_graficos_barra(df_agrupado,tipo_df,x,y,filial):
    if tipo_df=="Receitas":
        cores = ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b"]
        titulo=f"Distribuição da Receita por Categoria - {filial}"
    else:
        cores = ["#17becf","#bcbd22","#e377c2","#7f7f7f","#ffbb78","#aec7e8"]
        titulo=f"Distribuição das Despesas por Centro de Custo - {filial}"

    fig_bar=px.bar(
        df_agrupado,
        x=x,
        y=y,
        text_auto=".2s",
        color=x,
        color_discrete_sequence=cores,
        width=300
        )
    fig_bar.update_layout(
        xaxis_title=x,
        yaxis_title=y,
        showlegend=False,
        xaxis_tickangle=0,
        title={
        'text': titulo,
        'x': 0.0,
        'xanchor': 'left'
    })
    
    fig_bar.update_traces(textposition='outside')  
    
    st.plotly_chart(fig_bar,use_container_width=True)

def criar_graficos_pizza(df_agrupado,tipo_df,x,y,filial):
    if tipo_df=="Receitas":
        titulo=f"Distribuição da Receita por Categoria - {filial}"
    else:
        titulo=f"Distribuição das Despesas por Centro de Custo - {filial}"
    fig_pie = px.pie(
        df_agrupado,
        names=x,
        values=y,
        title=titulo,
        hole=0.4,
        color_discrete_sequence=qualitative.Set3
        )
    fig_pie.update_layout(showlegend=True,legend=dict(orientation="v", x=1, y=0.5))
    fig_pie.update_traces(textinfo="percent+label")

    st.plotly_chart(fig_pie,use_container_width=True)

def exibir_graficos(tipo_visualizacao, df_receitas, df_despesas,filial):
    col1, col2 = st.columns(2)

    if tipo_visualizacao == "Valores absolutos":
        with col1:
            criar_graficos_barra(df_receitas, "Receitas", "Grupo", "Valor",filial)
        with col2:
            criar_graficos_barra(df_despesas, "Despesas", "Centro_Custo", "Valor_Pago/Recebido",filial)
    else:
        with col1:
            criar_graficos_pizza(df_receitas, "Receitas", "Grupo", "Valor",filial)
        with col2:
            criar_graficos_pizza(df_despesas, "Despesas", "Centro_Custo", "Valor_Pago/Recebido",filial)
