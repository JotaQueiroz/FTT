from flask import Flask, redirect, render_template, request, url_for


app = Flask(__name__)


personagens = [{ 'nome': 'Jeff' , 'descricao': 'alto e magro' , 'imagem': 'C/Imagens' , 'programa': 'Egel' , 'animador': 'Matheus' }]


class Personagem:
    def __init__(self, nome, descricao, imagem, programa, animador ):
        self.nome = nome
        self.descricao = descricao
        self.imagem = imagem
        self.programa = programa
        self.animador = animador
        
@app.route('/', methods = ['GET'])       
def inicio():
    return render_template('index.html', personagens=personagens)

@app.route('/criar', methods = ['POST'])
def criar():
    nome = request.form.get('nome')
    descricao = request.form.get('descricao')
    imagem = request.form.get('imagem')
    programa = request.form.get('programa')
    animador =  request.form.get('animador')
    
    personagens = Personagem(nome, descricao, imagem, programa, animador )
    personagens.append(personagens)
    
    return redirect(url_for(inicio))

if __name__ == '__main__':
    app.run( debug = True )
