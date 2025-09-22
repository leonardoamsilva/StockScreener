# teste_api.py

import requests
import json

def explorar_api_tickers():
    url = "https://api.dadosdemercado.com.br/v1/tickers"
    
    print(f"Acessando a API em: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status() # Verifica se a requisição foi bem-sucedida
        
        # A MÁGICA: .json() converte a resposta JSON diretamente para um objeto Python (lista de dicionários)
        dados = response.json()
        
        print(f"\nSucesso! A API retornou {len(dados)} tickers.")
        print("\n--- Amostra dos 3 primeiros itens retornados: ---")
        # Usando json.dumps para imprimir de forma bonita (indentado)
        print(json.dumps(dados[:3], indent=2, ensure_ascii=False))
        
        # Agora, vamos extrair apenas a lista de strings dos tickers
        # Usando uma técnica chamada "List Comprehension" - uma forma 'pythônica' e eficiente de criar listas
        lista_de_tickers = [item['ticker'] for item in dados]
        
        print("\n--- Lista de tickers extraída (10 primeiros): ---")
        print(lista_de_tickers[:10])

        return lista_de_tickers

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None

# --- Vamos executar nossa função de exploração ---
if __name__ == "__main__":
    explorar_api_tickers()