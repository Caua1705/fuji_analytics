import pandas as pd
import streamlit as st

def agrupar_receitas_por_categoria(df,coluna_agrupada,coluna_valor,coluna_quantidade,agrupar_outros):
    df_agrupado = (
        df.groupby(coluna_agrupada).agg(
        Quantidade_total=(coluna_quantidade,"sum"),
        Valor_Total=(coluna_valor,"sum")
        )
        .reset_index()
        .sort_values(by='Valor_Total', ascending=False)
    )
    if agrupar_outros and len(df_agrupado) > 7:
        top7 = df_agrupado.iloc[:7]
        outros_valor = df_agrupado.iloc[7:]["Valor_Total"].sum()
        outros_quantidade = df_agrupado.iloc[7:]["Quantidade_total"].sum()
        df_com_outros = pd.DataFrame([{coluna_agrupada: "Outros",
                                        "Valor_Total": outros_valor,
                                        "Quantidade_total":outros_quantidade}])
        df_final= pd.concat([top7, df_com_outros], ignore_index=True)
    else:
       df_final=df_agrupado
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

