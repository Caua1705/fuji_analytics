import plotly.express as px
from plotly.colors import qualitative
import streamlit as st

def criar_graficos_principais_receitas(receitas_por_categoria,tipo_visualizacao):
    cores_receitas = [
    "#1f77b4",  # azul escuro
    "#ff7f0e",  # laranja vibrante
    "#2ca02c",  # verde forte
    "#d62728",  # vermelho
    "#9467bd",  # roxo
    "#8c564b"   # marrom
]
    fig1 = px.bar(
        receitas_por_categoria,
        x="Grupo",
        y="Valor",
        title="Receitas por Categoria",
        text_auto=".2s",
        color="Grupo",
        color_discrete_sequence=cores_receitas)
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
        title="Despesas por Categoria",
        hole=0.4,
        color_discrete_sequence=qualitative.Set3
        )
    fig2.update_layout(
    showlegend=True,
    legend=dict(orientation="v", x=1, y=0.5)
)
    fig2.update_traces(textinfo="percent+label")

    if tipo_visualizacao == "📊 Valores absolutos":
        st.plotly_chart(fig1, use_container_width=True)
    else:
        st.plotly_chart(fig2, use_container_width=True)

def criar_graficos_principais_despesas(despesas_por_categoria,tipo_visualizacao):
    cores_despesas = [
    "#17becf",  # ciano
    "#bcbd22",  # verde-oliva
    "#e377c2",  # rosa claro
    "#7f7f7f",  # cinza médio
    "#ffbb78",  # amarelo claro
    "#aec7e8"   # azul claro
]
    fig1=px.bar(despesas_por_categoria,
                x="Centro_Custo",
                y="Valor_Pago/Recebido",
                title="Despesas por Categoria",
                text_auto=".2s",
                color="Centro_Custo",
                color_discrete_sequence=cores_despesas)
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
    fig2 = px.pie(
        despesas_por_categoria,
        names="Centro_Custo",
        values="Valor_Pago/Recebido",
        title="Despesas por Categoria",
        hole=0.4,
        color_discrete_sequence=qualitative.Set3
        )    
    fig2.update_layout(
    showlegend=True,
    legend=dict(orientation="v", x=1, y=0.5)
)
    
    fig2.update_traces(textinfo="percent+label")

    if tipo_visualizacao=="📊 Valores absolutos":
        st.plotly_chart(fig1)
    else:
        st.plotly_chart(fig2)