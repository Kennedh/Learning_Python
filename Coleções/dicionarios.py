"""
Em algumas linguagens de progração, os dicionários Python são conhecidos
por mapas

Dicionários são coleções do tipo chave/valor

Dicionários são representados por chaves {}

print({})

    - Chaves e valor são separados por dois pontos 'chave:valor'
    - Os dois podem ser qualquer tipo de valor

# Forma mais comum para criação de dicionários

paises = {"br": "Brasil", "eua": "Estados unidos", "py": "Paraguai"}

print(paises)
print(type(paises))

# Forma menos comum

paises1 = dict(br="Brasil", eua="Estados Unidos", py="Paraguai")

print(paises)
print(type(paises))

# Acessando elementos

# Forma 1 - Acesando via Chave, da mesma forma que lista/tupla

print(paises["br"])

# Forma 2 - Acessando via get - Recomendado

print(paises.get("br"))

# Definir um valor padrão de busca caso não encontre no dicionário

p = input("Digite o a sigla do pais")

pais = paises.get(p, "Não encontrado")

print(pais)

#Verificar se uma chave está no dicionário

print("br" in paises)
print("ru" in paises)

# Adicionar elementos em um dicionário

receita = {"jan": 100, "fev": 120, "mar": 300}

print(receita)

# Forma 1 - Mais comum

receita["abr"] = 350

print(receita)

# Forma 2

novo_dado = {"mai": 500}

receita.update(novo_dado)

# Dá para adicionar valores e atualizar valores com update

receita.update({"jun": 850})
receita.update({"jan": 450})

print(receita)

# Remover dados de um dicionário

receita = {"jan": 100, "fev": 120, "mar": 300}

# Forma 1
receita.pop('mar')

print(receita)

# Forma 2

del receita["fev"]

print(receita)

receita = {"jan": 100, "fev": 250, "mar": 400}

print(receita.keys())
print(receita.values())

for chave, valor in receita.items():
    print(f"Chave: {chave} Valor: {valor}")

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita.values()))

"""
