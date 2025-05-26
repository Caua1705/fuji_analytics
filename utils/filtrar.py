def filtrar_por_data(df,coluna_data,data_inicial,data_final):
    df_filtrado=df.loc[(df[coluna_data]>=data_inicial) & 
                       (df[coluna_data]<=data_final)]
    return df_filtrado