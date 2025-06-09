import plotly.express as px
from plotly.colors import qualitative
import streamlit as st
from processamento.agrupar import agrupar_por_produto

                            
def criar_graficos_barra(df_agrupado, tipo_df, x, y, filial):
    if tipo_df == "Receitas":
        cores =['#D66BA0', '#8B5E3C', '#6BCBDB', '#F5CBA7', '#A9CCE3']
        titulo = f"Distribuição da Receita por Categoria - {filial}"
    else:
        cores = ["#17becf", "#bcbd22", "#e377c2", "#7f7f7f", "#ffbb78", "#aec7e8"]
        titulo = f"Distribuição das Despesas por Centro de Custo - {filial}"

    fig = px.bar(
        df_agrupado,
        x=x,
        y=y,
        text_auto=".2s",
        color=x,
        width=300,
        color_discrete_sequence=cores,
    )

    fig.update_layout(
        xaxis_title=x,
        yaxis_title=y,
        showlegend=True,
        xaxis_tickangle=0,
        title={
            'text': titulo,
            'x': 0.0,
            'xanchor': 'center'
        }
    )

    fig.update_traces(textposition='outside')

    st.plotly_chart(fig, use_container_width=True)

def criar_graficos_pizza(df_agrupado, tipo_df, x, y, filial):
    if tipo_df == "Receitas":
        titulo = f"Distribuição da Receita por Categoria - {filial}"
    else:
        titulo = f"Distribuição das Despesas por Centro de Custo - {filial}"

    fig = px.pie(
        df_agrupado,
        names=x,
        values=y,
        title=titulo,
        hole=0.4,
        color_discrete_sequence=qualitative.Set3,
    )
    fig.update_layout(
        showlegend=True,
        legend=dict(orientation="v", x=1, y=0.5)
    )

    fig.update_traces(textinfo="percent+label")

    st.plotly_chart(fig, use_container_width=True)

def criar_grafico_produtos(df,coluna_produto,coluna_quantidade,coluna_valor,filial):
    df_agrupado=agrupar_por_produto(df,coluna_produto,coluna_quantidade,coluna_valor,tipo_df=None)
    top_10_produtos=df_agrupado.iloc[:9]
    cores =['#D66BA0', '#8B5E3C', '#6BCBDB', '#F5CBA7', '#A9CCE3']
    titulo = f"Distribuição da Receita por Produto - {filial}"
    fig=px.bar(top_10_produtos,
               "Produto",
               "Valor",
               title=titulo,
               color="Produto",
               width=300,
               color_discrete_sequence=cores)
    
    fig.update_layout(
        xaxis_title="Produto",
        yaxis_title="Valor",
        showlegend=True,
        xaxis_tickangle=0,
        title={
            'text': titulo,
            'x': 0.0,
            'xanchor': 'center'
        }
    )

    fig.update_traces(textposition='outside')
    st.plotly_chart(fig,use_container_width=True)