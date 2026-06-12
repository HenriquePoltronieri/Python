import os

from flask import Flask

# Cada "bp" importado é um Blueprint — um pacote de rotas (autores, emprestimos, etc.)
from controllers import autores_bp, dashboard_bp, emprestimos_bp
from models import Autor, ItemEmprestimo, Emprestimo, db


def criar_app():
    app = Flask(
        __name__,
        template_folder="views/templates",
        static_folder="views/static",
    )

    pasta = os.path.abspath(os.path.dirname(__file__))
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
        pasta, "biblioteca.db"
    )
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.init_app(app)

    # BLUEPRINT — explicação rápida:
    # Em vez de jogar TODAS as rotas aqui no app.py, cada assunto fica no seu controller.
    # register_blueprint = "liga" esse pacote de rotas ao Flask (tipo plugar um módulo no jogo).
    # autores_bp     → URLs começam com /autores
    # emprestimos_bp → URLs começam com /emprestimos
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(autores_bp)
    app.register_blueprint(emprestimos_bp)


    with app.app_context():
        db.create_all()

    return app


app = criar_app()

if __name__ == "__main__":
    app.run(debug=True)
