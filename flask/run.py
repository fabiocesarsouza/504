from flask import Flask, jsonify, redirect, request
import requests
import json
from modulos.usuarios import usuario
from modulos.view import view

app = Flask(__name__)
app.register_blueprint(usuario)
app.register_blueprint(view)

@app.route('/', methods=['GET'])
def index():
    mensagem = {"mensagem": "api rest"}
    return jsonify(mensagem)

@app.route('/', methods=['POST'])
def metodo_post():
    print(request.get_json())
    return redirect('/')

@app.route('/cep/<string:busca>')
def buscar_end(busca):
    re = requests.get('https://viacep.com.br/ws/{}/json/'.format(busca))
    return jsonify(re.json())

if __name__=="__main__":
    app.run(host='0.0.0.0', debug=True, port=5000)    