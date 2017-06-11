from flask import Flask, abort, jsonify, make_response, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

Qualis = [
    # O = Outros
    {"Qualis" : "O" , "Pontos" : 4, "Tipo" : "Capitlo_Livro"},
    {"Qualis" : "O" , "Pontos" : 4, "Tipo" : "Livro"},
    {"Qualis" : "O" , "Pontos" : 4, "Tipo" : "Edicao_livro"},

    #Revista
    {"Qualis" : "A1" , "Pontos" : 30, "Tipo" : "Revista"},
    {"Qualis" : "A2" , "Pontos" : 26, "Tipo" : "Revista"},
    {"Qualis" : "B1" , "Pontos" : 20, "Tipo" : "Revista"},
    {"Qualis" : "B2" , "Pontos" : 16, "Tipo" : "Revista"},
    {"Qualis" : "B3" , "Pontos" : 14, "Tipo" : "Revista"},
    {"Qualis" : "B4" , "Pontos" : 12, "Tipo" : "Revista"},
    {"Qualis" : "B5" , "Pontos" : 10, "Tipo" : "Revista"},
    {"Qualis" :  "C" , "Pontos" : 4,  "Tipo": "Revista"},
    {"Qualis" :  "S" , "Pontos" : 4,  "Tipo": "Revista"},

    #Conferencia
    {"Qualis": "A1", "Pontos": 20, "Tipo": "Conferencia"},
    {"Qualis": "A2", "Pontos": 18, "Tipo": "Conferencia"},
    {"Qualis": "B1", "Pontos": 16, "Tipo": "Conferencia"},
    {"Qualis": "B2", "Pontos": 12, "Tipo": "Conferencia"},
    {"Qualis": "B3", "Pontos": 10, "Tipo": "Conferencia"},
    {"Qualis": "B4", "Pontos": 8,  "Tipo": "Conferencia"},
    {"Qualis": "B5", "Pontos": 6,  "Tipo": "Conferencia"},
    {"Qualis": "C",  "Pontos": 4,  "Tipo": "Conferencia"},
    {"Qualis": "S",  "Pontos": 4,  "Tipo": "Conferencia"}

]

@app.route('/pontuacao', methods=['POST'])
def get_pontuacao():
    if (not request.json) or (not 'publicacoes') in request.json:
        print(request)
        abort(400)

    publicacoes = request.json['publicacoes']
    print(request.json['publicacoes'])
    pontuacao = 0
    for pub in publicacoes:
        for ql in Qualis:
            if pub['Qualis'] == ql['Qualis'] and pub['Tipo'] == ql['Tipo']:
                pontuacao += ql['Pontos']

    print(pontuacao)
    return jsonify(pontuacao)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port='666')
