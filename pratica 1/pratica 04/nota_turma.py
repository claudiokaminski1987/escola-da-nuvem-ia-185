notas = []

while True:
    entrada = input("Digite uma nota de 0 a 10 ou 'fim' para encerrar: ")

    if entrada.lower() == "fim":
        break

    try:
        nota = float(entrada)
        if 0 <= nota <= 10:
            notas.append(nota)
        else:
            print("Nota inválida! Digite apenas valores entre 0 e 10.")
    except ValueError:
        print("Entrada inválida! Digite apenas números ou 'fim'.")

if notas:
    media = sum(notas) / len(notas)
    print(f"A média da turma é: {media:.2f}")
else:
    print("Nenhuma nota válida foi registrada.")