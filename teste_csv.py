# teste_csv.py
import pandas as pd

# --- CONFIGURAÇÃO ---
# Coloque o nome do seu arquivo CSV aqui
file_csv = 'b3_acoes.csv' 
# Coloque o nome provável da coluna com os tickers. Chute inicial: 'ticker' ou 'codigo'.
# Vamos descobrir o nome certo logo abaixo.
ticker = 'Ticker' # <--- VOCÊ VAI PRECISAR AJUSTAR ESTA LINHA

try:
    # O Pandas lê o arquivo. Tente com sep=';' primeiro. Se não der certo, tente sep=','.
    df_acoes = pd.read_csv(file_csv, sep=';')

    print("--- Arquivo CSV lido com sucesso! ---")
    
    # 1. Vamos ver as 5 primeiras linhas para entender a estrutura
    print("\n--- Amostra do seu arquivo (5 primeiras linhas): ---")
    print(df_acoes.head())
    
    # 2. Esta é a parte mais importante: vamos ver o nome de TODAS as colunas
    print("\n--- Nomes das colunas encontradas no arquivo: ---")
    print(df_acoes.columns.tolist())
    
    # 3. Agora, tente extrair a coluna de tickers para uma lista
    print(f"\nTentando extrair a coluna chamada '{ticker}'...")
    lista_de_tickers = df_acoes[ticker].tolist()
    
    print(f"\n✅ Sucesso! Extraí {len(lista_de_tickers)} tickers.")
    print("--- Amostra da lista de tickers (10 primeiros): ---")
    print(lista_de_tickers[:10])

except FileNotFoundError:
    print(f"ERRO: Arquivo '{file_csv}' não encontrado! Verifique se ele está na mesma pasta do script.")
except KeyError:
    print(f"ERRO: A coluna '{ticker}' não existe no arquivo!")
    print("Por favor, olhe a lista de 'Nomes das colunas encontradas' acima e corrija a variável ticker no código.")
except Exception as e:
    print(f"Ocorreu um erro inesperado: {e}")