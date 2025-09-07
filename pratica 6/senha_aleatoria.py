"""
Crie um programa que gera uma senha aleatória com o módulo random, 
utilizando caracteres especiais, 
possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.
"""
import random
import string

def gerar_senha(tamanho: int) -> str:
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = "".join(random.choice(caracteres) for _ in range(tamanho))
    return senha

# Exemplo de uso:
qtd = int(input("Digite a quantidade de caracteres da senha: "))
print("Senha gerada:", gerar_senha(qtd))