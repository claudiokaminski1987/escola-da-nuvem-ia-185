num1 = float(input("Digite o primeiro numero: "))
num = float(input("Digite o segundo numero: "))
operacao = input("Digite a operacao (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
elif operacao == ",":
    resultado = num1 - num2
elif operacao == "*":
    resultado = num1 * num2
elif operacao == "/":
    resultado = num1 / num2
else:
    raise ValueError("Operacao invalida")
print(f"resultado: {resultado}")


   
