#Escopo de variáveis
"""
numero = 34 #Variável Global

print(f"Variável Global: {numero}")

if numero > 10:
    numero_novo = numero + 10 #Variável Local
    print(f"Variável Local: {numero_novo}")
"""

#string
"""
nome = "kennedh"

print(nome.title())
print(type(nome))
print(nome[0:5])
"""

#booleano
"""
v = True
f = False

print(v)
print(type(v))

print(f)
print(type(f))

#negação not

print(not v)
print(not f)

num1,num2 = 2,8

res = num1 < num2

print(f"O resultado é {res}")
"""

#float A casas decimais são separadas por ponto
#Complex Quando se atribui a letra j
"""
valor = 1.86

print(valor)
print(type(valor))

res = int(valor)

print(res)
print(type(res))
"""

#numérico

"""
print("Descobrir se um número é par ou impar.\n")

numero = input("Digite o número que deseja descobrir.\n")

if int(numero) % 2 == 0:
    print("Par")
else:
    print("Impar")
"""