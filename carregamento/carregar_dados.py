import pandas as pd
from utils.config_formatacao import MAPA_BEBIDA,MAPA_COMIDA,MAPA_OUTROS

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

def formatar_colunas_valores(df, colunas_valores):
    if isinstance(colunas_valores, str):
        colunas_valores = [colunas_valores]
    for coluna in colunas_valores:
        df[coluna] = (
            df[coluna]
            .astype(str)
            .str.replace(",", ".", regex=False)
            .str.replace(" ", "", regex=False)  # remove espaços, se tiver
        )
        df[coluna] = pd.to_numeric(df[coluna], errors="coerce").abs().fillna(0)
    return df

def formatar_quantidade(df_receitas,coluna_quantidade):
    coluna_quantidade=[coluna_quantidade]
    for coluna in coluna_quantidade:
        serie_temporaria = df_receitas[coluna].astype(str).str.replace('.', '', regex=False).str.replace(',', '.')
        df_receitas[coluna] = pd.to_numeric(serie_temporaria, errors='coerce').abs().fillna(0).astype(int)
    return df_receitas

def padronizar_valores(df,coluna_alterada,substituicoes):
    df[coluna_alterada]=df[coluna_alterada].str.strip()
    df[coluna_alterada]=df[coluna_alterada].replace(substituicoes)
    return df

def classificar_produto(df_receitas,coluna_categoria):

    def definir_tipo_produto(valor):
        if valor in MAPA_BEBIDA:
            return "Bebidas"
        elif valor in MAPA_COMIDA:
            return "Comidas"
        elif valor in MAPA_OUTROS:
            return "Outros"
        else:
            return "Outros"

    df_receitas["Tipo_produto"]=df_receitas[coluna_categoria].apply(definir_tipo_produto)
    return df_receitas

def formatar_dataframe(df,substituicoes_colunas,colunas_nulas,colunas_data,colunas_valores,coluna_alterada,substituicoes_valores):
    if substituicoes_colunas:
        df = df.rename(columns=substituicoes_colunas)
    filial_substituicoes = {
            "FUJI ALDEOTA": "Aldeota",
            "FUJI CAMBEBA": "Cambeba"
        }
    df['Filial'] = df['Filial'].replace(filial_substituicoes)
    df= padronizar_valores(df,coluna_alterada,substituicoes_valores)
    df = formatar_valores_nulos(df,colunas_nulas)
    df = formatar_colunas_valores(df,colunas_valores)
    df = formatar_data(df,colunas_data)
    return df

def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def formatar_porcentagem(valor):
    return f"{valor:.2f}%"

def formatar_unidade(valor):
    if valor < 100:
        return f"{valor:02d}"
    else:
        return f"{valor:,}".replace(",", ".")

def formatar_datas_sidebar(data_incial,data_final):
    data_inicio_formatada = data_incial.strftime("%d-%m")
    data_fim_formatada = data_final.strftime("%d-%m")
    return data_inicio_formatada,data_fim_formatada

import pandas as pd
import streamlit as st
from pathlib import Path
from utils.config_formatacao import config_receitas, config_despesas
from utils.formatadores import formatar_dataframe,formatar_quantidade,classificar_produto

dir_raiz=Path(__file__).parents[1]

@st.cache_data

def carregar_e_preparar_dados():
    df_receitas=pd.read_excel(dir_raiz / "data" / "receitas.xlsx")
    df_despesas = pd.read_excel(dir_raiz / "data" / "despesas.xlsx")
    df_catalogo = pd.read_excel(dir_raiz / "data" / "catalogo_produtos.xlsx")
    df_receitas = formatar_dataframe(df_receitas, **config_receitas)
    df_receitas = formatar_quantidade(df_receitas,"Quantidade")
    df_receitas = classificar_produto(df_receitas,"Grupo")
    df_despesas = formatar_dataframe(df_despesas, **config_despesas)
    return df_receitas,df_despesas,df_catalogo