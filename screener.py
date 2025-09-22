import requests
from bs4 import BeautifulSoup

def search_indicators(ticker):
  url = f'https://www.statusinvest.com.br/acoes/{ticker}'
  headers = {'User-Agent': 'Mozilla/5.0'}
  print(f"Buscando dados para {ticker}...")
  try:
    response = requests.get(url, headers=headers)
    response.raise_for_status()
  except Exception as e:
    print(f'Erro ao acessar {url} para o ticker {ticker}: {e}')
    return None
    
  soup = BeautifulSoup(response.content, 'html.parser')

  indicators = {'ticker': ticker, 'P/L': None, 'P/VP': None, 'ROE': None, 'D.Y': None}

  try:
    main_container = soup.find('div', class_='top-info')

    if not main_container:
      print("Container principal 'top-info' não encontrado. O site pode ter mudado.")
      return None

    all_indicators = soup.find_all('div', class_='item')

    for indicator in all_indicators:
      title_element = indicator.find('h3', class_='title')
      value_element = indicator.find('strong', class_='value')

      if title_element and value_element:
        title = title_element.text.strip()
        value_text = value_element.text.strip()

        if value_text in ['-', 'N/A', '']:
          continue

        try:
          if title == 'P/L':
            indicators['P/L'] = float(value_text.replace(',', '.'))
          elif title == 'P/VP':
            indicators['P/VP'] = float(value_text.replace(',', '.'))
          elif title == 'ROE':
            indicators['ROE'] = float(value_text.replace('%', '').replace(',', '.'))
          elif title == 'D.Y':
            indicators['D.Y'] = float(value_text.replace('%', '').replace(',', '.'))
            indicators['D.Y'] /= 100
            indicators['D.Y'] = format(indicators['D.Y'], '.2f')
        except Exception as e:
          print(f"Aviso para {ticker}: Não consegui converter o valor '{value_text}' para o indicador '{title}'. Erro: {e}")
  except Exception as e:
    print(f"Erro ao analisar (parse) os dados para {ticker}: {e}")
    return None

  if indicators['P/L'] is None or indicators['D.Y'] is None:
    print(f"Aviso: Falha ao extrair P/L ou D.Y para {ticker}. Dados parciais encontrados: {indicators}")
    return None

  return indicators

dados_petr4 = search_indicators('PETR4')
if dados_petr4:
  print("\nDados encontrados: ")
  print(dados_petr4)