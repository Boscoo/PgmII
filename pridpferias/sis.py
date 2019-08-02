from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("Index.html")

@app.route("/ListarReceita")
def listar():
    return render_template("ListarReceitas.html")

@app.route("/FormAdicionarIngrediente")
def formaddIng():
    return render_template("FormAdicionarIngredientes.html")

@app.route("/FormAdicionarReceita")
def fromaddReceita():
    return render_template("FormAdicionarReceita.html")

@app.route("/MostrarReceitas")
def mostrar():
    return render_template("MostrarReceitas.html")

@app.route("/addIngrediente")
def addIng():
    return render_template("ListarReceitas.html") 

app.run(port=7500, host="0.0.0.0", debug=True)    