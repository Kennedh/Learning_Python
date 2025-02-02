"""2. Faça um programa que leia um número inteiro fornecido pelo usuário. Se esse número for positivo, calcule
a raiz quadrada do número e apresente-a. Se o número for negativo, mostre uma mensagem dizendo que o
número é inválido."""


num = int(input("Escreva um número positivo: "))

if num >= 0:
    print(f"A raiz quadrada de {num} é {num**0.5:.2f}")
else:
    print("Número inválido!")
