# 📊 Pipeline de Engenharia de Dados: Monitoramento de Moedas

Este projeto automatiza a extração, tratamento e visualização de dados de cotação de moedas (USD/BRL). É um pipeline de dados completo seguindo a arquitetura medalhão (Bronze, Silver e Gold).

## 🛠️ Tecnologias Utilizadas
* **Linguagem:** Python 3.x
* **Ingestão:** Requests (API AwesomeAPI)
* **Processamento:** Pandas
* **Banco de Dados:** SQLite
* **Visualização:** Streamlit & Plotly
* **Versionamento:** Git & GitHub

## 🏗️ Arquitetura do Projeto!  

Aqui está o fluxo lógico dos dados:

![Fluxograma do Projeto] <img width="1024" height="335" alt="image" src="https://github.com/user-attachments/assets/4f096ea6-0c84-4bd2-8ce1-bb60bddacced" />

## 🖥️ Visualização de Dados (Streamlit)

<img width="1359" height="674" alt="dashboard 2 projeto" src="https://github.com/user-attachments/assets/adbfb459-0550-4816-a79f-2b3a96934e08" />


O dashboard foi construído para transformar dados brutos em insights acionáveis. As principais funcionalidades são:

- **Métricas em Tempo Real (KPIs):** Exibição do preço de compra atual com indicadores de máxima e mínima do período.
- **Gráfico de Evolução (Linha):** Visualização interativa da variação cambial ao longo do tempo usando Plotly.
- **Análise de Composição (Pizza):** Distribuição percentual das faixas de preço (Baixo, Médio, Alto) para entender a volatilidade.
- **Tabela de Dados Curados:** Acesso direto à Camada Silver/Gold processada pelo pipeline.


1.  **Ingestão (Extract):** O script `ingestao.py` consome dados de uma API financeira e salva em formato CSV (Camada Bronze).
2.  **Transformação (Transform/Load):** O script `transformacao.py` limpa os dados, converte timestamps em datas e carrega no banco de dados SQLite (Camada Silver/Gold).
3.  **Dashboard (Serve):** O arquivo `app.py` disponibiliza uma interface interativa para análise dos dados.

## 📁 Estrutura de Camadas (Medalhão)
* **Bronze:** `dados_brutos.csv` - Dados originais sem tratamento.
* **Silver/Gold:** `meu_banco_dados.db` - Dados limpos, tipados e estruturados em tabelas SQL, prontos para análise.

## 🚀 Como rodar o projeto
1. Clone o repositório:
   ```bash
   git clone [https://github.com/seu-usuario/seu-repositorio.git](https://github.com/seu-usuario/seu-repositorio.git)
   
