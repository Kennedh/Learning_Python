"""
Jogo de Adivinhação: Crie um jogo em que o computador gera um número aleatório entre 1 e 100,
e o usuário tem que adivinhar qual é o número. O programa deve dar dicas se o número digitado é maior
ou menor que o número gerado.
"""
import random

n = random.randint(1, 100)
r = ()

while r != n:
    r = int(input("Adivinhe o número: "))
    if r != n:
        print("Você errou!")
        if r > n:
            print(f"{r} é maior que número aleatório\n")
        else:
            print(f"{r} é menor que o número aleatório\n")
    else:
        print("Você acertou!")