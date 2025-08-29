"""

Crie um programa que converta temperaturas entre Celsius,

 Fahrenheit e Kelvin. 

O usuário deve informar a temperatura,

 a unidade de origem e a unidade para qual deseja converter.
 """
temp = float(input("Digite a temperatura: "))
origem = input("Digite a unidade de origem (C/F/K): ").upper()
destino = input("Digite a unidade de destino (C/F/K): ").upper()

resultado = temp

# Converter para Celsius primeiro
if origem == "F":
    resultado = (temp - 32) * 5/9
elif origem == "K":
    resultado = temp - 273.15

# Converter de Celsius para destino
if destino == "F":
    resultado = resultado * 9/5 + 32
elif destino == "K":
    resultado = resultado + 273.15

print(f"Temperatura convertida: {resultado:.2f} {destino}")