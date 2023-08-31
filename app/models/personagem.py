from app import db

# Crio uma classe pra incluir personagens
class Personagem:
# Definir função init
    def __init__(self, nome, descricao, imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.programa = programa
        self.animador = animador

# Definir função de apresentação
    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Imagem: {self.imagem}")
        print(f"Programa: {self.programa}")
        print(f"Animador: {self.animador}")

# Definir função de criação de personagem
def criar_personagem():
    nome = input("Digite o nome do personagem: ")
    descricao = input("Digite a descrição do personagem: ")
    imagem = input("Digite o link da imagem do personagem: ")
    programa = input("Digite o programa do personagem: ")
    animador = input("Digite o animador do personagem: ")
    return Personagem(nome, descricao, imagem, programa, animador)

