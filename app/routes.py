from app import app
from flask import render_template

@app.route('/')
@app.route('/casa')
@app.route('/index')
def index():
    data = {"dia":5, "autor":"Erick Ayres", "Nascimento":"23 de Maio"}
    return render_template('index.html',nome='Erix Code',dados=data)

@app.route('/contato')
def contato():
    return render_template('contato.html')