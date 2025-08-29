"""Crie uma função que calcule a gorjeta a ser deixada em um restaurante, 
baseada no valor total da conta e na porcentagem de gorjeta desejada.
 Calcule o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: 
valor_conta (float): O valor total da conta
 porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)

Retorna: 
float: O valor da gorjeta calculada


"""
def calcular_gorjeta(valor_conta: float, porcentagem_gorjeta: float) -> float:
    gorjeta = valor_conta * (porcentagem_gorjeta / 100)
    return gorjeta

# Exemplo de uso:
valor = float(input("Digite o valor da conta: "))
porcentagem = float(input("Digite a porcentagem da gorjeta: "))
print(f"Valor da gorjeta: R$ {calcular_gorjeta(valor, porcentagem):.2f}")
