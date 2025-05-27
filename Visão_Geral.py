import streamlit as st
from carregamento.carregar_dados import carregar_dataframes
from utils.formatar import formatar_data, formatar_valores_nulos, formatar_coluna_valor
from processamento.agrupar import agrupar_por_filial, receitas_por_categoria, despesas_por_categoria
from processamento.metricas import exibir_metricas_financeiras
from processamento.graficos import criar_graficos_principais_receitas, criar_graficos_principais_despesas
from utils.filtrar import filtrar_por_data

st.set_page_config(
    page_title="Dashboard Financeiro",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("📊 Visão Geral de Receitas e Despesas")
st.markdown("Bem-vindo(a) ao dashboard financeiro. Aqui você pode analisar receitas e despesas filtrando por filial e período.")

st.markdown("---")

# --- Sidebar: filtros ---
with st.sidebar:
    st.header("Filtros de análise")
    st.markdown("Escolha a filial e o período para visualizar os dados correspondentes.")

    filial = st.selectbox("Selecione a filial", ["Todas", "Aldeota", "Cambeba"])

    st.subheader("Período")
    data_inicio = st.date_input("Data de início")
    data_fim = st.date_input("Data de fim")
    
    st.markdown("---")
    st.caption("Desenvolvido por [Seu Nome]")

# --- Carregar e formatar dados (sem mudança visual) ---
df_receitas, df_despesas = carregar_dataframes()

df_receitas = formatar_valores_nulos(df_receitas, ["Produto", "Grupo", "Quantidade", "Valor", "Filial"])
df_despesas = formatar_valores_nulos(
    df_despesas,
    [
        "Filial", "Tipo_Lancamento", "Sintetica", "Analitica", "Detalhada",
        "Observacao", "Fornecedor/Cliente", "Conta", "Forma_Pag/Rec",
        "Valor_Original", "Valor_Pago/Recebido", "Status"
    ],
)
df_receitas = formatar_coluna_valor(df_receitas, "Valor")
df_despesas = formatar_coluna_valor(df_despesas, "Valor_Pago/Recebido")
df_receitas = formatar_data(df_receitas, "Data")
df_despesas = formatar_data(df_despesas, ["Data_Lancamento", "Data_Competencia", "Data_Vencimento", "Data_Pagamento"])

dict_receitas = agrupar_por_filial(df_receitas)
dict_despesas = agrupar_por_filial(df_despesas)

# --- Aplicar filtros ---
if filial == "Aldeota":
    df_receitas_filtrado = filtrar_por_data(dict_receitas["Aldeota"], "Data", data_inicio, data_fim)
    df_despesas_filtrado = filtrar_por_data(dict_despesas["Aldeota"], "Data_Pagamento", data_inicio, data_fim)
elif filial == "Cambeba":
    df_receitas_filtrado = filtrar_por_data(dict_receitas["Cambeba"], "Data", data_inicio, data_fim)
    df_despesas_filtrado = filtrar_por_data(dict_despesas["Cambeba"], "Data_Pagamento", data_inicio, data_fim)
else:
    df_receitas_filtrado = filtrar_por_data(df_receitas, "Data", data_inicio, data_fim)
    df_despesas_filtrado = filtrar_por_data(df_despesas, "Data_Pagamento", data_inicio, data_fim)

# --- Mostrar métricas ---
st.header("📈 Métricas Financeiras")
st.write("Resumo dos valores filtrados para receitas e despesas.")
exibir_metricas_financeiras(df_receitas_filtrado, df_despesas_filtrado)

st.markdown("---")

# --- Aba para gráficos ---
aba1, aba2 = st.tabs(["Visão Financeira", "Evolução Mensal"])

with aba1:
    st.subheader("Visualização Financeira")
    tipo_visualizacao = st.radio(
        "Selecione o tipo de visualização:",
        ["📊 Valores absolutos", "📉 Proporção percentual"],
        horizontal=True,
    )
    agrupar_outros = tipo_visualizacao == "📉 Proporção percentual"

    # Preparar dados
    match filial:
        case "Aldeota":
            df_receitas_cat = receitas_por_categoria(df_receitas_filtrado, agrupar_outros)
            df_despesas_cat = despesas_por_categoria(df_despesas_filtrado, agrupar_outros)
        case "Cambeba":
            df_receitas_cat = receitas_por_categoria(df_receitas_filtrado, agrupar_outros)
            df_despesas_cat = despesas_por_categoria(df_despesas_filtrado, agrupar_outros)
        case "Todas":
            df_receitas_cat = receitas_por_categoria(df_receitas_filtrado, agrupar_outros)
            df_despesas_cat = despesas_por_categoria(df_despesas_filtrado, agrupar_outros)

    # Exibir gráficos lado a lado
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### Receitas por Categoria")
        criar_graficos_principais_receitas(df_receitas_cat, tipo_visualizacao)
    with col2:
        st.markdown("### Despesas por Categoria")
        criar_graficos_principais_despesas(df_despesas_cat, tipo_visualizacao)

with aba2:
    st.subheader("Evolução Mensal")
    st.info("Aqui você pode incluir gráficos de evolução mensal ou outras análises ao longo do tempo.")