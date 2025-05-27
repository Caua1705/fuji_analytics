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

def formatar_coluna_valor(df,coluna_valor):
    df[coluna_valor] = pd.to_numeric(df[coluna_valor], errors="coerce").abs().fillna(0)
    return df

def padronizar_valores(df,coluna_alterada,substituicoes):
    df[coluna_alterada]=df[coluna_alterada].replace(substituicoes)
    return df

def formatar_dataframe(df,colunas_nulas,colunas_data,coluna_valor,coluna_alterada,substituicoes):
    df= padronizar_valores(df,coluna_alterada,substituicoes)
    df = formatar_valores_nulos(df,colunas_nulas)
    df = formatar_coluna_valor(df,coluna_valor)
    df = formatar_data(df,colunas_data)
    return df

