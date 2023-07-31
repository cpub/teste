from app import app
from flask import render_template, request, flash, redirect
@app.route("/")
@app.route("/index")
def index():
    # PÁGINA COM PARAMETROS PASSADOS COM VARIÁVEIS
    nome="Elísios"
    dados={"profissao":"PROFESSOR","canal":"CANAL DO ELÍSIO"}
    return render_template('index.html',nome=nome,dados=dados)

@app.route("/contato")
def contato():
    # PÁGINAS SEM PARÂMENTROS EM LUGAR NENHUM
    return render_template('contato.html')

# PÁGINA COM PARÂMETROS PASSADOS NA URL
@app.route("/parametros/<nome>/<profissao>/<canal>")
def parametros(nome,profissao,canal):
    dados = {"profissao":profissao,"canal":canal}
    return render_template('parametros.html',nome=nome, dados=dados)


# MÉTODOS GET / POST
@app.route("/login1")
def login1():
    return render_template('login1.html')

@app.route("/autenticar1", methods=['GET'])
def autenticar1():
        # REQUEST PARA PEGAR OS DADOS DO FORMULÁRIO
        usuario = request.args.get('usuario')
        senha = request.args.get('senha')
        if (usuario == "admin" and senha=="senha123"):
            return "usuário {} e senha {}".format(usuario,senha)
        else:
            flash("DADOS INVÁLIDOS")
            flash("LOGIN OU SENHA INVÁLIDOS")
            return redirect('/login1')

@app.route("/login2")
def login2():
    return render_template('login2.html')
@app.route("/autenticar2", methods=['POST'])
def autenticar2():
        # REQUEST PARA PEGAR OS DADOS DO FORMULÁRIO
        usuario = request.form.get('usuario')
        senha = request.form.get('senha')
        return "usuário {} e senha {}".format(usuario,senha)





# if __name__ == "__main__":
#     app.run(debug=True)
