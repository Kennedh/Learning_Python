"""
Calculadora com Operações: Desenvolva uma calculadora que permita ao usuário realizar as quatro operações básicas
(adição, subtração, multiplicação e divisão). O programa deve solicitar os dois números e a operação desejada.
"""

while True:
    print("Escolha um opção:")
    print("1 - Soma:")
    print("2 - Subtração:")
    print("3 - Multiplicação:")
    print("4 - Divisão:")
    print("5 - Sair")
    opcao = int(input())

    if opcao == 5:
        break

    num1 = int(input("Primeiro número:"))
    num2 = int(input("Segundo número:"))

    if opcao == 1:
        print(f"Resultado: {num1 + num2}\n\n")
    elif opcao == 2:
        print(f"Resultado: {num1 - num2}\n\n")
    elif opcao == 3:
        print(f"Resultado: {num1 * num2}\n\n")
    elif opcao == 4:
        print(f"Resultado: {num1 * num2}\n\n")
    else:
        print("Opção incorreta!")