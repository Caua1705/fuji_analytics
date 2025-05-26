import pandas as pd

def formatar_data(df,colunas):
    if isinstance(colunas,str):
        colunas=[colunas]
    for coluna in colunas:
        df[coluna]=pd.to_datetime(df[coluna],dayfirst=True,errors='coerce').dt.date
    return df

def formatar_valores_nulos(df,colunas):
    for coluna in colunas:
        df[coluna]=df[coluna].fillna(0)
    return df

def formatar_coluna_valor(df, coluna_valor):
    df[coluna_valor] = pd.to_numeric(df[coluna_valor], errors="coerce").abs().fillna(0)
    return df

