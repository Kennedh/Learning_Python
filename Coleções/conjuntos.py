"""
Conjuntos em python e em qualquer outra linguagem se refere a Teoria dos conjuntos da matematica

- No python os conjuntos são chamado de Sets

Dito isso da mesma forma que a matemática:

- Sets não possuem valores duplicados;
- Sets não possuem valores ordenados;
- Elementos não são acessados via indice.

Conjuntos são bons para utilizar quando precisamos armazenar elementos sem se preocupar com ordenção,
ou com chaves ou indices.

Os conjuntos são representados por {} que diferente dos dicionários são represetados apenas por {valor} em vez
de {chave, valor}

#Definindo um conjunto:

#Forma 1

s = set({1, 2, 3, 4, 5, 6, 7, 2, 6, 4})

print(s)
print(type(s))

#Forma mais comum

s1 = {1, 2, 3, 4, 5, 6, 7, 2, 6, 4}

print(s1)
print(type(s1))


lista = [99,2,34,23,2,12,1,44,5,34]
print(f"lista: {lista}")

tupla = (99,2,34,23,2,12,1,44,5,34)
print(f"Tupla: {tupla}")

dicionario = {}.fromkeys(lista, "dict")
print(f"Dicionário: {dicionario}")

conjunto = set(lista)
print(f"Conjunto: {conjunto}")


#Adicionando elementos

s = {1, 2, 3}
print(s)

s.add(4)
s.add(4) #Duplicidade não gera erro
print(s)


#remover elementos

s = {1, 2, 3}
print(s)

# Forma 1

s.remove(1)
print(s)
s.remove(33) #Remover valores inexistentes gera erro

# Forma 2

s.discard(2)
print(s)
s.discard(33) #Valores inexistentes não gera erro

# Métodos matemáticos de conjuntos

estudantes_python = {"Marcos", "Patricia", "Ellen", "Pedro", "Julia", "Guilherme"}
estudantes_java = {"Fernando", "Gustavo", "Julia", "Ana", "Patricia"}

# Gerar um conjunto com nomes de estudantes únicos

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando pipe |

unicos2 = estudantes_java | estudantes_python
print(unicos2)

# Gerar conjunto de estudantes que estão em ambos os cursos (Conjuntos)

# Forma 1 - Utilizando intersection

inter = estudantes_python.intersection(estudantes_java)
print(inter)

# Forma 2 = Utilizando o &

inter2 = estudantes_java & estudantes_python
print(inter2)

# Gerar um conjunto de estudantes que não estão no outro curso

# Forma 1 - Utilizando difference

dif = estudantes_python.difference(estudantes_java)
print(dif)

# Forma 2 - Utilizando - (menos)

dif2 = estudantes_python - estudantes_java
print(dif2)

# Soma, Valor Máximo, Valor Mínimo e tamanho

conjunto = {1,2,3,4,5}

print(sum(conjunto))
print(max(conjunto))
print(min(conjunto))
print(len(conjunto))
"""
