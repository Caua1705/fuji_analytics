import pandas as pd

def agrupar_por_categoria(df,coluna_agrupada,valor_agrupado,agrupar_outros):
    df_agrupado = (
    df.groupby(coluna_agrupada)[valor_agrupado]
    .sum()
    .sort_values(ascending=False)
    .reset_index()
)
    if agrupar_outros and len(df_agrupado) > 7:
        top7 = df_agrupado.iloc[:7]
        outros_valor = df_agrupado.iloc[7:][valor_agrupado].sum()
        outros = pd.DataFrame([{coluna_agrupada: "Outros", valor_agrupado: outros_valor}])
        df_final= pd.concat([top7, outros], ignore_index=True)
    else:
       df_final=df_agrupado.iloc[:7]
    return df_final

    