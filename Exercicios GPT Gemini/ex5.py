"""
Verificação de Números Primos: Crie um programa que peça ao usuário para digitar um número e determine se ele é primo ou não.
Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
"""

n = int(input("Digite um número: "))

if (n > 1) and (n / n == 1) and not (n % 2 == 0):
    print(f"{n} é um número primo!")
else:
    print(f"{n} não é um número primo!")
