from app import app
from flask import render_template
@app.route("/")
@app.route("/index")
def index():
    nome="Elísio"
    dados={"profissao":"PROFESSOR","canal":"CANAL DO ELÍSIO"}
    return render_template('index.html',nome=nome,dados=dados)



@app.route("/contato")
def contato():
    return render_template('contato.html')


# if __name__ == "__main__":
#     app.run(debug=True)