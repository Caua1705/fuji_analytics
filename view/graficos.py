import plotly.express as px
from plotly.colors import qualitative
import streamlit as st

def criar_graficos_barra(df_agrupado,tipo_df,x,y):
    if tipo_df=="Receitas":
        cores = ["#1f77b4","#ff7f0e","#2ca02c","#d62728","#9467bd","#8c564b"]
        titulo="Receitas por Categoria"
    else:
        cores = ["#17becf","#bcbd22","#e377c2","#7f7f7f","#ffbb78","#aec7e8"]
        titulo="Despesas por Categoria"

    fig_bar=px.bar(
        df_agrupado,
        x=x,
        y=y,
        text_auto=".2s",
        color=x,
        color_discrete_sequence=cores
        )
    fig_bar.update_layout(
        xaxis_title=x,
        yaxis_title=y,
        showlegend=False,
        xaxis_tickangle=0,
        title={'text': titulo,'x': 0.5,'xanchor': 'center'})
    
    fig_bar.update_traces(textposition='outside')  
    
    st.plotly_chart(fig_bar,use_container_width=True)

def criar_graficos_pizza(df_agrupado,tipo_df,x,y):
    if tipo_df=="Receitas":
        titulo="Receitas por Categoria"
    else:
        titulo="Despesas por Categoria"
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

