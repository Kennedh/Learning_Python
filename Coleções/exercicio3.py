"""
3. Faça um programa que leia 10 valores, armazene-os em uma lista e apresente quantos valores pares ele
possui.
"""
lista = []
count = 0

print("Digite 10 valores:")

for i in range(10):
    num = int(input(f"Valor {i+1}: "))
    lista.append(num)

for par in lista:
    if par % 2 == 0:
        count += 1

print(f"A lista tem {count} números pares")