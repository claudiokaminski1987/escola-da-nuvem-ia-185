"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""
from datetime import datetime

def idade_em_dias(ano_nascimento: int) -> int:
    ano_atual = datetime.now().year
    idade_anos = ano_atual - ano_nascimento
    return idade_anos * 365

# Exemplo de uso:
ano = int(input("Digite o ano de nascimento: "))
print(f"Idade aproximada em dias: {idade_em_dias(ano)} dias")
