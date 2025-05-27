import streamlit as st
import pandas as pd
def agrupar_por_filial(df):
    df_aldeota=df.loc[df["Filial"]=="Aldeota"]
    df_cambeba=df.loc[df["Filial"]=="Cambeba"]
    return {"Aldeota":df_aldeota,
            "Cambeba":df_cambeba}

def receitas_por_categoria(df_receitas,agrupar_outros):

    df_receitas["Grupo"]=df_receitas["Grupo"].replace({"COUVERT ARTISTICO":"COUVERT"})

    df_receitas_por_categoria=df_receitas.groupby("Grupo")["Valor"].sum().sort_values(ascending=False).reset_index()

    if agrupar_outros and len(df_receitas_por_categoria) > 7:
        top7 = df_receitas_por_categoria.iloc[:7]
        outros_valor = df_receitas_por_categoria.iloc[7:]["Valor"].sum()
        outros = pd.DataFrame([{"Grupo": "Outros", "Valor": outros_valor}])
        df_receitas_por_categoria = pd.concat([top7, outros], ignore_index=True)
    return df_receitas_por_categoria

def despesas_por_categoria(df_despesas,agrupar_outros):
    df_despesas["Centro_Custo"] = df_despesas["Centro_Custo"].replace({
        "DESPESAS FIXAS": "FIXAS",
        "DESPESAS VARIÁVEIS": "VARIÁVEIS",
        "DESPESA COM PESSOAL": "PESSOAL",
        "LVP SERVIÇOS  ADMINISTRATIVOS LTDA":"LVP",
        "PUBLICIDADE E PROPAGANDA":"PUBLICIDADE"})
    
    df_despesas_por_categoria = (df_despesas.groupby("Centro_Custo")["Valor_Pago/Recebido"].sum().sort_values(ascending=False).reset_index())
    
    if agrupar_outros and len(df_despesas_por_categoria) > 7:
        top7 = df_despesas_por_categoria.iloc[:7]
        outros_valor = df_despesas_por_categoria.iloc[7:]["Valor_Pago/Recebido"].sum()
        outros = pd.DataFrame([{"Centro_Custo": "Outros", "Valor_Pago/Recebido": outros_valor}])
        df_despesas_por_categoria = pd.concat([top7, outros], ignore_index=True)
    
    return df_despesas_por_categoria

    