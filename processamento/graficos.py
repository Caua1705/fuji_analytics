import streamlit as st
import plotly.express as px

def criar_graficos_principais_receitas(receitas_por_categoria,tipo_visualizacao):
    st.write(receitas_por_categoria)
    fig1=px.bar(receitas_por_categoria,x="Grupo",y="Valor",title="Receitas por Categoria")
    fig1.update_layout(xaxis_title="Grupo",yaxis_title="Valor",showlegend=True)
    fig2=px.pie(receitas_por_categoria,names="Grupo",values="Valor",title="Receitas por Categoria")
    if tipo_visualizacao=="📊 Valores absolutos":
        st.plotly_chart(fig1)
    else:
        st.plotly_chart(fig2)

def criar_graficos_principais_despesas(despesas_por_categoria,tipo_visualizacao):
    fig1=px.bar(despesas_por_categoria,x="Centro_Custo",y="Valor_Pago/Recebido",title="Despesas por Categoria")
    fig2=px.pie(despesas_por_categoria,names="Centro_Custo",values="Valor_Pago/Recebido",title="Despesas por Categoria")
    if tipo_visualizacao=="📊 Valores absolutos":
        st.plotly_chart(fig1)
    else:
        st.plotly_chart(fig2)