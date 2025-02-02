"""
Exercícios Práticos
Crie um programa que peça ao usuário para digitar dois números e imprima a soma, subtração, multiplicação e divisão entre eles.

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

print(f"Soma: {n1 + n2}\n")
print(f"Subtração: {n1 - n2}\n")
print(f"Multiplicação: {n1 * n2}\n")
print(f"Divisão: {n1 / n2}\n")

Faça um programa que peça ao usuário para digitar um número e imprima se ele é par ou ímpar.

n = int(input("Digita um número ai parceiro, que eu te conto se é impar ou par:"))

if n % 2 == 0:
    print(f"Seguinte, {n} é par meu consagrado")
else:
    print(f"Então meu chegado, {n} é impar.")

Crie um programa que imprima os números de 1 a 10 usando um loop for.

for n in range(1, 11):
    print(n)

Faça um programa que peça ao usuário para digitar um número e imprima a tabuada desse número usando um loop while.

tb = int(input("Digite um número: "))
n = 1
print(f"Tabuada de {tb}\n")
while n <= 10:
    print(f"{tb} x {n} = {tb*n}")
    n = n + 1

Crie um programa que peça ao usuário para digitar várias notas e calcule a média delas.

quantidade = int(input("Quantas notas vocês deseja fazer a média?"))

notas = []

for i in range(quantidade):
    nota = float(input(f"Digite a {i+1}ª nota:"))
    notas.append(nota)

media = sum(notas) / quantidade

print(f"A média é: {media:.2f}")

Verificação de Números Primos: Crie um programa que peça ao usuário para digitar um número e determine se ele é primo ou não.
Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.

n = int(input("Digite um número: "))

if (n > 1) and (n / n == 1) and not (n % 2 == 0):
    print(f"{n} é um número primo!")
else:
    print(f"{n} não é um número primo!")

Calculadora com Operações: Desenvolva uma calculadora que permita ao usuário realizar as quatro operações básicas
(adição, subtração, multiplicação e divisão). O programa deve solicitar os dois números e a operação desejada.

while True:
    print("Escolha um opção:")
    print("1 - Soma:")
    print("2 - Subtração:")
    print("3 - Multiplicação:")
    print("4 - Divisão:")
    print("5 - Sair")
    opcao = int(input())

    if opcao == 5:
        break

    num1 = int(input("Primeiro número:"))
    num2 = int(input("Segundo número:"))

    if opcao == 1:
        print(f"Resultado: {num1 + num2}\n\n")
    elif opcao == 2:
        print(f"Resultado: {num1 - num2}\n\n")
    elif opcao == 3:
        print(f"Resultado: {num1 * num2}\n\n")
    elif opcao == 4:
        print(f"Resultado: {num1 * num2}\n\n")
    else:
        print("Opção incorreta!")

Jogo de Adivinhação: Crie um jogo em que o computador gera um número aleatório entre 1 e 100,
e o usuário tem que adivinhar qual é o número. O programa deve dar dicas se o número digitado é maior
ou menor que o número gerado.

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
"""
palavra = "kennedh"

tentativas = 10
acertos = ["_"] * len(palavra)

for i in range(tentativas):
    r = input("Digite uma letra: ").lower()

    acertos = [r if r == letra else acertos[idx] for idx, letra in enumerate(palavra)]

    print(" ".join(acertos))

    if "_" not in acertos:
        print("Parabéns! Você acertou a palavra!")
        break
else:
    print(f"Você perdeu! A palavra era '{palavra}'.")