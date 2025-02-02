#Estruturas Lógicas: and, or, not, is

user = input("Usuário: ")
senha = input("Senha: ")

if user == ("kennedh" or "Kennedh" or "KENNEDH") and senha == "12345":
    print(f"Bem-vindo {user.title()}")
else:
    print("Nome de usuário ou senha incorretos!")

#not inverte o valor
#is compara variavel para ver se possuem o mesmo valor na memória

"""
ativo = True
logado = True

if ativo and logado:
    print("Bem-vindo usuário!")
else:
    print("Você precisa ativar sua conta. Por favor cheque seu e-mail")
"""


#Estruturas condicionais: if, else, elif
"""
idade = int(input("Digite sua idade."))

if idade < 18:
    print("Menor de idade")
elif idade == 18:
    print("Parabens, agora você é maior de idade!")
else:
    print("Maior de idade")
"""