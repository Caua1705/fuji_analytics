'''

PÁGINA VISAO GERAL:

st.title("📊 Visão Geral do Negócio")

# Sidebar – Filtros
with st.sidebar:
    st.subheader("📅 Filtros de Período")
    data_inicio = st.date_input("Data de início")
    data_fim = st.date_input("Data de fim")
    st.selectbox("Filtrar por praça", options=["Todas", "Salão", "Delivery"])
    st.button("🔄 Atualizar Dados")

# Tabs principais
aba1, aba2 = st.tabs(["📈 Visão Financeira", "📅 Evolução Mensal"])

with aba1:
    st.subheader("✅ Métricas Financeiras")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Receita Total", "R$ 125.000")
    col2.metric("Despesa Total", "R$ 72.000")
    col3.metric("Lucro Total", "R$ 53.000")
    col4.metric("Ticket Médio", "R$ 29,75")

    st.markdown("---")
    st.subheader("📊 Distribuição de Receita e Despesas")

    col5, col6 = st.columns(2)
    with col5:
        st.plotly_chart(grafico_receita_por_categoria, use_container_width=True)
    with col6:
        st.plotly_chart(grafico_despesas_por_categoria, use_container_width=True)

    st.markdown("---")
    st.subheader("🔍 Insights")
    st.success("🟢 Bebidas representam 20% das vendas, mas 35% da receita.")
    st.warning("🔴 Despesas com fornecedores são 65% do custo total.")

with aba2:
    st.subheader("📅 Evolução Mensal")

    st.plotly_chart(grafico_linha_receita_despesa, use_container_width=True)

    st.markdown("---")
    st.subheader("📄 Detalhamento por Mês")
    st.dataframe(tabela_mensal)

    st.markdown("---")
    st.info("📌 Maio foi o mês com maior lucro do trimestre.")

    ----------------------------------------------------------------------------------------

    PÁGINA DESEMPENHO DE PRODUTOS

# Tab 1 — 📊 Resumo
st.subheader("🏆 Top Produtos")
# Métricas
st.metric("Produto mais vendido", "Produto X (10.000 un)")
st.metric("Produto com maior faturamento", "Produto Y (R$ 150.000)")

# Gráfico barras
st.plotly_chart(fig_top_quantidade)
st.plotly_chart(fig_top_faturamento)

st.info(f"🔍 O produto **{produto_mais_vendido}** lidera em volume de vendas, com {quantidade_mais_vendida} unidades. Já o produto **{produto_maior_faturamento}** gerou o maior faturamento, totalizando R$ {faturamento_maior_produto:,.2f}.")

---

# Tab 2 — 🔥 Populares
st.subheader("⚠️ Produtos Populares com Baixa Rentabilidade")
# Tabela
st.dataframe(df_populares_baixa_rentabilidade)

# Insight textual
st.warning("🔍 Produto X tem alta saída, mas baixa margem. Pode estar subvalorizado.")

# Gráfico scatter quantidade x ticket médio
st.plotly_chart(fig_scatter_quantidade_ticket)

---

# Tab 3 — 💎 Premium
st.subheader("📉 Produtos com Baixo Volume e Alto Ticket")
# Tabela
st.dataframe(df_baixo_volume_alto_ticket)

# Insight textual
st.info("💡 Produtos com baixa saída e alto ticket podem precisar de promoção para aumentar giro.")

# Gráfico barras ticket médio vs quantidade
st.plotly_chart(fig_barras_ticket_quantidade)

---

# Tab 4 — 💰 Lucratividade
st.subheader("💰 Margem por Produto")
# Tabela margem
st.dataframe(df_margem_produtos)

# Métricas
st.metric("Margem Total", "R$ 50.000")
st.metric("Margem Média por Produto", "R$ 1.500")

# Gráfico barras margem top produtos
st.plotly_chart(fig_barras_margem)

# Insight textual
st.success("🔍 Produto Y é o mais lucrativo e deve ser foco de estratégias de venda.")


---------------------------------------------------------------------------------------------------------

PÁGINA DE CLIENTES E DELIVERY

st.subheader("🚚 Visão Geral do Delivery")

- Total de pedidos
- Receita total (delivery)
- Ticket médio (delivery)
- % do delivery nas vendas totais

TAB 1(PERFORMACE)

st.subheader("🏆 Produtos mais vendidos via delivery")

- Tabela: Produto | Qtde vendida | Receita

st.subheader("👤 Entregadores mais ativos")

- Tabela: Entregador | Qtde de entregas | Média por dia

🔍 *Insight*: "O delivery representa X% da receita — explorar promoções específicas pode alavancar vendas."

TAB2 (BAIRRO)

st.subheader("🌍 Faturamento por Bairro")

- Gráfico de barras: Faturamento total por bairro (ex: `px.bar(...)`)
- Gráfico de pizza: Percentual de pedidos por bairro (ex: `px.pie(...)`)

st.subheader("📈 Ticket Médio por Bairro")

- Tabela: Bairro | Quantidade de pedidos | Ticket médio (ordenada decrescente)

st.success("🔍 Bairro Y tem o maior ticket médio. Pode valer a pena investir em fidelização nesse público.")

TAB 3 (HORÁRIOS DE PICO)

st.subheader("🕐 Pedidos por Horário")

- Gráfico de linhas: Qtde de pedidos por hora

st.subheader("📅 Pedidos por Dia da Semana")

- Gráfico de barras: Segunda a domingo

🔍 *Insight*: "A maioria dos pedidos ocorre nas noites de sexta e sábado. Ideal para ofertas programadas."




















































































































































































'''