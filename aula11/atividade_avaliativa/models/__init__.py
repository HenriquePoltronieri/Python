# Aqui nasce o "db" — é ele que conversa com o arquivo .db do SQLite.
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# O PONTO (.) no import = "pega da MESMA pasta models/"
# Ex.: from .autor = arquivo autor.py que está do seu lado, no mesmo apartamento.
# Já no controller a gente usa "from models import Autor" (sem ponto) porque olhamos de FORA.
from .base import ModeloBase
from .autor import Autor
from .emprestimo import ItemEmprestimo, Emprestimo

__all__ = ["db", "ModeloBase", "Autor", "Emprestimo", "ItemEmprestimo"]
