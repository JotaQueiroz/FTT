from flask import Flask, redirect, render_template, request, url_for, jsonify
"""
    Importação das bibliotecas utilizados no projeto.
"""

app = Flask(__name__)

personagens = []
"""
    Lista usada para a inclusão dos personagens.
"""

@app.route('/personagem')       
def inicio():
    """
    Essa função é a pagina de exibição de todos os personagens cadastrados.
    Return: Retorna a lista de personagens.
    """
    return jsonify(personagens)

@app.route('/personagem/criar', methods = ['POST'])
def criar():
    """
    Função utilizada para a crianção dos personagem recebendo os parâmetros:
    :param name: Nome do personagem
    :param description: Descrição do personagem
    :param image: Onde a imagem esta arquivada
    :param program: Nome do programa do personagem
    :param animator: Desenhista da arte do personagem
    Returns: Retorna a mensagem de 'Personagem criado com sucesso!'.
    """
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
