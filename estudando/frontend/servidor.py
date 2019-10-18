from flask import Flask, render_template
import requests
from playhouse.shurtcuts import dict_to_model

app = Flask(__name__)

@app.route("/")
def index():
    return "frontend do sistema  de pessoas. <a href=/listar_pessoas> Operação Listar </a>"

@app.route("/Listar_pessoas")
def listar_pessoas():
    dados_pessoas = requests.get('http://localhost:4999/Listar_pessoas')

app.run(debug=true)