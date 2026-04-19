import requests
import pandas as pd
from datetime import datetime
import os

def extrair_cotacao():
    print("--- ☁️  Iniciando Ingestão (Camada Bronze) ---")
    
    # URL da API (Dólar para Real)
    url = "https://economia.awesomeapi.com.br/json/daily/USD-BRL/15" # Últimos 15 dias
    
    try:
        response = requests.get(url)
        data = response.json()
        
        # Converte para DataFrame do Pandas
        df = pd.DataFrame(data)
        
        # Seleciona apenas as colunas que nos interessam
        df = df[['high', 'low', 'bid', 'timestamp']]
        
        # Salva o arquivo CSV (O seu bloco de 'Excel' no fluxograma)
        nome_arquivo = "dados_brutos.csv"
        df.to_csv(nome_arquivo, index=False)
        
        print(f"✅ SUCESSO: Arquivo '{nome_arquivo}' criado com {len(df)} linhas.")
        print(f"📍 Localização: {os.path.abspath(nome_arquivo)}")

    except Exception as e:
        print(f"❌ Erro na extração: {e}")

if __name__ == "__main__":
    extrair_cotacao()