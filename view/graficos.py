import plotly.express as px
from plotly.colors import qualitative
import streamlit as st
                            
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
        showlegend=False,
        xaxis_tickangle=0,
        title={
            'text': titulo,
            'x': 0.0,
            'xanchor': 'left'
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

def criar_grafico_curva_abc(df_receitas_curva_abc):
    fig=px.bar(df_receitas_curva_abc,"Produto","Valor_Total","Produto",title="Curva ABC")
    fig.add_trace(px.line(df_receitas_curva_abc,
                      x='Produto',
                      y='Percentual_Acumulado',
                      line_shape='spline', # Ou 'linear'
                      markers=False
                     ).update_traces(yaxis="y2",
                                     line_color='black', # Cor para a linha acumulada
                                     line_width=2,
                                     name='Percentual Acumulado'
                                     ).data[0])

# Configurar o segundo eixo Y para o percentual acumulado
    fig.update_layout(yaxis=dict(title='Valor Total', side='left', showgrid=False),
                    yaxis2=dict(title='Percentual Acumulado', side='right', overlaying='y', showgrid=False, range=[0,1], tickformat=".0%"),
                    xaxis_title="Produtos (Ordenados por Faturamento)",
                    title_x=0.5,
                    hovermode="x unified",
                    legend_title_text="Categoria ABC"
                    )

    # Adicionar linhas de referência para 80% e 95% no eixo Y secundário
    fig.add_hline(y=0.8, line_dash="dash", line_color="grey", annotation_text="80% (Limite A)", annotation_position="top right", yref="y2")
    fig.add_hline(y=0.95, line_dash="dot", line_color="grey", annotation_text="95% (Limite B)", annotation_position="top right", yref="y2")

    fig.show()

    st.plotly_chart(fig)