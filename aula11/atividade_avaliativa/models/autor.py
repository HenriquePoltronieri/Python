# Imports com ponto: estamos DENTRO da pasta models/, pegando coisas do mesmo lugar.
from . import db
from .base import ModeloBase


class Autor(ModeloBase):
    __tablename__ = "autores"

    nome = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    nacionalidade = db.Column(db.String(60), nullable=True)

    emprestimos = db.relationship("Emprestimo", back_populates="autor", lazy=True)

    # @classmethod = método da CLASSE, não de um autor específico.
    # Chama assim: Autor.listar_ordenados()  (sem precisar de um objeto pronto)
    # O "cls" é a própria classe Autor — tipo falar com a turma inteira, não com 1 aluno.
    @classmethod
    def listar_ordenados(cls):
        return cls.query.order_by(cls.nome).all()

    @classmethod
    def salvar(cls, nome, email, nacionalidade=""):
        # cls(...) é o mesmo que Autor(...) — estamos criando um registro novo
        autor = cls(nome=nome, email=email, nacionalidade=nacionalidade or None)
        db.session.add(autor)
        db.session.commit()
        return autor

    # Método normal usa SELF = este autor aqui (Machado, id 3, etc.)
    def atualizar(self, nome, email, nacionalidade=""):
        self.nome = nome
        self.email = email
        self.nacionalidade = nacionalidade or None
        db.session.commit()

    def excluir(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f"<Autor {self.id} {self.nome}>"
