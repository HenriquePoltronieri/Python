from flask import Flask, request, render_template_string


app = Flask(__name__)

# Lista com dicionários para acesso
usuarios = [
    {'usuario': 'henrique', 'senha': '12400319'},
    {'usuario': 'marcos', 'senha': 'cotemig2026'},
    {'usuario': 'janaina', 'senha': 'cotemig2026'}
]

def show_the_login_form():
    return render_template_string("""
        <h2>Login</h2>
        <form method="POST">
            <input type="text" name="usuario" placeholder="Usuário"><br><br>
            <input type="password" name="senha" placeholder="Senha"><br><br>
            <button type="submit">Entrar</button>
        </form>
    """)

def do_the_login():
    usuario = request.form.get('usuario')
    senha = request.form.get('senha')

    # Percorre a lista de dicionários com for
    for u in usuarios:
        if usuario == u['usuario'] and senha == u['senha']:
            return f"<h1>Bem-vindo, {usuario}!</h1>"

    return "<h1>Login inválido</h1>"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        return do_the_login()
    else:
        return show_the_login_form()

if __name__ == "__main__":
    app.run(debug=True)