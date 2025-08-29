"""Crie uma função que verifique se uma palavra ou frase é um palíndromo
 (lê-se igual de trás para frente, ignorando espaços e pontuação). 

Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.

"""
import string

def eh_palindromo(texto: str) -> str:
    # Remove espaços e pontuações
    texto_limpo = "".join(ch.lower() for ch in texto if ch.isalnum())
    # Verifica se é palíndromo
    return "Sim" if texto_limpo == texto_limpo[::-1] else "Não"

# Exemplo de uso:
frase = input("Digite uma palavra ou frase: ")
print(f"É palíndromo? {eh_palindromo(frase)}")
