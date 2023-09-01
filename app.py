from flask import Flask, redirect, render_template, request, url_for, jsonify


app = Flask(__name__)

personagens = []

@app.route('/personagem')       
def inicio():
    return jsonify(personagens)

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

if __name__ == '__main__':
    app.run( debug = True )
