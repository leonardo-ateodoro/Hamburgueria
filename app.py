from flask import Flask, render_template
from model.produto import recuperar_produtos, rec_destq

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    produtos = recuperar_produtos()
    destaques = rec_destq()
    return render_template("index.html", produtos = produtos, destaques = destaques)

@app.route("/produto")
def pagina_pagina2():
    return render_template("produto.html")

app.run(debug=True)