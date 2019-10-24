from flask import Flask, render_template
from modelo import Pessoa
import requests
from playhouse.shortcuts import dict_to_model

app = Flask(__name__)

@app.route("/")
def index():
    return "frontend do sistema  de pessoas. <a href=/listar_pessoas> Operação Listar </a>"

@app.route("/listar_pessoas")
def listar_pessoas():
    dados_pessoas = requests.get('http://localhost:4999/listar_pessoas')
    json_pessoas = dados_pessoas.json()
    pessoas = []
    for pessoa_em_json in json_pessoas['lista']:
        p = dict_to_model(Pessoa, pessoa_em_json)
        pessoas.append(p)
    return render_template("listar_pessoas.html", lista = pessoas)

app.run(debug=True)