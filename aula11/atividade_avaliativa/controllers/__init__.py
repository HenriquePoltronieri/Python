# Esta pasta controllers/ exporta os Blueprints para o app.py registrar.
# Cada arquivo *_controller.py cria um Blueprint com nome único (ex: "autores").
from .autores_controller import autores_bp
from .dashboard_controller import dashboard_bp
from .emprestimos_controller import emprestimos_bp

__all__ = ["dashboard_bp", "autores_bp", "emprestimos_bp"]
