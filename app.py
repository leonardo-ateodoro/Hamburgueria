from flask import Flask, render_template

app = Flask (__name__)

@app.route("/")
def pagina_inicial():
    return render_template("index.html")

@app.route ("/pagina2")
def pagina_pagina2():
    return render_template ("pagina2.html")



app.run(debug=True)