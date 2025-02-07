#Escreva um programa que peça um número ao usuário e informe se ele é par ou ímpar.

def par_ou_impar():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Este número é par")
    else:
        print("Este número é impar")

#Peça ao usuário um número N e calcule a soma de todos os números naturais até N.

def soma_naturais():
    n = int(input("Digite um número: "))
    i = 0
    natural = 0
    while i < n:
        i += 1
        natural = natural + i
    print(natural)

soma_naturais()