import pandas as pd

file_csv = 'b3_acoes.csv' 

ticker = 'Ticker'

try:
    df_acoes = pd.read_csv(file_csv, sep=';')

    print("--- Arquivo CSV lido com sucesso! ---")
    
  
    print("\n--- Amostra do seu arquivo (5 primeiras linhas): ---")
    print(df_acoes.head())
    
    print("\n--- Nomes das colunas encontradas no arquivo: ---")
    print(df_acoes.columns.tolist())
    
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