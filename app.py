from flask import Flask
from minimo import minimo

app = Flask(__name__)

@app.route("/")
def home():
    return "API funcionando"

@app.route("/minimo")
def calcular():
    lista = [5, 2, 8, 1]
    return {"minimo": minimo(lista)}
