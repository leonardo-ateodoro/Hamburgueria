from flask import Flask, redirect, render_template, request , session
from model.produto import recuperar_produtos, rec_destq, recuperar_produto
from model.usuario import Usuario

app = Flask(__name__)
app.secret_key = "nao sei"
@app.route("/")
def pagina_inicial():
    produtos = recuperar_produtos()
    destaques = rec_destq()
    return render_template("index.html", produtos = produtos, destaques = destaques)

@app.route("/produto/<codigo>")
def pagina_pagina2(codigo):
    produto = recuperar_produto(codigo)
    return render_template("produto.html", produto = produto )

@app.route("/cadastrar_usuario", methods=["POST"])
def cadastrar_usuario():
        usuario = request.form.get ("usuario")
        senha = request.form.get ("senha")
        nome = request.form.get ("nome")

        novo_usuario = Usuario(usuario, senha, nome)
        novo_usuario.cadastrar()

        return redirect("/")

@app.route ("/logar/usuario", methods=["POST"])
def logar_usuario():
     usuario = request.form.get("usuario")
     senha = request.form.get("senha")

     resultado = Usuario.logar(usuario, senha)

     if not resultado:
        session["usuario_logado"] = resultado

     return redirect("/")      

     

@app.get("/cadastro_login")
def cadastro_login():
    return render_template("cadastro_login.html")

app.run(debug=True,host="0.0.0.0")