from flask import Blueprint, redirect, render_template, request, url_for

from models import Autor, db

# BLUEPRINT = agrupador de rotas com apelido "autores"
# url_for('autores.listar') | URLs começam com /autores/
autores_bp = Blueprint("autores", __name__, url_prefix="/autores")


@autores_bp.route("/")
def listar():
    return render_template("autores/lista.html", autores=Autor.listar_ordenados())


@autores_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        nacionalidade = request.form.get("nacionalidade", "").strip()
        if not nome or not email:
            return render_template(
                "autores/formulario.html",
                titulo="Cadastrar autor",
                erro="Nome e e-mail são obrigatórios.",
                nome=nome,
                email=email,
                nacionalidade=nacionalidade,
            )
        Autor.salvar(nome, email, nacionalidade)
        return redirect(url_for("autores.listar"))

    return render_template("autores/formulario.html", titulo="Cadastrar autor")


@autores_bp.route("/editar/<int:autor_id>", methods=["GET", "POST"])
def editar(autor_id):
    autor = db.session.get(Autor, autor_id)
    if not autor:
        return redirect(url_for("autores.listar"))

    if request.method == "POST":
        nome = request.form.get("nome", "").strip()
        email = request.form.get("email", "").strip()
        nacionalidade = request.form.get("nacionalidade", "").strip()
        if not nome or not email:
            return render_template(
                "autores/formulario.html",
                titulo="Editar autor",
                erro="Nome e e-mail são obrigatórios.",
                nome=nome,
                email=email,
                nacionalidade=nacionalidade,
                autor_id=autor.id,
            )
        autor.atualizar(nome, email, nacionalidade)
        return redirect(url_for("autores.listar"))

    return render_template(
        "autores/formulario.html",
        titulo="Editar autor",
        nome=autor.nome,
        email=autor.email,
        nacionalidade=autor.nacionalidade or "",
        autor_id=autor.id,
    )


@autores_bp.route("/excluir/<int:autor_id>", methods=["POST"])
def excluir(autor_id):
    autor = db.session.get(Autor, autor_id)
    if autor:
        autor.excluir()
    return redirect(url_for("autores.listar"))
