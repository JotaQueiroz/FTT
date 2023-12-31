from flask import Flask, request, jsonify


app = Flask(__name__)


# Crio uma classe pra personagens
class Personagem:
# Definir função init
    def __init__(self, nome, descricao, imagem, programa, animador):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.programa = programa
        self.animador = animador

# Definir função de apresentação
    @app.route("/chars/", methods = ["POST"])
    def apresentar(self):
        print(f"Nome: {self.nome}")
        print(f"Descrição: {self.descricao}")
        print(f"Imagem: {self.imagem}")
        print(f"Programa: {self.programa}")
        print(f"Animador: {self.animador}")

# Definir função de criação de personagem
@app.route("/chars/", methods = ["GET"])
def criar_personagem():
    nome = input("Digite o nome do personagem: ")
    descricao = input("Digite a descrição do personagem: ")
    imagem = input("Digite o link da imagem do personagem: ")
    programa = input("Digite o programa do personagem: ")
    animador = input("Digite o animador do personagem: ")
    return Personagem(nome, descricao, imagem, programa, animador)



def main():
# Crio lista para os personagens
    personagens = []

    while True:
    # Crio layout de inicio    
        print("\n1 - Criar personagem")
        print("2 - Mostrar personagens")
        print("3 - Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            personagem = criar_personagem()
            personagens.append(personagem)
            print("Personagem criado com sucesso!")

        elif escolha == '2':
            print("\n--- Personagens ---")
            for personagem in personagens:
                personagem.apresentar()
                print("------------------")

        elif escolha == '3':
            print("Saindo...")
            break

        else:
            print("Opção inválida")


if __name__ == "__main__":
    app.run( port=5000 , host='localhost' , debug = True )
    
    