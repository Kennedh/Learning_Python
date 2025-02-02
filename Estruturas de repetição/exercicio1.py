"""1. Faça um programa que determine e mostre os cinco primeiros múltiplos de 3, considerando números
maiores que 0."""
n2 = 1

for n in range(-1, 50):
    if (n % 3 == 0) and (n > 0) and n2 <= 5:
        print(n)
        n2 = n2 + 1
