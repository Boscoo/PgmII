from pessoa import Pessoa
from flask import Flask, render_template, request, redirect, url_for

lista = []
app = Flask(__name__)
@app.route("/")
def start():
        return render_template("inicio.html")

@app.route("/listar_pessoa")
def list_person():
        return render_template("listar_pessoa.html", pessoa=lista)

@app.route("/form_inserir_pessoa")
def form_insert():
        return render_template("form_inserir_pessoa.html")

@app.route("/adicionar_pessoa")
def add_person():
	n_registro = request.args.get("nreg")
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	telefone = request.args.get("telefone")
	identificacao = Pessoa(n_registro, nome, endereco, telefone)
	lista.append(identificacao)
	return render_template("exibir_mensagem.html")

@app.route("/excluir_pessoa")
def remove_person():
	item = None
	cod = request.args.get("cod")
	for p in lista:
		if cod == p.n_registro:
			item = p
			break
	if item != None:
		lista.remove(item)
	return redirect(url_for("list_person"))

@app.route("/form_alterar_pessoa")
def form_alter():
	pe = None
	cod=request.args.get("cod")
	for pe in lista:
		if pe.n_registro == cod:
			return render_template("form_alterar_pessoa.html", pessoa=pe)
	return "Pessoa nao encontrada " + cod

@app.route("/alterar_pessoa")
def alter_person():
	nreg = request.args.get("nreg")
	nome = request.args.get("nome")
	endereco = request.args.get("endereco")
	telefone = request.args.get("telefone")
	novo = Pessoa(nreg, nome, endereco, telefone)
	for i in range(len(lista)):
		if lista[i].n_registro == nreg:
			lista[i] = novo
			return redirect(url_for("list_person"))
	return "Deu ruim!"

app.run(host="0.0.0.0", debug=True)

