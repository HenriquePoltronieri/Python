from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .livro import Livro
from .base import ModeloBase
