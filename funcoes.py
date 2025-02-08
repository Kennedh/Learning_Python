#Escreva um programa que peça um número ao usuário e informe se ele é par ou ímpar.
from os.path import split


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

#Crie um programa que peça uma palavra e verifique se ela é um palíndromo (lida de trás para frente é igual).

def verifica_palindromo():
    palavra = input("Digite uma palavra: ").lower()
    compara = palavra[::-1]
    if compara == palavra:
        print(f"A palavra {palavra} é um palindromo")
    else:
        print(f"A palavra {palavra} não é um palindromo")

#Escreva uma função que receba um número N e retorne o seu fatorial (N!).

def fatorial():
    n = int(input("Digite um número: "))
    fat = n
    for i in range(n,1,-1):
        fat = fat * (i-1)
    print(f"O fatorial de {n} é {fat}")

# Recebe um número n, dai esse número subtrai o dia atual e o dia resultado tem que trazer o dia da semana

from datetime import datetime,timedelta

dia_da_semana = { "Monday":"segunda", "Tuesday":"Terça",
                  "Wednesday":"Quarta",  "Thursday":"quinta", "Friday":"sexta",
                  "Saturday":"Sabado", "Sunday":"Domingo" }

def dia_semana_sbtr():
    n = int(input("Numero"))
    hoje = datetime.today()
    nd = hoje - timedelta(days=n)
    hoje.strftime("%A")

    print(hoje)
    print(dia_da_semana[hoje.strftime("%A")])
    print(nd)
    print(dia_da_semana[nd.strftime("%A")])
