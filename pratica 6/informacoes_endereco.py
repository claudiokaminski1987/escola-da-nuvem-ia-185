"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário,
 utilizando a API ViaCEP.
   O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""
import requests

cep = input("Digite o CEP (somente números): ")
url = f"https://viacep.com.br/ws/{cep}/json/"

resposta = requests.get(url)

if resposta.status_code == 200:
    dados = resposta.json()
    
    if "erro" in dados:
        print("CEP não encontrado.")
    else:
        print("=== Endereço Encontrado ===")
        print("Logradouro:", dados.get("logradouro", ""))
        print("Bairro:", dados.get("bairro", ""))
        print("Cidade:", dados.get("localidade", ""))
        print("Estado:", dados.get("uf", ""))
else:
    print("Erro ao consultar CEP.")