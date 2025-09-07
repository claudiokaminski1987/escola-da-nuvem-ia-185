"""Crie um script em Python que escreva dados em um arquivo CSV.
 O arquivo CSV deve conter informações pessoais,
 como colunas Nome, Idade e Cidade."""
import csv

dados = [
    ["Nome", "Idade", "Cidade"],
    ["Ana", 25, "São Paulo"],
    ["Carlos", 30, "Rio de Janeiro"],
    ["Mariana", 22, "Belo Horizonte"]
]

with open("pessoas.csv", "w", newline="", encoding="utf-8") as f:
    escritor = csv.writer(f)
    escritor.writerows(dados)

print("Arquivo pessoas.csv criado com sucesso!")
