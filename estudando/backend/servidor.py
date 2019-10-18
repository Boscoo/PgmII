from flask import Flask, jsonify
from modelo import Pessoa
from playhouse.shortcuts import model_to_dict

app = Flask(__name__)

@app.route("/")
def index():
    return "backend do sistema de pessoas. <a href=/listar_pessoas> API listar pessoas </a>"

@app.route("/listar_pessoas")
def listar_pessoas():
    pessoas = list(map(model_to_dict, Pessoa.select()))
    return jsonify({'lista':pessoas})

app.run(debug=True, port=4999)