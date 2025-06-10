import pandas as pd
import streamlit as st

def agrupar_por_categoria(df,coluna_agrupada,coluna_valor,agrupar_outros):
    df_agrupado = (
        df.groupby(coluna_agrupada)[coluna_valor]
        .sum()
        .reset_index()
        .sort_values(by=coluna_valor, ascending=False) 
    )

    if agrupar_outros and len(df_agrupado) > 7:
        top7 = df_agrupado.iloc[:7]
        outros_data = {
            coluna_agrupada: "Outros",
            coluna_valor: df_agrupado.iloc[7:][coluna_valor].sum()
        }
        df_com_outros=pd.DataFrame([outros_data])
        df_final=pd.concat([top7, df_com_outros], ignore_index=True)
    else:
        df_final = df_agrupado.iloc[:7]
        
    return df_final

def get_top_n_categorias(df,coluna_agrupada,n):
    return df[coluna_agrupada].head(n).tolist()

def gerar_dataframe_comparativo(df,df_anterior,coluna_agrupada,coluna_valor):
    df_comparacao = pd.merge(
        df,
        df_anterior,
        on=coluna_agrupada,
        suffixes=('_atual', '_anterior'),
        how='inner'  # Apenas centros presentes nos dois períodos
    )
    if df_comparacao.empty:
        return None,None,df_comparacao
    
    df_comparacao["Diferença"]=df_comparacao[f"{coluna_valor}_atual"] - df_comparacao[f"{coluna_valor}_anterior"]
    df_comparacao=df_comparacao.sort_values(by="Diferença",ascending=False)
    maior_aumento=df_comparacao.iloc[0]
    percentual_aumento=(maior_aumento["Diferença"] / maior_aumento[f"{coluna_valor}_anterior"]) * 100
    return maior_aumento,percentual_aumento,df_comparacao
     

def agrupar_por_produto(df,coluna_produto,coluna_quantidade,coluna_valor,tipo_df):
    df_agrupado = (
        df.groupby(coluna_produto).agg(
        Quantidade=(coluna_quantidade,"sum"),
        Valor=(coluna_valor,"sum")
        )
        .reset_index()
        .sort_values(by='Valor', ascending=False)
    )
    if tipo_df is None:
        return df_agrupado
    if tipo_df == "Decadência":
        top1=df_agrupado["Produto"].iloc[-1]
        top3=df_agrupado["Produto"].iloc[::-1].head(3).tolist()
    else:
        top1=df_agrupado["Produto"].iloc[0]
        top3=df_agrupado["Produto"].head(3).tolist()
    return df_agrupado,top1,top3

def produtos_sem_vendas(df_receitas_filtrado,df_catalogo_produtos):
    df_receitas_filtrado["Produto"] = df_receitas_filtrado["Produto"].str.strip().str.lower()
    df_catalogo_produtos = df_catalogo_produtos.loc[df_catalogo_produtos["Produto"]!="Produto"]
    df_catalogo_produtos["Produto"] = df_catalogo_produtos["Produto"].str.strip().str.lower()

    df_concatenado=df_catalogo_produtos.merge(
        df_receitas_filtrado,
        on="Produto",
        how="left",
        indicator=True
    )
    return df_concatenado.loc[df_concatenado["_merge"]=="left_only","Produto"]

def produto_com_maior_variacao(df_receitas_por_produto,df_receitas_por_produto_anterior,tipo_df_concatenado):

    df_receitas_por_produto["Produto"] = df_receitas_por_produto["Produto"].str.strip().str.lower()
    df_receitas_por_produto_anterior["Produto"] = df_receitas_por_produto_anterior["Produto"].str.strip().str.lower()

    df_concatenado = df_receitas_por_produto[["Produto","Valor"]].merge(
        df_receitas_por_produto_anterior[["Produto","Valor"]],
        on="Produto",
        how="inner", 
        suffixes=("_atual", "_anterior")  
    )
    df_concatenado["Diferença"]=df_concatenado["Valor_atual"] - df_concatenado["Valor_anterior"]
    df_concatenado["Percentual_Diferença"]=df_concatenado["Diferença"] / df_concatenado["Valor_anterior"] * 100

    if tipo_df_concatenado == "Decadência":
        filtro = df_concatenado["Diferença"] < 0
    else:
        filtro = df_concatenado["Diferença"] > 0
    df_filtrado = df_concatenado[filtro].copy()
    df_filtrado[["Diferença", "Percentual_Diferença"]] = df_filtrado[["Diferença", "Percentual_Diferença"]].abs()
    df_filtrado = df_filtrado.sort_values(by="Diferença", ascending=False)
    top1 = df_filtrado.iloc[0]
    diferenca = top1["Diferença"]
    percentual_diferenca = top1["Percentual_Diferença"]

    demais_produtos = df_filtrado.iloc[1:11][["Produto", "Diferença", "Percentual_Diferença"]]

    return top1, diferenca, percentual_diferenca, demais_produtos



