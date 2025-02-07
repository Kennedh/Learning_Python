#Escreva um programa que peça um número ao usuário e informe se ele é par ou ímpar.

def par_ou_impar():
    numero = int(input("Digite um número: "))
    if numero % 2 == 0:
        print("Este número é par")
    else:
        print("Este número é impar")