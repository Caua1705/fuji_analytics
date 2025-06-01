from datetime import timedelta

def filtrar_por_filial(df):
    df_aldeota=df.loc[df["Filial"]=="Aldeota"]
    df_cambeba=df.loc[df["Filial"]=="Cambeba"]
    return {"Aldeota":df_aldeota,
            "Cambeba":df_cambeba}

def filtrar_por_data(df,coluna_data,data_inicial,data_final):
    df_filtrado=df.loc[(df[coluna_data]>=data_inicial) & 
                       (df[coluna_data]<=data_final)]
    
    periodo_atual_dias = (data_final - data_inicial).days + 1
    
    data_inicio_anterior = data_inicial - timedelta(days=periodo_atual_dias)
    data_fim_anterior = data_inicial - timedelta(days=1)
    
    df_filtrado_anterior=df.loc[(df[coluna_data]>=data_inicio_anterior) & 
                                (df[coluna_data]<=data_fim_anterior)]
    return df_filtrado,df_filtrado_anterior

def processar_filial(dict_receitas,dict_despesas,df_receitas,df_despesas,filial,data_inicial,data_final):
    if filial=="Todas":
        df_receitas_filtrado,df_receitas_filtrado_anterior=filtrar_por_data(df_receitas,"Data",data_inicial,data_final)
        df_despesas_filtrado,df_despesas_filtrado_anterior=filtrar_por_data(df_despesas,"Data_Pagamento",data_inicial,data_final)
    else:
        df_receitas_filtrado,df_receitas_filtrado_anterior=filtrar_por_data(dict_receitas[filial],"Data",data_inicial,data_final)
        df_despesas_filtrado,df_despesas_filtrado_anterior=filtrar_por_data(dict_despesas[filial],"Data_Pagamento",data_inicial,data_final)
    return df_receitas_filtrado,df_despesas_filtrado,df_receitas_filtrado_anterior,df_despesas_filtrado_anterior
