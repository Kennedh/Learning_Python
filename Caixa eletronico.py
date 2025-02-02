
print("Bem vindo ao Kennedh's Bank\n")

saldo = 50

while True:
    print("1 - Deposito")
    print("2 - Saque")
    print("3 - Saldo")
    print("4 - Sair")
    opcao = input()

    if opcao == "1":
        deposito = int(input("Quanto você deseja depositar?"))
        saldo += deposito
        print(f"Saldo restante: R$ {saldo}")
    elif opcao == "2":
        saque = int(input("Quanto deseja sacar?"))
        saldo -= saque
        print(f"Saldo restante: R$ {saldo}")
    elif opcao == "3":
        print(f"Saldo: R$: {saldo}")
    elif opcao == "4":
        print("Encerrando programa...")
        break
    else:
        print("Opção errada!")

