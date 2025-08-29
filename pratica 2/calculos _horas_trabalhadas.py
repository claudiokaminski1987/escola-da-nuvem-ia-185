"""Calculadora de salário por horas trabalhadas
 Leia o número de um funcionário, seu número de horas trabalhadas e
   o valor que recebe por hora.
     Calcule o salário do funcionário 
     e exiba o resultado formatado corretamente. 
     Entrada: O programa recebe 2 números inteiros e 1 número com duas casas decimais, representando: Número do funcionário (numero_funcionario). Quantidade de horas trabalhadas (horas_trabalhadas). 
Valor recebido por hora (valor_por_hora). Saída:"""
# leitura dos valores
numero_funcionario = int(input("Digite o numero do funcionario: "))
horas_trabalhadas = int(input("Digite o numero de horas trabalhadas: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))
# calculo do salario
salario = horas_trabalhadas * valor_por_hora
# exibição do resultado formatado
print(f"NUMBER = {numero_funcionario}")
print(f"SALARY = U$ {salario:.2f}")
# Fim do codigo