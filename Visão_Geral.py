import streamlit as st
from carregamento.carregar_dados import carregar_dataframes
from utils.formatar import formatar_data,formatar_valores_nulos,formatar_coluna_valor
from processamento.agrupar import agrupar_por_filial,receitas_por_categoria,despesas_por_categoria
from processamento.metricas import exibir_metricas_financeiras
from processamento.graficos import criar_graficos_principais_receitas,criar_graficos_principais_despesas
from utils.filtrar import filtrar_por_data

st.title("Visão Geral de Receitas e Despesas")

#Carregar Dados
df_receitas,df_despesas=carregar_dataframes()

#Formatar dados
df_despesas=df_despesas.rename(columns={"DESPESAS FIXAS":"FIXAS",
                                        "DESPESAS VARIÁVEIS":"VARIÁVEIS",
                                        "DESPESA COM PESSOAL":"PESSOAL",
                                        "LVP SERVIÇOS ADMINISTRATIVOS LTDA": "LVP"})
df_receitas=formatar_valores_nulos(df_receitas,["Produto","Grupo","Quantidade","Valor","Filial"])
df_despesas=formatar_valores_nulos(df_despesas,["Filial","Tipo_Lancamento","Sintetica","Analitica","Detalhada",
                                                "Observacao","Fornecedor/Cliente",
                                                "Conta","Forma_Pag/Rec","Valor_Original",""
                                                "Valor_Pago/Recebido","Status"])
df_receitas=formatar_coluna_valor(df_receitas,"Valor")
df_despesas=formatar_coluna_valor(df_despesas,"Valor_Pago/Recebido")
df_receitas=formatar_data(df_receitas,"Data")
df_despesas=formatar_data(df_despesas,["Data_Lancamento","Data_Competencia","Data_Vencimento","Data_Pagamento"])


#Agrupar por filial:
dict_receitas=agrupar_por_filial(df_receitas)
dict_despesas=agrupar_por_filial(df_despesas)

#Filtros Sidebar
with st.sidebar:
    st.subheader("Filial")
    filial=st.sidebar.selectbox("Selecione a filial",["Todas","Aldeota","Cambeba"])
    st.subheader("📅 Filtros de Período")
    data_inicio = st.date_input("Data de início")
    data_fim = st.date_input("Data de fim")

if filial=="Aldeota":
    df_receitas_aldeota_filtrado=filtrar_por_data(dict_receitas["Aldeota"],"Data",data_inicio,data_fim)
    df_despesas_aldeota_filtrado=filtrar_por_data(dict_despesas["Aldeota"],"Data_Pagamento",data_inicio,data_fim)
    exibir_metricas_financeiras(df_receitas_aldeota_filtrado,df_despesas_aldeota_filtrado)
elif filial=="Cambeba":
    df_receitas_cambeba_filtrado=filtrar_por_data(dict_receitas["Cambeba"],"Data",data_inicio,data_fim)
    df_despesas_cambeba_filtrado=filtrar_por_data(dict_despesas["Cambeba"],"Data_Pagamento",data_inicio,data_fim)
    exibir_metricas_financeiras(df_receitas_cambeba_filtrado,df_despesas_cambeba_filtrado)
elif filial=="Todas":
    df_receitas_todos_filtrado=filtrar_por_data(df_receitas,"Data",data_inicio,data_fim)
    df_despesas_todos_filtrado=filtrar_por_data(df_despesas,"Data_Pagamento",data_inicio,data_fim)
    exibir_metricas_financeiras(df_receitas_todos_filtrado,df_despesas_todos_filtrado)

aba1, aba2 = st.tabs(["Visão Financeira", "Evolução Mensal"])

st.subheader("Análise Comparativa de Receitas e Despesas por Categoria")
tipo_visualizacao = st.radio(
    "",
    ["📊 Valores absolutos", "📉 Proporção percentual"],
    horizontal=True,
    label_visibility="collapsed")

match(filial):

    case "Aldeota":
        df_receitas_por_categoria_aldeota=receitas_por_categoria(df_receitas_aldeota_filtrado)
        df_despesas_por_categoria_aldeota=despesas_por_categoria(df_despesas_aldeota_filtrado)
        st.write(df_receitas_por_categoria_aldeota)

        col1,col2=st.columns(2)
        with col1:
            criar_graficos_principais_receitas(df_receitas_por_categoria_aldeota,tipo_visualizacao)
        with col2:
            criar_graficos_principais_despesas(df_despesas_por_categoria_aldeota,tipo_visualizacao)

    case "Cambeba":
        df_receitas_por_categoria_cambeba=receitas_por_categoria(df_receitas_cambeba_filtrado)
        df_despesas_por_categoria_cambeba=despesas_por_categoria(df_despesas_cambeba_filtrado)

        col1,col2=st.columns(2)
        with col1:
            criar_graficos_principais_receitas(df_receitas_por_categoria_cambeba,tipo_visualizacao)
        with col2:
            criar_graficos_principais_despesas(df_despesas_por_categoria_cambeba,tipo_visualizacao)

    case "Todas":
        df_receitas_por_categoria_todos=receitas_por_categoria(df_receitas_todos_filtrado)
        df_despesas_por_categoria_todos=despesas_por_categoria(df_despesas_todos_filtrado)

        col1,col2=st.columns(2)
        with col1:
            criar_graficos_principais_receitas(df_receitas_por_categoria_todos,tipo_visualizacao)
        with col2:
            criar_graficos_principais_despesas(df_despesas_por_categoria_todos,tipo_visualizacao)

        
       

