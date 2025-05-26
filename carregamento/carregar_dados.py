import pandas as pd
from pathlib import Path

dir_raiz=Path(__file__).parents[1]

def carregar_dataframes():
    df_receitas=pd.read_excel(dir_raiz / "data" / "receitas.xlsx")
    df_despesas = pd.read_excel(dir_raiz / "data" / "despesas.xlsx")
    return df_receitas,df_despesas