import pandas as pd
from pathlib import Path

caminho_arquivo=Path(__file__).parent / "data" / "receitas_atualizado.xlsx"

df=pd.read_excel(caminho_arquivo,sheet_name="Planilha1")

df["Valor"] = df["Valor"].astype(str).str.replace(',', '.').astype(float)

# Calcular a soma
soma = df["Valor"].sum()

print(f"A soma é: {soma}")