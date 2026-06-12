from . import db
from .base import ModeloBase


class Emprestimo(ModeloBase):
    """Empréstimo principal — pertence a um Autor (chave estrangeira)."""

    __tablename__ = "emprestimos"

    autor_id = db.Column(db.Integer, db.ForeignKey("autores.id"), nullable=False)
    status = db.Column(db.String(30), nullable=False, default="pendente")
    observacao = db.Column(db.String(255), nullable=True)

    autor = db.relationship("Autor", back_populates="emprestimos")
    itens = db.relationship(
        "ItemEmprestimo", back_populates="emprestimo", cascade="all, delete-orphan"
    )

    # @property = "parece um atributo, mas calcula na hora"
    # Use: emprestimo.total   (SEM parênteses) — no template fica {{ emprestimo.total }}
    # Não guarda no banco; soma os itens toda vez que você pede.
    @property
    def total(self):
        return sum(item.subtotal for item in self.itens)

    @classmethod
    def listar_com_autor(cls):
        return cls.query.order_by(cls.data_criacao.desc()).all()

    @classmethod
    def criar_com_itens(cls, autor_id, itens_dados, observacao=""):
        emprestimo = cls(
            autor_id=autor_id,
            observacao=observacao or None,
            status="pendente",
        )
        db.session.add(emprestimo)
        db.session.flush()

        for item in itens_dados:
            db.session.add(
                ItemEmprestimo(
                    emprestimo_id=emprestimo.id,
                    titulo=item["titulo"],
                    quantidade=item["quantidade"],
                    valor_unitario=item["valor_unitario"],
                )
            )
        db.session.commit()
        return emprestimo

    def __repr__(self):
        return f"<Emprestimo {self.id} autor={self.autor_id}>"


class ItemEmprestimo(ModeloBase):
    """Itens do empréstimo — segunda tabela ligada a Emprestimo (FK)."""

    __tablename__ = "itens_emprestimo"

    emprestimo_id = db.Column(db.Integer, db.ForeignKey("emprestimos.id"), nullable=False)
    titulo = db.Column(db.String(120), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False, default=1)
    valor_unitario = db.Column(db.Float, nullable=False)

    emprestimo = db.relationship("Emprestimo", back_populates="itens")

    # @property de novo: quantidade * valor, sem chamar subtotal()
    @property
    def subtotal(self):
        return self.quantidade * self.valor_unitario

    def __repr__(self):
        return f"<ItemEmprestimo {self.titulo} x{self.quantidade}>"
