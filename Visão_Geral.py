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
# --- Parte HTML/CSS para a barra superior fixa e estilização ---
# Este código cria a barra superior fixa com a logo e o nome do sistema.
header_html = """
<style>
    /* Estilos para o elemento HTML body - para garantir que não haja margens */
    html, body {
        margin: 0;
        padding: 0;
        width: 100%;
        height: 100%;
        font-family: Arial, sans-serif; /* Garante uma fonte padrão */
        background-color: #f4f7fa; /* Cor de fundo geral da página */
    }

    /* Estilos para a barra superior fixa */
    .fixed-header {
        position: fixed; /* Fixa a barra no topo da tela */
        top: 0;
        left: 0;
        width: 100%; /* Ocupa a largura total */
        background-color: #ffffff; /* Fundo branco para a barra */
        padding: 10px 20px; /* Espaçamento interno */
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); /* Sombra sutil */
        display: flex; /* Usa Flexbox para alinhar os itens */
        justify-content: space-between; /* Distribui os itens: esquerda, centro, direita */
        align-items: center; /* Alinha os itens verticalmente no centro */
        /* O z-index é CRÍTICO para que a barra fique ACIMA de outros elementos do Streamlit */
        z-index: 9999; /* Um valor alto para garantir que esteja no topo */
        box-sizing: border-box; /* Inclui padding e borda no tamanho total */
    }

    /* Contêineres internos da barra para alinhamento */
    .header-left, .header-center, .header-right {
        display: flex;
        align-items: center;
    }

    /* Estilo da logo */
    .header-logo {
        height: 40px; /* Altura da logo */
        margin-right: 15px; /* Espaçamento à direita da logo */
        /* Garante que a imagem se ajuste */
        object-fit: contain;
    }

    /* Estilo do nome do sistema */
    .header-system-name {
        font-size: 1.2em; /* Tamanho da fonte */
        font-weight: bold; /* Negrito */
        color: #333; /* Cor do texto */
        flex-grow: 1; /* Permite que ocupe o espaço restante no centro */
        text-align: center; /* Centraliza o texto */
    }

    /* Estilo dos botões de ícone (Exportar, Configurações) */
    .header-icon-button {
        background: none; /* Sem fundo */
        border: none; /* Sem borda */
        font-size: 1.5em; /* Tamanho do ícone */
        color: #555; /* Cor do ícone */
        cursor: pointer; /* Cursor de mão ao passar por cima */
        margin-left: 15px; /* Espaçamento entre os ícones */
        transition: color 0.2s ease-in-out; /* Transição suave na cor */
    }

    .header-icon-button:hover {
        color: #007bff; /* Cor ao passar o mouse */
    }

    /* *** CRÍTICO para Streamlit: Adiciona um padding ao contêiner principal do Streamlit *** */
    /* Inspecione o elemento no navegador (F12) para encontrar a classe do contêiner principal
       do seu Streamlit se '.st-emotion-cache-1jm6gvw' não funcionar.
       Esta classe é uma suposição para versões mais recentes do Streamlit.
       Pode ser 'st-main', '.main' ou outro hash gerado pelo Streamlit. */
    .st-emotion-cache-1jm6gvw { /* Exemplo de classe comum para o main container do Streamlit */
        padding-top: 150px !important; /* Empurra o conteúdo para baixo, !important pode ser necessário */
    }
    /* Se a classe acima não funcionar, tente também: */
    .main { /* Outra classe comum para o contêiner principal */
        padding-top: 70px !important;
    }
    .stApp > header { /* Para algumas versões, o header do Streamlit pode interferir */
        z-index: 0 !important; /* Coloca o header do Streamlit por baixo do seu */
        height: 0 !important; /* Esconde o header padrão do Streamlit */
        visibility: hidden !important;
    }

</style>

<div class="fixed-header">
    <div class="header-left">
        <img src="https://raw.githubusercontent.com/Caua1705/fuji_analytics/main/assets/novinha.png" alt="Logo FUJI" class="header-logo">
    </div>
    <div class="header-center">
        <span class="header-system-name">Visão Estratégica | Fuji Analytics</span>
    </div>
    <div class="header-right">
        <span class="header-icon-button">📤</span>
        <span class="header-icon-button">⚙️</span>
    </div>
</div>
"""

# Injetar o HTML/CSS da barra superior no Streamlit
st.markdown(header_html, unsafe_allow_html=True)

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

  