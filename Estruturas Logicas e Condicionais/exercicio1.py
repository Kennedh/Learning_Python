#1. Faça um programa que receba dois números inteiros e mostre qual deles é o maior

num1 = int(input("Escreva o primeiro número:"))
num2 = int(input("Escreva o segundo número:"))

if num1 > num2:
    print(f"O número {num1} é maior que {num2}")
else:
    print(f"O número {num2} é maior que {num1}")
