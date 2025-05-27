import plotly.express as px
import streamlit as st

def criar_graficos_principais_receitas(receitas_por_categoria, tipo_visualizacao):
    cores_receitas = {
    "COMBINADOS": "#1f77b4", 
    "DRINKS": "#aec7e8",     
    "FRUTAS": "#ff7f0e",     
    "TEMAKI": "#ffbb78",      
    "PASTE": "#2ca02c",       
    "Outros": "#d3d3d3"} 
    fig1 = px.bar(
        receitas_por_categoria,
        x="Grupo",
        y="Valor",
        title="Receitas por Categoria",
        text_auto=".2s",
        color="Grupo",
        color_discrete_map=cores_receitas)
    fig1.update_layout(
        xaxis_title="Grupo",
        yaxis_title="Valor",
        showlegend=False,
        xaxis_tickangle=0,
         title={
        'text': "Receitas por Categoria",
        'x': 0.5,
        'xanchor': 'center'
        })
    fig1.update_traces(texttemplate='%{y:.2s}', textposition='outside')

    fig2 = px.pie(
        receitas_por_categoria,
        names="Grupo",
        values="Valor",
        title="Receitas por Categoria",
        hole=0.4)
    fig2.update_traces(textinfo="percent+label")

    if tipo_visualizacao == "📊 Valores absolutos":
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.plotly_chart(fig2, use_container_width=True)

def criar_graficos_principais_despesas(despesas_por_categoria,tipo_visualizacao):
    cores_despesas = {
    "ALUGUEL": "#d62728",       
    "MARKETING": "#ff9896",     
    "FUNCIONÁRIOS": "#9467bd",  
    "FORNECEDORES": "#8c564b", 
    "INSUMOS": "#e377c2",       
    "Outros": "#d3d3d3"}
    fig1=px.bar(despesas_por_categoria,
                x="Centro_Custo",
                y="Valor_Pago/Recebido",
                title="Despesas por Categoria",
                text_auto=".2s",
                color="Centro_Custo",
                color_discrete_map=cores_despesas)
    fig1.update_layout(xaxis_title="Centro de Custo",
                       yaxis_title="Valor",
                       showlegend=False,
                       xaxis_tickangle=0,
                       title={
        'text': "Receitas por Categoria",
        'x': 0.5,
        'xanchor': 'center'})
    fig1.update_traces(texttemplate='%{y:.2s}', textposition='outside')

    fig2=px.pie(despesas_por_categoria,names="Centro_Custo",values="Valor_Pago/Recebido",title="Despesas por Categoria")
    if tipo_visualizacao=="📊 Valores absolutos":
        st.plotly_chart(fig1)
    else:
        st.plotly_chart(fig2)