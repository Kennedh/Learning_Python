"""
Verificação de Números Primos: Crie um programa que peça ao usuário para digitar um número e determine se ele é primo ou não.
Um número primo é aquele que é divisível apenas por 1 e por ele mesmo.
"""

n = int(input("Digite um número: "))

if n == 2:
    print("2 é um número primo!")
elif (n > 1) and (n % 2 != 0):
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            print(f"{n} não é um número primo!")
            break
    else:
        print(f"{n} é um número primo!")
else:
    print(f"{n} não é um número primo!")
