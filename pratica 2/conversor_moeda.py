"""Conversor de Moeda Crie um programa que converte um valor em reais
 para dólares e euros. 
 Use os seguintes dados: Valor em reais: R$ 100.00 
 Taxa do dólar: R$ 5.60 
 Taxa do euro: R$ 6.60
   O programa deve calcular e exibir os valores convertidos,
 arredondando para duas casas decimais."""
#valor_reais = 100.00 #valor em reais
valor_reais = float(input("Digite ovalor em reais: R$ "))
taxa_dolar = 5.60 # taxa do dolar
taxa_euto = 6.60 # taxa do euro
#calculo do valor em dolares
valor_dolares = valor_reais / taxa_dolar
#calculo do valor em euros
valor_euros = valor_reais / taxa_euto
#exibicao dos resultados
print(f"Valor em Reais: R$ {valor_reais:.2f}")
print(f"Valor em Dolares: $ {valor_dolares:.2f}")
print(f"Valor em Euros: £ {valor_euros:.2f}")
# Fim do Codigo
