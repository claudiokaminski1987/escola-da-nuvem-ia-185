"""Crie um script em Python que leia e escreva dados em um arquivo JSON.
 O arquivo JSON deve conter informações de uma pessoa,
 com campos nome, idade e cidade."""
import json

# Criando dicionário com dados da pessoa
pessoa = {
    "nome": "João",
    "idade": 28,
    "cidade": "Curitiba"
}

# Escrevendo no arquivo JSON
with open("pessoa.json", "w", encoding="utf-8") as f:
    json.dump(pessoa, f, ensure_ascii=False, indent=4)

print("Arquivo pessoa.json criado com sucesso!")

# Lendo o arquivo JSON
with open("pessoa.json", "r", encoding="utf-8") as f:
    dados = json.load(f)
    print("Dados lidos do JSON:", dados)

