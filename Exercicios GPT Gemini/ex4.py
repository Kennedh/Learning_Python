"""
Crie um programa que peça ao usuário para digitar várias notas e calcule a média delas.
"""

quantidade = int(input("Quantas notas vocês deseja fazer a média?"))

notas = []

for i in range(quantidade):
    nota = float(input(f"Digite a {i+1}ª nota:"))
    notas.append(nota)

media = sum(notas) / quantidade

print(f"A média é: {media:.2f}")