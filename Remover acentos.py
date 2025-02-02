import unicodedata

def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFKD', texto) if not unicodedata.combining(c))

with open("palavras.txt", "r", encoding="utf-8") as f:
    palavras = f.read().splitlines()

palavras_sem_acentos = [remover_acentos(palavra) for palavra in palavras]

with open("palavras_sem_acentos.txt", "w", encoding="utf-8") as f:
    f.write("\n".join(palavras_sem_acentos))

print("Arquivo gerado: palavras_sem_acentos.txt")
