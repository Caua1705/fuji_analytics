import pandas as pd
import streamlit as st

def agrupar_receitas_por_categoria(df,coluna_agrupada,coluna_valor,coluna_quantidade,agrupar_outros):
    df_agrupado = (
        df.groupby(coluna_agrupada).agg(
        Quantidade=(coluna_quantidade,"sum"),
        Valor=(coluna_valor,"sum")
        )
        .reset_index()
        .sort_values(by='Valor', ascending=False)
    )
    if agrupar_outros and len(df_agrupado) > 7:
        top7 = df_agrupado.iloc[:7]
        outros_valor = df_agrupado.iloc[7:]["Valor"].sum()
        outros_quantidade = df_agrupado.iloc[7:]["Quantidade"].sum()
        df_com_outros = pd.DataFrame([{coluna_agrupada: "Outros",
                                        "Valor": outros_valor,
                                        "Quantidade":outros_quantidade}])
        df_final= pd.concat([top7, df_com_outros], ignore_index=True)
    else:
       df_final=df_agrupado.iloc[:7]
    return df_final

def agrupar_despesas_por_categoria(df, coluna_agrupada, coluna_valor, agrupar_outros):
    df_agrupado = (
        df.groupby(coluna_agrupada)[coluna_valor].
        sum()
        .reset_index()
        .sort_values(by=coluna_valor, ascending=False) 
    )

    if agrupar_outros and len(df_agrupado) > 7:
        top7_df = df_agrupado.iloc[:7]
        outros_valor = df_agrupado.iloc[7:][coluna_valor].sum()
        
        df_com_outros = pd.DataFrame([{
            coluna_agrupada: "Outros",
            coluna_valor: outros_valor
        }])
        
        df_final = pd.concat([top7_df, df_com_outros], ignore_index=True)
    else:
        df_final = df_agrupado
        
    return df_final

def criar_curva_abc(df_receitas):
    df_agrupado=(
        df_receitas.groupby("Produto").agg(
        Valor_Total=("Valor","sum"),
        Quantidade_Total=("Quantidade","sum")
    )
    .sort_values(by="Valor_Total",ascending=False)
    )
    df_agrupado["Percentual Valor"]= df_agrupado["Valor_Total"] / df_agrupado["Valor_Total"].sum() 
    df_agrupado["Percentual_Acumulado"]= df_agrupado["Percentual Valor"].cumsum()
    df_agrupado=df_agrupado.reset_index()
    return df_agrupado

def agrupar_por_produto(df,coluna_produto,coluna_quantidade,coluna_valor):
    df_agrupado = (
        df.groupby(coluna_produto).agg(
        Quantidade=(coluna_quantidade,"sum"),
        Valor=(coluna_valor,"sum")
        )
        .reset_index()
        .sort_values(by='Valor', ascending=False)
    )
    return df_agrupado