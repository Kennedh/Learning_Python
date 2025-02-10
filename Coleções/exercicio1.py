"""
1. Crie um programa que lê 6 valores inteiros, armazene em uma lista e em seguida mostre na tela os valores
lidos.
"""

lista = []

for i in range(6):
    num = int(input(f"Valor {i+1}: "))
    lista.append(num)

print(lista)



