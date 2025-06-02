import streamlit as st
# Carregar Dados
from carregamento.carregar_dados import carregar_dataframes
# Formatar Dados
from utils.formatadores import formatar_dataframe,formatar_quantidade
from utils.config_formatacao import config_receitas, config_despesas
from utils.estilo import aplicar_estilo_pagina,inserir_logo,linha_divisoria
# Filtrar Dados
from processamento.filtrar import filtrar_por_filial, processar_filial
#Exibir Sidebar:
from view.sidebar import exibir_sidebar
# Exibir Métricas
from view.metricas import exibir_metricas_financeiras
# Agrupar Dados
from processamento.agrupar import agrupar_receitas_por_categoria,agrupar_despesas_por_categoria
# Exibir Gráficos
from view.graficos import criar_graficos_barra,criar_graficos_pizza
from view.insights import insight_receitas,insight_despesas

# Configuração da Página
st.set_page_config(layout="wide")
aplicar_estilo_pagina()

# Logo Fixa
inserir_logo("https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png", 100)

# Título
# --- HTML e CSS para a barra superior personalizada ---
# Esta barra vai conter a logo (ou nome simplificado) e os botões de exportação.
# Ela usará position: fixed para ficar no topo.
top_bar_html = """
<style>
    /* Estilos para o elemento HTML body */
    html, body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        font-family: Arial, sans-serif;
        background-color: #f4f7fa; /* Cor de fundo geral da página */
    }

    /* Estilos para a barra superior (logo e botões de exportação) */
    .custom-top-bar {
        position: fixed;
        top: 0;
        left: 0;
        width: 100%;
        background-color: #ffffff; /* Fundo branco */
        padding: 10px 20px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        display: flex;
        justify-content: space-between; /* Alinha logo à esquerda e botões à direita */
        align-items: center;
        z-index: 9999; /* Garante que fique no topo */
        box-sizing: border-box;
    }

    /* Logo/Nome "Fuji" na barra superior */
    .top-bar-fuji {
        font-size: 1.5em; /* Tamanho do texto "Fuji" */
        font-weight: bold;
        color: #333;
        display: flex;
        align-items: center;
        gap: 8px; /* Espaço entre logo e texto */
    }
    .top-bar-fuji img {
        height: 30px; /* Altura da pequena logo Fuji */
    }


    /* Botões de exportação na barra superior */
    .export-buttons-container {
        display: flex;
        gap: 10px; /* Espaço entre os botões */
        align-items: center;
    }
    .export-button {
        background-color: #007bff; /* Azul para o botão principal */
        color: white;
        padding: 8px 15px;
        border: none;
        border-radius: 5px;
        cursor: pointer;
        font-size: 0.9em;
        display: flex;
        align-items: center;
        gap: 5px;
        transition: background-color 0.2s ease-in-out;
    }
    .export-button:hover {
        background-color: #0056b3;
    }
    .export-format-text {
        font-size: 0.8em;
        color: #666;
        margin-left: 5px;
        line-height: 1; /* Garante que não crie espaço extra */
        display: flex;
        flex-direction: column;
        align-items: flex-end; /* Alinha PDF/Excel à direita */
    }
    .export-format-text span {
        margin: 0;
        padding: 0;
    }

    /* Estilos para o título principal do dashboard (abaixo da barra superior) */
    .main-dashboard-title {
        text-align: center;
        font-size: 1.8em; /* Tamanho maior para o título principal */
        font-weight: bold;
        color: #333;
        margin-top: 15px; /* Espaço entre a barra superior e este título */
        margin-bottom: 20px; /* Espaço abaixo do título */
    }

    /* Ajuste para o conteúdo principal do Streamlit para não ser coberto */
    .st-emotion-cache-1jm6gvw { /* Ou a classe correta do seu contêiner */
        padding-top: 70px !important; /* Altura da barra superior + um pouco mais */
    }
    .main { /* Classe alternativa */
        padding-top: 70px !important;
    }
    .stApp > header { /* Para remover o header padrão do Streamlit, se interferir */
        z-index: 0 !important;
        height: 0 !important;
        visibility: hidden !important;
    }
</style>

<div class="custom-top-bar">
    <div class="top-bar-fuji">
        <img src="https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png" alt="Fuji Logo">
        Fuji
    </div>
    <div class="export-buttons-container">
        <button class="export-button">
            <i class="fas fa-file-export"></i> Exportar Relatório
        </button>
        <div class="export-format-text">
            <span>PDF</span>
            <span>Excel</span>
        </div>
    </div>
</div>
"""

# Injetar o HTML/CSS da barra superior
st.markdown(top_bar_html, unsafe_allow_html=True)
# Sidebar 
data_inicio,data_fim,filial=exibir_sidebar()

# Carregar Dados
df_receitas, df_despesas = carregar_dataframes()


# Formatar Dados
df_receitas = formatar_dataframe(df_receitas, **config_receitas)
df_receitas = formatar_quantidade(df_receitas,"Quantidade")
df_despesas = formatar_dataframe(df_despesas, **config_despesas)

# Filtrar por Filial
dict_receitas = filtrar_por_filial(df_receitas)
dict_despesas = filtrar_por_filial(df_despesas)

# Filtrar por Data
df_receitas_filtrado,df_despesas_filtrado,df_receitas_filtrado_anterior,df_despesas_filtrado_anterior = processar_filial(
    dict_receitas,
    dict_despesas,
    filial,
    data_inicio,
    data_fim
)

#Verifica se há Dados
if df_receitas_filtrado.empty or df_despesas_filtrado.empty:
    st.warning("⚠️ **Aviso:** Nenhum dado disponível para o período selecionado. Verifique os parâmetros e refaça a consulta.")
    st.stop()

#Métricas Financeiras
exibir_metricas_financeiras(df_receitas_filtrado, df_despesas_filtrado)
linha_divisoria()

modo_percentual = st.toggle("📊 Mostrar em proporção (%)", value=False)
if modo_percentual:
    agrupar_outros=True
else:
    agrupar_outros=False

# Agrupar por Categoria
df_receitas_por_categoria = agrupar_receitas_por_categoria(df_receitas_filtrado, "Grupo", "Valor","Quantidade",agrupar_outros)
df_despesas_anterior_por_categoria = agrupar_despesas_por_categoria(df_despesas_filtrado_anterior, "Centro_Custo", "Valor_Pago/Recebido",agrupar_outros)
df_despesas_por_categoria = agrupar_despesas_por_categoria(df_despesas_filtrado, "Centro_Custo", "Valor_Pago/Recebido",agrupar_outros)

# Gráficos
col1, col2 = st.columns(2)
with col1:
    insight_receitas(df_receitas_por_categoria,data_inicio,data_fim)
    st.subheader(f"Receitas por Categoria")
    if agrupar_outros:
        criar_graficos_pizza(df_receitas_por_categoria, "Receitas", "Grupo", "Valor", filial)
    else:
        criar_graficos_barra(df_receitas_por_categoria, "Receitas", "Grupo", "Valor", filial)

with col2:
    insight_despesas(df_despesas_por_categoria,df_despesas_anterior_por_categoria,data_inicio,data_fim)
    st.subheader("Despesas por Centro de Custo")
    if agrupar_outros:
        criar_graficos_pizza(df_despesas_por_categoria, "Despesas", "Centro_Custo", "Valor_Pago/Recebido", filial)
    else:
        criar_graficos_barra(df_despesas_por_categoria, "Despesas", "Centro_Custo", "Valor_Pago/Recebido", filial)

  