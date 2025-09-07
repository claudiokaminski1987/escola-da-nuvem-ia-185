"""Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação 
ao Real Brasileiro (BRL).
 O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP),
   e o programa deve exibir o valor atual, máximo e mínimo da cotação, 
   além da data e hora da última atualização. 
Utilize a API da AwesomeAPI para obter os dados de cotação."""
import requests

moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper()
url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    chave = f"{moeda}BRL"
    
    if chave in dados:
        cotacao = dados[chave]
        print("=== Cotação ===")
        print("Moeda:", cotacao["code"])
        print("Valor atual (R$):", cotacao["bid"])
        print("Máximo do dia:", cotacao["high"])
        print("Mínimo do dia:", cotacao["low"])
        print("Data e hora:", cotacao["create_date"])
    else:
        print("Moeda não encontrada.")
else:
    print("Erro ao consultar cotação.")
