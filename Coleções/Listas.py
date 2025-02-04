"""

#listas em python são representadas em colchetes []

lista1 = [1, 23, 34, 46, 67, 89,98]
lista2 = ["a", "d", "e", "f", "h", "j", "t"]
lista3 = []
lista4 = list(range(11))
lista5 = list("Kennedh")

# checar se determinado valor está na lista

if 8 in lista4:
    print("Encontrei o número 8")
else:
    print("Não encontrei o número 8")

if "e" in lista5:
    print("Encontrei a letra 'e'")
else:
    print("Não encontrei a letra 'e'")

#Ordenar uma lista

lista5.sort()
print(lista5)

#Contar os itens da lista

l = len(lista1)
print(l)

#Contar itens especificos da lista

n = lista5.count("e")
print(n)

#Adicionar elemento na lista com appen (apenas um elemento)

print(lista5)
lista5.append("")
print(lista5)

#Para adicionar mais de um elemento utiliza o extend

lista5.extend(["C", "u", "s", "t", "ó", "d", "i", "o"])
print(lista5)


#É possivel adicionar um elemento em uma posição especifica da lista
#Obs: O novo elemento é adicionado a direita do elemento

lista = list(range(15))
print(lista)
lista.insert(3, "Teste")
print(lista)

#É possivel juntar duas listas

lista2 = ["a","b","c","d","e"]
lista3 = lista + lista2
print(lista3)

#tambem é possivel utilizar o extend para unir uma lista em outra sem criar uma nova

lista.extend(lista2)
print(lista)

#Inverter uma lista

lista.reverse()
print(lista)


lista1 = list(range(0,15))
lista2 = list(range(15,15))

#copia de lista

lista3 = lista1.copy()

#remover ultimo elemento de uma lista

lista3.pop()

#Agora escolhendo a posição

lista3.pop(4)

#Transformar uma string em lista

frase = "Transformando string em lista"
nome = "Kennedh"
print(nome)
nome = list(nome)
frase = frase.split()
print(nome)
print(frase)

#Agora transformando uma lista em string

frase2 = " ".join(frase)
print(frase2)

lista = list(range(20))

# Itarando sobre listas

for n in lista:
    print(n)

# Utilizando while

carrinho = []
produto = ""

while produto != "sair":
    print("Adicione um produto na lista ou digite 'sair' para sair")
    produto = input()
    if produto != "sair":
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

# Utilizando variáveis em listas

numeros = list(range(1,5))

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

lista = [num1,num2,num3,num4,num5]

print(numeros)
print(lista)

# Imprimir um item especifico

print(lista[3])

#Descobrir em qual indice está o elemento

lista = list(range(5,20))

print(lista.index(5))


lista = list(range(5,20))

print(lista)

print(lista.index(6,0)) #buscando 6 apartir da posição 0

# Revisão slicing

# lista [inicio:fim:passo]
# range (inicio:fim:passo)

# Tralhando com slice de lista com o parametro "inicio"

lista = [1, 2, 3, 4, 5]

print(lista[1:])
print(lista[:2])
print(lista[:4])
print(lista[1::2])

lista = [1, 2, 3, 4, 5]

print(sum(lista))
print(max(lista))
print(min(lista))
print(len(lista))
"""

# Desempacotamento de listas

lista = [1,2,3]

num1, num2, num3 = lista

print(num1)
print(num2)
print(num3)