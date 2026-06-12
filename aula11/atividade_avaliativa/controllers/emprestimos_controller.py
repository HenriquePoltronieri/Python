from flask import Blueprint, redirect, render_template, request, url_for

from models import Autor, Emprestimo, db

# Outro Blueprint, outro "módulo" de rotas — mesmo app, pasta mental separada (emprestimos)
# No HTML: url_for('emprestimos.listar') — primeiro nome é o Blueprint, segundo é a função
emprestimos_bp = Blueprint("emprestimos", __name__, url_prefix="/emprestimos")

def _ler_itens_form():
    titulos = request.form.getlist("titulo")
    quantidades = request.form.getlist("quantidade")
    valores = request.form.getlist("valor_unitario")
    itens = []
    for titulo, qtd, valor in zip(titulos, quantidades, valores):
        titulo = titulo.strip()
        if not titulo:
            continue
        try:
            itens.append(
                {
                    "titulo": titulo,
                    "quantidade": int(qtd),
                    "valor_unitario": float(str(valor).replace(",", ".")),
                }
            )
        except ValueError:
            return None, "Quantidade ou valor inválido nos itens."
    if not itens:
        return None, "Adicione pelo menos um item ao empréstimo."
    return itens, None


# Decorator @route: GET em /emprestimos/ chama esta função
@emprestimos_bp.route("/")
def listar():
    return render_template(
        "emprestimos/lista.html", emprestimos=Emprestimo.listar_com_autor()
    )


@emprestimos_bp.route("/cadastrar", methods=["GET", "POST"])
def cadastrar():
    autores = Autor.listar_ordenados()
    if not autores:
        return render_template(
            "emprestimos/formulario.html",
            titulo="Novo empréstimo",
            autores=[],
            erro="Cadastre um autor antes de criar empréstimos.",
        )

    if request.method == "POST":
        try:
            autor_id = int(request.form.get("autor_id", 0))
        except ValueError:
            autor_id = 0
        observacao = request.form.get("observacao", "").strip()
        itens, erro_itens = _ler_itens_form()

        if not autor_id or not db.session.get(Autor, autor_id):
            erro = "Selecione um autor válido."
        elif erro_itens:
            erro = erro_itens
        else:
            # @classmethod — monta empréstimo + itens num lugar só
            Emprestimo.criar_com_itens(autor_id, itens, observacao)
            return redirect(url_for("emprestimos.listar"))
        return render_template(
            "emprestimos/formulario.html",
            titulo="Novo empréstimo",
            autores=autores,
            erro=erro,
            observacao=observacao,
        )

    return render_template(
        "emprestimos/formulario.html", titulo="Novo empréstimo", autores=autores
    )


@emprestimos_bp.route("/<int:emprestimo_id>")
def detalhe(emprestimo_id):
    emprestimo = db.session.get(Emprestimo, emprestimo_id)
    if not emprestimo:
        return redirect(url_for("emprestimos.listar"))
    return render_template("emprestimos/detalhe.html", emprestimo=emprestimo)
