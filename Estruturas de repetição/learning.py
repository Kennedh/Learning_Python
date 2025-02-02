#for
#Iterando sobre string
"""
nome = "Kennedh Custódio"

for letra in nome:
    print(letra)

#Iterando sobre lista

lista = [1, 3, 5, 7, 9]

for n in lista:
    print(n)

#Iterando sobre range

n = range(1, 50)

for numero in n:
    print(numero)

qtd = int(input("Quantas vezes você quer repetir o loop?"))

for n in range (1, qtd):
    print(f"Imprimindo {n}")

for n in range(1, 10+1,2):
    print(n)
"""
#While
"""
n = 1

while n <= 10:
    print(n)
    n = n+1
"""
#break
"""
for n in range(1, 11):
    if n == 6:
        break
    else:
        print(n)
print("Sai do loop")
"""

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == "sair":
        break
