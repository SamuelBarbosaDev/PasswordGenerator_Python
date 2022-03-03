



#Como? Criar um gerador de senhas.

from random import choice
from string import punctuation as simbolos
from string import ascii_letters as letras
from string import digits as numeros

def senha(digito=8):
    digitos = int(digito)
    valores = letras + numeros + simbolos
    senha = ""

    for i in range(digitos):
        senha += choice(valores)
    return senha

variavel_senha = senha(20)

print("-"*100)
print("senha: ", variavel_senha)
print("-"*100)

