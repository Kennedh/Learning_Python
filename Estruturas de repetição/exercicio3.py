"""
3. Faça um programa que declare um inteiro, inicialize-o com 0, incremente-o de 1000 em 1000, imprimindo
seu valor na tela, até que seu valor seja 100000 (cem mil).
"""
n = int(input("Digite um número inteiro: "))

for numero in range(n, 100000, 1000):
    print(numero)