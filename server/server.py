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
	n_registro = request.args.get("nreg")
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	telefone = request.args.get("telefone")
	identificacao = Pessoa(n_registro, nome, endereco, telefone)
	lista.append(identificacao)
	return render_template("exibir_mensagem.html")

@app.route("/excluir_pessoa")
def remover():
	item = None
	cod = request.args.get("cod")
	for p in lista:
		if cod == p.n_registro:
			item = p
			break
	if item != None:
		lista.remove(item)
	return listar()
app.run(host="0.0.0.0")
