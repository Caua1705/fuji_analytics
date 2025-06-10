def classificar_periodo(diferenca_dias):
    if diferenca_dias==1:
        return "dia"
    elif 2<= diferenca_dias <=14:
        return "curto"
    else:
        return "longo"
    
