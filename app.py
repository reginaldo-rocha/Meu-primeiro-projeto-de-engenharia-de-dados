import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px # A biblioteca que você acabou de instalar

st.set_page_config(page_title="Monitor Pro", layout="wide")

# Título Principal
st.title("📈 Dashboard Analítico de Câmbio")

def carregar_dados():
    conn = sqlite3.connect("meu_banco_dados.db")
    df = pd.read_sql_query("SELECT * FROM cotacoes", conn)
    conn.close()
    return df

try:
    df = carregar_dados()

    # --- LINHA 1: KPIs ---
    ult_preco = float(df['preco_compra'].iloc[0])
    col1, col2, col3 = st.columns(3)
    col1.metric("Dólar Hoje", f"R$ {ult_preco:.2f}")
    col2.metric("Máxima", f"R$ {float(df['maximo'].max()):.2f}")
    col3.metric("Mínima", f"R$ {float(df['minimo'].min()):.2f}")

    # --- LINHA 2: Gráficos ---
    col_esq, col_dir = st.columns([2, 1]) # Coluna da esquerda é o dobro da direita

    with col_esq:
        st.subheader("Variação Temporal")
        fig_linha = px.line(df, x='data_consulta', y='preco_compra', title="Evolução do Preço")
        st.plotly_chart(fig_linha, use_container_width=True)

    with col_dir:
        st.subheader("Distribuição")
        # Criando categorias para o Gráfico de Pizza
        df['categoria'] = pd.cut(df['preco_compra'], bins=3, labels=['Baixo', 'Médio', 'Alto'])
        contagem = df['categoria'].value_counts().reset_index()
        
        fig_pizza = px.pie(contagem, values='count', names='categoria', 
                           title="Frequência de Faixas de Preço",
                           hole=0.4) # Estilo Donut
        st.plotly_chart(fig_pizza, use_container_width=True)

    # --- LINHA 3: Tabela ---
    st.subheader("Dados Detalhados")
    st.dataframe(df, use_container_width=True)

except Exception as e:
    st.error(f"Erro: {e}")