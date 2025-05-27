import streamlit as st
import pandas as pd
def agrupar_por_filial(df):
    df_aldeota=df.loc[df["Filial"]=="Aldeota"]
    df_cambeba=df.loc[df["Filial"]=="Cambeba"]
    return {"Aldeota":df_aldeota,
            "Cambeba":df_cambeba}

def receitas_por_categoria(df_receitas):
    df_receitas_por_categoria=df_receitas.groupby("Grupo")["Valor"].sum().sort_values(ascending=False).reset_index()
    if len(df_receitas_por_categoria) > 7:
        top5 = df_receitas_por_categoria.iloc[:7]
        outros_valor = df_receitas_por_categoria.iloc[7:]["Valor"].sum()
        outros = pd.DataFrame([{"Grupo": "Outros", "Valor": outros_valor}])
        df_receitas_por_categoria = pd.concat([top5, outros], ignore_index=True)
    return df_receitas_por_categoria

def despesas_por_categoria(df_despesas):
    df_despesas["Centro_Custo"] = df_despesas["Centro_Custo"].replace({
        "DESPESAS FIXAS": "FIXAS",
        "DESPESAS VARIÁVEIS": "VARIÁVEIS",
        "DESPESA COM PESSOAL": "PESSOAL",
        "LVP SERVIÇOS  ADMINISTRATIVOS LTDA":"LVP"})
    df_despesas_por_categoria=df_despesas.groupby("Centro_Custo")["Valor_Pago/Recebido"].sum().sort_values(ascending=False).reset_index()
    if len(df_despesas_por_categoria)>7:
        top5=df_despesas_por_categoria.iloc[:7]
        outros=df_despesas_por_categoria.iloc[7:].sum()
        top5.loc["Outros"]=outros
        return top5
    return df_despesas_por_categoria

    