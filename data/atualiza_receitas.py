import pandas as pd
from pathlib import Path

# Caminho absoluto da pasta onde o script está
pasta_principal = Path(__file__).parent.resolve()

# Pastas com os arquivos .csv
pastas = ['Aldeota', 'Cambeba']
arquivo_receitas = pasta_principal / 'receitas.xlsx'

# Novo arquivo atualizado
arquivo_atualizado = pasta_principal / 'receitas_atualizado.xlsx'

# Lista para armazenar todos os DataFrames encontrados
todos_df = []

# Loop nas pastas
for filial in pastas:
    caminho = pasta_principal / filial
    print(f"\n🔍 Procurando arquivos em: {caminho}")

    if not caminho.exists():
        print(f"❌ Pasta não encontrada: {caminho}")
        continue

    arquivos_csv = list(caminho.glob('*.csv'))  # Somente arquivos .csv

    print(f"🗂️ Arquivos encontrados na pasta {filial}: {[a.name for a in arquivos_csv]}")

    for arquivo in arquivos_csv:
        data_str = arquivo.stem  # usa o nome do arquivo sem extensão

        try:
            dia, mes = data_str.split('-')
            data_formatada = f'{dia.zfill(2)}/{mes.zfill(2)}/2025'
        except Exception as e:
            print(f"⚠️ Nome de arquivo inválido ({arquivo.name}), pulando.")
            continue

        try:
            df = pd.read_csv(arquivo, encoding='utf-8', sep=';')  # ajuste encoding e separador se necessário
        except Exception as e:
            print(f"⚠️ Erro ao ler {arquivo.name}: {e}")
            continue

        # Limpa e padroniza os nomes das colunas
        df.columns = df.columns.str.strip().str.replace('\n', '').str.replace('  ', ' ')

        colunas_necessarias = {'Produto', 'Grupo', 'Quantidade', 'Valor'}
        if not colunas_necessarias.issubset(df.columns):
            print(f"⚠️ Arquivo {arquivo.name} ignorado: colunas obrigatórias ausentes.")
            print(f"   ➤ Colunas encontradas: {list(df.columns)}")
            continue

        # Adiciona colunas fixas
        df['Data'] = data_formatada
        df['Filial'] = filial

        # Chave única para controle interno (não será salva)
        df['Chave'] = (
            df['Data'].astype(str) + '|' +
            df['Filial'].astype(str) + '|' +
            df['Produto'].astype(str) + '|' +
            df['Grupo'].astype(str) + '|' +
            df['Quantidade'].astype(str) + '|' +
            df['Valor'].astype(str)
        )

        todos_df.append(df)

# Verificação final
if not todos_df:
    print("⚠️ Nenhum dado novo encontrado. Verifique os arquivos nas pastas.")
    print("⛔ Arquivo não será criado pois não há dados novos.")
    exit()

# Junta tudo
df_novos = pd.concat(todos_df, ignore_index=True)
print("\n✅ Arquivos novos unidos com sucesso!")

# Carrega o arquivo principal, se existir
try:
    df_principal = pd.read_excel(arquivo_receitas)
    print("✅ Arquivo principal receitas.xlsx carregado.")

    if 'Chave' not in df_principal.columns:
        if 'Grupo' not in df_principal.columns:
            df_principal['Grupo'] = ''
        df_principal['Chave'] = (
            df_principal['Data'].astype(str) + '|' +
            df_principal['Filial'].astype(str) + '|' +
            df_principal['Produto'].astype(str) + '|' +
            df_principal['Grupo'].astype(str) + '|' +
            df_principal['Quantidade'].astype(str) + '|' +
            df_principal['Valor'].astype(str)
        )
except FileNotFoundError:
    print(f"❌ Arquivo receitas.xlsx não encontrado. Será criado novo.")
    df_principal = pd.DataFrame()

# Combina tudo e remove duplicatas
df_final = pd.concat([df_principal, df_novos], ignore_index=True)
df_final = df_final.drop_duplicates(subset=['Chave'])

# Remove a coluna 'Chave' antes de salvar
df_final = df_final.drop(columns=['Chave'])

# Salva no arquivo Excel atualizado
df_final.to_excel(arquivo_atualizado, index=False)
print("💾 Dados atualizados no arquivo receitas_atualizado.xlsx com sucesso, sem duplicatas!")