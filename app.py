
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/pagina1')
def pagina1():
    datos = ["Python", "Flask", "Jinja2"]
    return render_template("pagina1.html", tecnologias=datos)

@app.route('/pagina2')
def pagina2():
    usuarios = [
        {"nombre": "Ana", "rol": "Admin"},
        {"nombre": "Luis", "rol": "Usuario"},
        {"nombre": "María", "rol": "Editor"}
    ]
    return render_template("pagina2.html", usuarios=usuarios)

if __name__ == "__main__":
    app.run(debug=True)
