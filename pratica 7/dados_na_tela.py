"""Crie um script en Python que leia um arquivo CSV e exiba os dados na tela.
 O arquivo CSV deve conter informações de pessoas,
   com colunas Nome, Idade e Cidade."""
import csv

with open("pessoas.csv", "r", encoding="utf-8") as f:
    leitor = csv.reader(f)
    for linha in leitor:
        print(linha)
['Nome', 'Idade', 'Cidade']
['Ana', '25', 'São Paulo']
['Carlos', '30', 'Rio de Janeiro']
['Mariana', '22', 'Belo Horizonte']
