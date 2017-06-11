from flask import Flask, jsonify, abort, make_response, request
from flask_cors import CORS

from Dao.AutorDAO import AutorDAO
from Dao.PublicacaoDAO import PublicacaoDAO
from Modelo.Autor import Autor
from Modelo.Publicacao import Publicacao

app = Flask(__name__)
CORS(app)

@app.route('/autor', methods=['GET'])
def get_autor():
    autores = AutorDAO()
    vetor = []
    for autor in autores.get():
        aut = Autor(autor[0], autor[1])
        vetor.append(aut.toJson())
    print(vetor)
    return jsonify({"data": vetor})

@app.route('/autor', methods=['POST'])
def add_autor():
    if (not request.json) or (not 'cpf') in request.json:
        print(request)
        abort(400)
    autores = AutorDAO()
    autores.insert((request.json['cpf'],request.json['nome']))
    return ""

@app.route('/autor', methods=['PUT'])
def update_autor():
    if (not request.json) or (not 'cpf') in request.json:
        print(request)
        abort(400)
    autores = AutorDAO()
    autores.update((request.json['cpf'],request.json['nome']))
    return ""

@app.route('/publicacoes/<string:cpf>', methods=['GET'])
def get_publicacoes_por_autor(cpf):
    publicacoes = PublicacaoDAO()
    vetor = []
    for publicacao in publicacoes.get_publicacoes_by_autor(cpf):
        pub = Publicacao(publicacao[0])
        pub.qualis = publicacao[1]
        pub.nome_autor = publicacao[2]
        vetor.append(pub.toJsonCompleto())
    print(vetor)
    response = jsonify({"publicacoes": vetor})
    print(response)
    return response

@app.route('/publicacoes', methods=['GET'])
def get_publicacao():
    publicacoes = PublicacaoDAO()
    vetor = []
    for publicacao in publicacoes.get():
        pub = Publicacao(publicacao[1])
        vetor.append(pub.toJson())
    print(vetor)
    response = jsonify({"publicacoes": vetor})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/publicacoes', methods=['POST'])
def add_publicacao():
    if (not request.json) or (not 'titulo') in request.json:
        print(request)
        abort(400)
    publicacoes = PublicacaoDAO()
    publicacoes.insert(request.json['titulo'])
    return ""


@app.errorhandler(404)
def not_found():
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port='555')