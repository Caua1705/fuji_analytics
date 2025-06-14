from datetime import timedelta
import pandas as pd

def filtrar_por_filial(df):
    df_aldeota=df.loc[df["Filial"]=="Aldeota"]
    df_cambeba=df.loc[df["Filial"]=="Cambeba"]
    return {"Aldeota":df_aldeota,
            "Cambeba":df_cambeba,
            "Todas": df}

def filtrar_por_data(df,coluna_data,data_inicial,data_final):
    
    data_inicial = pd.to_datetime(data_inicial)
    data_final = pd.to_datetime(data_final)
    
    df_filtrado=df.loc[(df[coluna_data]>=data_inicial) & 
                       (df[coluna_data]<=data_final)]
    
    periodo_atual_dias = (data_final - data_inicial).days + 1
    
    data_inicio_anterior = data_inicial - timedelta(days=periodo_atual_dias)
    data_fim_anterior = data_inicial - timedelta(days=1)
    
    df_filtrado_anterior=df.loc[(df[coluna_data]>=data_inicio_anterior) & 
                                (df[coluna_data]<=data_fim_anterior)]
    return df_filtrado,df_filtrado_anterior

def processar_filial(dict_receitas, dict_despesas, filial, data_inicial, data_final):
    df_receitas_filtrado, df_receitas_filtrado_anterior = filtrar_por_data(
        dict_receitas[filial], "Data", data_inicial, data_final
    )
    df_despesas_filtrado, df_despesas_filtrado_anterior = filtrar_por_data(
        dict_despesas[filial], "Data_Pagamento", data_inicial, data_final
    )
    return df_receitas_filtrado, df_despesas_filtrado, df_receitas_filtrado_anterior, df_despesas_filtrado_anterior
