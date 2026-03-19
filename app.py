from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return render_template("index.html")

@app.route("/agendamento", methods=["POST","GET"])
def agendamento():
    return redirect("https://wa.me//5511945717295?text=Gostaria%20de%20mais%20informações%20sobre%20o%20Espaço%20Mulher%20Campesina%20!💌")

@app.route("/especialidades")
def especialidades():
    return render_template("especialidades.html")

@app.route("/produtos")
def produtos():
    return render_template("produtos.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/promocao")
def promocao():
    return render_template("promocao.html")

@app.route("/blog")
def blog():
    return render_template("blog.html")

@app.route("/apresentacao")
def apresentacao():
    return render_template("apresentacao.html")

@app.route("/mentoria")
def mentoria():
    return render_template("mentoria.html")

@app.route("/artigo")
def artigo():
    return render_template("artigo.html")

@app.route("/whatsapp")
def whatsapp():
    return redirect("https://wa.me//5511945717295?text=Gostaria%20de%20mais%20informações%20sobre%20o%20Espaço%20Mulher%20Campesina%20!💌")


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)