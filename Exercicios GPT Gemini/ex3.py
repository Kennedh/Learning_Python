"""
Faça um programa que peça ao usuário para digitar um número e imprima a tabuada desse número usando um loop while.
"""

tb = int(input("Digite um número: "))
n = 1
print(f"Tabuada de {tb}\n")
while n <= 10:
    print(f"{tb} x {n} = {tb*n}")
    n = n + 1
