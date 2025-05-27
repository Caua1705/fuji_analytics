def filtrar_por_filial(df):
    df_aldeota=df.loc[df["Filial"]=="Aldeota"]
    df_cambeba=df.loc[df["Filial"]=="Cambeba"]
    return {"Aldeota":df_aldeota,
            "Cambeba":df_cambeba}

def filtrar_por_data(df,coluna_data,data_inicial,data_final):
    df_filtrado=df.loc[(df[coluna_data]>=data_inicial) & 
                       (df[coluna_data]<=data_final)]
    return df_filtrado

def processar_filial(dict_receitas,dict_despesas,df_receitas,df_despesas,filial,data_inicio,data_fim):
    if filial=="Todas":
        df_receitas_filtrado=filtrar_por_data(df_receitas,"Data",data_inicio,data_fim)
        df_despesas_filtrado=filtrar_por_data(df_despesas,"Data_Pagamento",data_inicio,data_fim)
    else:
        df_receitas_filtrado=filtrar_por_data(dict_receitas[filial],"Data",data_inicio,data_fim)
        df_despesas_filtrado=filtrar_por_data(dict_despesas[filial],"Data_Pagamento",data_inicio,data_fim)
    return df_receitas_filtrado,df_despesas_filtrado