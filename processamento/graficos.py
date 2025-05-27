import plotly.express as px
import streamlit as st

def criar_graficos_principais_receitas(receitas_por_categoria, tipo_visualizacao):
    fig1 = px.bar(
        receitas_por_categoria,
        x="Grupo",
        y="Valor",
        title="Receitas por Categoria",
        text_auto=".2s",
        color="Grupo",
    )
    fig1.update_layout(
        xaxis_title="Grupo",
        yaxis_title="Valor",
        showlegend=False,
        xaxis_tickangle=0,
        bargap=0.4)
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
    fig1=px.bar(despesas_por_categoria,
                x="Centro_Custo",
                y="Valor_Pago/Recebido",
                title="Despesas por Categoria",
                text_auto=".2s",
                color="Centro_Custo")
    fig1.update_layout(xaxis_title="Centro_Custo",
                       yaxis_title="Valor_Pago/Recebido",
                       showlegend=False,
                       xaxis_tickangle=0,
                       bargap=0.4)
    fig2=px.pie(despesas_por_categoria,names="Centro_Custo",values="Valor_Pago/Recebido",title="Despesas por Categoria")
    if tipo_visualizacao=="📊 Valores absolutos":
        st.plotly_chart(fig1)
    else:
        st.plotly_chart(fig2)