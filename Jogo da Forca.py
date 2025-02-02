"""
Jogo da Forca: Desenvolva um jogo da forca em que o computador escolhe uma palavra aleatória de uma lista,
e o usuário tem que adivinhar as letras da palavra.
O jogo termina quando o usuário acerta todas as letras ou esgota o número de tentativas.
"""
import random

with open("palavras.txt", encoding="utf-8") as f:
    w = f.read().splitlines()

palavra = random.choice(w)

tentativas = 12
acertos = ["_"] * len(palavra)

for i in range(tentativas):
    r = input("Digite uma letra: ").lower()

    acertos = [r if r == letra else acertos[idx] for idx, letra in enumerate(palavra)]

    print(" ".join(acertos))
    print(f"Tentativas restantes: {tentativas - (i+1)}\n")

    if "_" not in acertos:
        print("Parabéns! Você acertou a palavra!")
        break
    elif tentativas - (i+1) == 0:
        chute = input("Você sabe qual é a palavra?")
        if chute == palavra:
            print("Parabéns! Você acertou a palavra!")
            break
else:
    print(f"Você perdeu! A palavra era '{palavra}'.")
