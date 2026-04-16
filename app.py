from flask import Flask, render_template
from model.produto import recuperar_produtos, rec_destq, recuperar_produto

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    produtos = recuperar_produtos()
    destaques = rec_destq()
    return render_template("index.html", produtos = produtos, destaques = destaques)

@app.route("/produto/<codigo>")
def pagina_pagina2(codigo):
    produto = recuperar_produto(codigo)
    return render_template("produto.html", produto = produto )

app.run(debug=True)