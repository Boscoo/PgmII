from pessoa import Pessoa
from flask import Flask, render_template, request

lista = []
app = Flask(__name__)
@app.route("/")
def start():
        return render_template("inicio.html")

@app.route("/listar_pessoa")
def listar():
        return render_template("listar_pessoa.html", pessoa=lista)

@app.route("/form_inserir_pessoa")
def insert():
        return render_template("form_inserir_pessoa.html")

@app.route("/adicionar_pessoa")
def add():
        nome = request.args.get("nome")
        endereco = request.args.get("endereco")
        telefone = request.args.get("telefone")
        identificacao = Pessoa(nome, endereco, telefone)
        lista.append(identificacao)
        return render_template("exibir_mensagem.html")
app.run(host="0.0.0.0")
