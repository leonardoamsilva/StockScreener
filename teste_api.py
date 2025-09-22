import requests
import json

def explorar_api_tickers():
    url = "https://api.dadosdemercado.com.br/v1/tickers"
    
    print(f"Acessando a API em: {url}")
    
    try:
        response = requests.get(url)
        response.raise_for_status() 

        dados = response.json()
        
        print(f"\nSucesso! A API retornou {len(dados)} tickers.")
        print("\n--- Amostra dos 3 primeiros itens retornados: ---")

        print(json.dumps(dados[:3], indent=2, ensure_ascii=False))
        
        lista_de_tickers = [item['ticker'] for item in dados]
        
        print("\n--- Lista de tickers extraída (10 primeiros): ---")
        print(lista_de_tickers[:10])

        return lista_de_tickers

    except requests.exceptions.RequestException as e:
        print(f"Erro ao acessar a API: {e}")
        return None


if __name__ == "__main__":
    explorar_api_tickers()