import streamlit as st
import pandas as pd
from utils.dados_em_sessao import obter_dados
from processamento.filtrar import filtrar_por_filial,processar_filial
from datetime import timedelta

st.markdown("### 📅 Desempenho Diário")

df_receitas,df_despesas,_=obter_dados()

# Filtrar por Filial
dict_receitas = filtrar_por_filial(df_receitas)
dict_despesas = filtrar_por_filial(df_despesas)

# Filtrar Filial por Data

col1,col2=st.columns(2)
with col1:
    filial = st.selectbox("Selecione a filial", ["Todas", "Aldeota", "Cambeba"])
with col2:
    data_selecionada = st.date_input("Selecione a data para análise diária", value=pd.to_datetime("today"),format="DD/MM/YYYY")

df_receitas_filtrado,df_despesas_filtrado,df_receitas_anterior,df_despesas_filtrado_anterior = processar_filial(
    dict_receitas,
    dict_despesas,
    filial,
    data_selecionada,
    data_selecionada
)

#Total Receitas do dia
receita_dia = df_receitas_filtrado["Valor"].sum()

#Primeiro dia mês atual
primeior_dia_mes_selecionado=data_selecionada.replace(day=1)

#Dias mês anterior
ultimo_dia_mes_anterior=primeior_dia_mes_selecionado- timedelta(days=1)
primeiro_dia_mes_anterior = ultimo_dia_mes_anterior.replace(day=1)
total_dias_mes_anterior=ultimo_dia_mes_anterior.day

#Dias 2 meses atrás
ultimo_dia_dois_meses_atras = primeiro_dia_mes_anterior - timedelta(days=1)
primeiro_dia_dois_meses_atras = ultimo_dia_dois_meses_atras.replace(day=1)
total_dias_2_meses_atras=ultimo_dia_dois_meses_atras.day

total_dias=total_dias_mes_anterior+total_dias_2_meses_atras

#Total despesas do mês anterior
df_meses_anteriores=dict_despesas[filial].loc[(dict_despesas[filial]["Data_Pagamento"].dt.date>=primeiro_dia_dois_meses_atras) &
                                                     (dict_despesas[filial]["Data_Pagamento"].dt.date<=ultimo_dia_mes_anterior)]

despesa_total_meses_anteriores=df_meses_anteriores["Valor_Pago"].sum()

#Despesa média diária dos últimos 2 meses
despesa_media_diaria_mes_anterior=despesa_total_meses_anteriores / total_dias


col1, col2 = st.columns(2)

with col1:
    st.metric(label="Receita do Dia", value=f"R$ {receita_dia:,.2f}")
with col2:
    st.metric(label="Média Diária de Despesas (Últimos 2 Meses)", value=f"R$ {despesa_media_diaria_mes_anterior:,.2f}")

st.markdown("---")

if receita_dia >= despesa_media_diaria_mes_anterior:
    st.success(f"✅ O dia {data_selecionada.strftime('%d/%m/%Y')} se pagou com sobra de **R$ {receita_dia - despesa_media_diaria_mes_anterior:,.2f}**.")
else:
    st.error(f"❌ O dia {data_selecionada.strftime('%d/%m/%Y')} NÃO se pagou. Faltaram **R$ {despesa_media_diaria_mes_anterior - receita_dia:,.2f}**.")