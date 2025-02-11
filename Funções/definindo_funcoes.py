"""
Definindo funções

- Funções são pequenos trechos de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- Muito uteis para executar procedimentos similares por repetidas vezes;

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- mas()
- min()
- count()
- e muitas outras.
"""

# Exemplo de utilização de funções:

#cores = ["verde", "amarelo", "azul", "branco"]

# Utilizando a função integrada (Built-in) do python print()

#print(cores)

#curso = "Programação em Python: Essencial"

#print(curso)

#cores.append("roxo")

#print(cores)

"""
Em python, a forma geral de definir uma função é:

def nome_da_funcao(parametro_de_entrada):
    bloco_da_funcao
    
Onde: 

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline;
parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula.
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.
"""

def diz_oi():
    print("Oi!")

# Utilizando funções

#diz_oi()

# Exmeplo 2

def cantar_parabens():
    print("Parabens pra você")
    print("Nesta data querida")
    print("Muitas felicidades")
    print("Muitos anos de vida")

cantar_parabens()
