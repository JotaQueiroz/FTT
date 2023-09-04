from flask import Flask, redirect, render_template, request, url_for, jsonify

# Chamada pra biblioteca Flask
app = Flask(__name__)

# Criação da lista "personagens"
personagens = []

# Direcionamento pra API inicial
@app.route('/personagem')       
def inicio():
    return jsonify(personagens)

# Direcionamento pra API de criação de personagens
@app.route('/personagem/criar', methods = ['POST'])
def criar():
    data = request.get_json()
    if data:
        personagem = {
            "name": data.get('name'),
            "description": data.get('description'),
            "image": data.get('image'),
            "program": data.get('program'),
            "animator": data.get('animator')
        }
        personagens.append(personagem)
        return jsonify({"message": "Personagem criado com sucesso!"}), 201
    else:
        return jsonify({"message": "Error"}), 400

# Fim do programa
if __name__ == '__main__':
    app.run( debug = True )
