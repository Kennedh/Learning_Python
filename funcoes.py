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
    n = int(input("Número de dias: "))
    hoje = datetime.today()
    nd = hoje - timedelta(days=n)
    hoje.strftime("%A")

    print(hoje)
    print(f"Data atual: {dia_da_semana[hoje.strftime("%A")]}\n")
    print(nd)
    print(f"Data subtraida: {dia_da_semana[nd.strftime("%A")]}")

# Peça um número N e imprima a sequência de Fibonacci até esse valor.

def fibonacci():
    n = int(input("Escreva um número: "))
    fib = [1,1]
    seq = 0
    #for i in range(1,n):
    while seq < n:
        seq = fib[-1] + fib[-2]
        if seq <= n:
            fib.append(seq)
        else:
            break
    print(fib)

# Crie uma função que recebe uma lista de números e a ordena sem usar .sort().

def ordena_lista(lista):
    return sorted(lista)

lista = [2,6,8,1,2,8,6,9,7,5,21]
print(f"Lista ordenada: {ordena_lista(lista)}")