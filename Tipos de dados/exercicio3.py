#3. Faça um programa que recebe três valores e apresente a soma dos quadrados dos valores lidos.

print("Soma do quadrado de 3 números\n")

num1 = int(input("Digite o primeiro número:\n"))
num2 = int(input("Digite o segundo número:\n"))
num3 = int(input("Digite o terceiro número:\n"))

soma = (num1 ** 2) + (num2 ** 2) + (num3 ** 2)

print(f"Resultado: {soma}")