import streamlit as st
import plotly.express as px
import pandas as pd

def exibir_abas(filial):
    # Título centralizado
    st.markdown(
        f"""
        <h3 style='text-align: center; margin-top: 0; margin-bottom: 0;'>
            Distribuição de Receita e Despesas | {filial}
        </h3>
        """,
        unsafe_allow_html=True
    )

    # Toggle alinhado à direita mas discreto
    col1, col2, col3 = st.columns([8, 1, 1])
    with col3:
        modo_percentual = st.toggle("📊 %", help="Mostrar proporção percentual")

    if modo_percentual:
        tipo_visualizacao = "Proporção percentual"
        agrupar_outros = True
    else:
        tipo_visualizacao = "Valores absolutos"
        agrupar_outros = False

    return tipo_visualizacao, agrupar_outros


# 🔥 Gerar um gráfico de exemplo
df = pd.DataFrame({
    "Categoria": ["A", "B", "C", "D"],
    "Valor": [100, 200, 150, 80]
})
fig = px.pie(df, names="Categoria", values="Valor", title="")

# 🚀 Função para centralizar o gráfico
def plotar_grafico_centralizado(figura):
    col1, col2, col3 = st.columns([1, 4, 1])
    with col2:
        st.plotly_chart(figura, use_container_width=True)

# 💼 Chamando tudo
filial = "Aldeota"
tipo_visualizacao, agrupar_outros = exibir_abas(filial)

# 🎨 Mostrar os gráficos centralizados
plotar_grafico_centralizado(fig)
plotar_grafico_centralizado(fig)  # outro gráfico se quiser