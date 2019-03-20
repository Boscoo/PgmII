from pessoa import Pessoa
from flask import Flask, render_template

lista = [Pessoa("Fulano", "Rua 4", "3333-3333"),
         Pessoa("Detal", "Rua cinza", "3333-2244")
        ]
app = Flask(__name__)
@app.route("/")
def start():
    return render_template("listar_pessoa.html", pessoa=lista)
app.run()
