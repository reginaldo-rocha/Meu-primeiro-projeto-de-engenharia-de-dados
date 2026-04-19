import pandas as pd
from datetime import datetime
import sqlite3

def transformar_e_salvar():
    print("--- ⚙️ Iniciando Transformação (Camada Silver) ---")
    
    # 1. Leitura do dado bruto (Bronze)
    try:
        df = pd.read_csv("dados_brutos.csv")
    except FileNotFoundError:
        print("❌ Erro: O arquivo 'dados_brutos.csv' não foi encontrado!")
        return

    # 2. Limpeza e Transformação
    # Converter o timestamp da API para uma data legível
    df['data_consulta'] = pd.to_datetime(df['timestamp'], unit='s')
    
    # Renomear colunas para algo mais profissional
    df = df.rename(columns={
        'bid': 'preco_compra',
        'high': 'maximo',
        'low': 'minimo'
    })
    
    # Selecionar apenas o que importa e organizar as colunas
    df_limpo = df[['data_consulta', 'preco_compra', 'maximo', 'minimo']]
    
    print("✅ Dados limpos e transformados!")
    print(df_limpo.head())

    # 3. Carga (Load) para o Banco SQLite (O Cilindro do seu desenho)
    conexao = sqlite3.connect("meu_banco_dados.db")
    df_limpo.to_sql("cotacoes", conexao, if_exists="replace", index=False)
    conexao.close()
    
    print("🚀 Sucesso! Dados salvos no banco 'meu_banco_dados.db'.")

if __name__ == "__main__":
    transformar_e_salvar()