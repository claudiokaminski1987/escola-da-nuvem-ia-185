"""Calculadora de Consumo de Combustível
 Desenvolva um programa que calcula
   o consumo médio de combustível de um veículo.
     Use os seguintes dados: Distância percorrida: 300 km
       Combustível gasto: 25 litros
       O programa deve calcular o consumo médio (km/l) e exibir todos os dados da viagem,
 incluindo o resultado final arredondado para duas casas decimais."""

#dados da viagem
distancia_percorrida = 300  # em km
combustivel_gasto = 25      # em litros
#calculo do consumo medio
consumo_medio = distancia_percorrida / combustivel_gasto
#exibicao dos resultados
print(f"Distancia Percorrida: {distancia_percorrida} km")
print(f"Combustivel Gasto: {combustivel_gasto} litros")
print(f"Consumo Medio: {consumo_medio:.2f} km/l")
print(f"Media de consumo: {consumo_medio:.2f} km/l")
