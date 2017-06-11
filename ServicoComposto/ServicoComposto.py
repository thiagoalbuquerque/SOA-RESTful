from flask import Flask, jsonify, abort, make_response, request
import requests
from flask_cors import CORS
from BasicoDeLogica.ServicoDeLogica import get_pontuacao

app = Flask(__name__)
CORS(app)

@app.route('/composto/p', methods=['GET'])
def get_p():
    publicacao = [
        {"Qualis": "A1", "Tipo": "Conferencia"},
        {"Qualis": "B2", "Tipo": "Revista"},
    ]

    return ""

@app.route('/composto', methods=['GET'])
def get_pontuacao_autor():
    pub_autor = requests.get('http://127.0.0.1:555/pub_autor')
    print(pub_autor.text)

    logica = requests.get('http://127.0.0.1:555/', pub_autor)
    print(logica)
    return ""


if __name__ == "__main__":
    app.run()