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

#ordenar uma lista

ordem =