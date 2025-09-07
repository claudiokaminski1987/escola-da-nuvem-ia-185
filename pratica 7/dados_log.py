"""Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning.
 Calcule a média e o desvio padrão do tempo de exercução constantes."""
Tempo: 12.5
Tempo: 10.8
Tempo: 11.2

import re
import statistics

tempos = []

# Lendo arquivo de log
with open("log.txt", "r") as f:
    for linha in f:
        match = re.search(r"(\d+(\.\d+)?)", linha)  # captura números (float/int)
        if match:
            tempos.append(float(match.group(1)))

if tempos:
    media = statistics.mean(tempos)
    desvio = statistics.pstdev(tempos)  # desvio padrão populacional
    print(f"Média do tempo: {media:.2f}")
    print(f"Desvio padrão: {desvio:.2f}")
else:
    print("Nenhum dado de tempo encontrado no log.")