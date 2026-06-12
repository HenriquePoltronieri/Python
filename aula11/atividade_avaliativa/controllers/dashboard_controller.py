from flask import Blueprint, render_template

from models import Autor, Emprestimo

# Blueprint da home — sem url_prefix, então "/" é a raiz do site
dashboard_bp = Blueprint("dashboard", __name__)


@dashboard_bp.route("/")
def index():
    return render_template(
        "index.html",
        total_autores=Autor.query.count(),
        total_emprestimos=Emprestimo.query.count(),
        emprestimos_recentes=Emprestimo.listar_com_autor()[:5],
    )
