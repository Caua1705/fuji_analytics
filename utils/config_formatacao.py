config_receitas = {
    "substituicoes_colunas": {},
    "colunas_nulas": ["Produto", "Grupo", "Quantidade", "Valor", "Filial"],
    "colunas_data": "Data",
    "colunas_valores": "Valor",
    "coluna_alterada": "Grupo",
    "substituicoes_valores": {
        "COUVERT ARTISTICO": "COUVERT"
    },
}

config_despesas={
    "substituicoes_colunas": {
        "Valor_Pago/Recebido": "Valor Pago"
    },
    "colunas_nulas": [
        "Filial","Tipo_Lancamento",
        "Sintetica","Analitica",
        "Detalhada","Observacao","Fornecedor/Cliente",
        "Conta","Forma_Pag/Rec","Valor_Original",
        "Valor Pago","Status"
        ],
    "colunas_data": [
        "Data_Lancamento",
        "Data_Competencia",
        "Data_Vencimento",
        "Data_Pagamento"
        ],
    "colunas_valores": "Valor Pago",
    "coluna_alterada": "Centro_Custo",
    "substituicoes_valores": {
        "DESPESAS FIXAS": "FIXAS",
        "DESPESAS VARIÁVEIS": "VARIÁVEIS",
        "DESPESAS VARIÃVEIS": "VARIÁVEIS",
        "PRODUÃ‡ÃƒO": "PRODUÇÃO",
        "DESPESA COM PESSOAL": "PESSOAL",
        "LVP SERVIÃ‡OS  ADMINISTRATIVOS LTDA": "LVP",
        "LVP SERVIÇOS  ADMINISTRATIVOS LTDA": "LVP",
        "PUBLICIDADE E PROPAGANDA": "PUBLICIDADE"
        }
}
    

MAPA_COMIDA = [
    'COMBINADOS', 'TEMAKI', 'ESPECIAIS', 'PASTE', 'TRUFADOS', 'HOT', 'SASHIMI',
    'FRUTAS', 'ENTRADAS SUSHI', 'MAKIMONO', 'DEL MARE', 'VERDURAS E LEGUMES',
    'LA CARNE', 'SOBREMESA FUJI', 'NIGUIRI', 'COZINHA FUJI', 'RISOTTI',
    'ENTRADAS ITA', 'PREMIUM', 'SOBREMESA ITA', 'SUSHI DESIGN', 'URAMAKI'
]

MAPA_BEBIDA = [
    'DRINKS', 'SUCOS E AGUA DE COCO', 'BEBIDAS GELADAS', 'BRANCOS', 'CERVEJAS',
    'TACAS', 'TINTOS', 'DESTILADOS', 'VINHOS E ESPUMANTES', 'ROSE', 'CAFES',
    'BORBULHAS'
]

MAPA_OUTROS = [
    'COUVERT', 'EMBALAGENS'
] 