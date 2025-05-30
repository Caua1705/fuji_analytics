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

def formatar_colunas_valores(df,colunas_valores):
    if isinstance(colunas_valores,str):
        colunas_valores=[colunas_valores]
    for coluna in colunas_valores:
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce").abs().fillna(0)
    return df

def padronizar_valores(df,coluna_alterada,substituicoes):
    df[coluna_alterada]=df[coluna_alterada].replace(substituicoes)
    return df

def formatar_dataframe(df,colunas_nulas,colunas_data,colunas_valores,coluna_alterada,substituicoes):
    df= padronizar_valores(df,coluna_alterada,substituicoes)
    df = formatar_valores_nulos(df,colunas_nulas)
    df = formatar_colunas_valores(df,colunas_valores)
    df = formatar_data(df,colunas_data)
    return df

