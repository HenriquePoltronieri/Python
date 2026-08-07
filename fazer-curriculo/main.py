from flask import Flask, render_template_string, request

app = Flask(__name__)

# --- TEMPLATES HTML ---
FORMULARIO_HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Criador de Currículo</title>
    <style>
        body { font-family: Arial, sans-serif; max-width: 500px; margin: 40px auto; padding: 20px; background: #f4f7f6; }
        .container { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 4px 15px rgba(0,0,0,0.1); }
        h2 { margin-top: 0; color: #333; }
        label { display: block; margin-top: 15px; font-weight: bold; color: #555; }
        input, textarea { width: 100%; padding: 10px; margin-top: 5px; box-sizing: border-box; border: 1px solid #ccc; border-radius: 4px; }
        button { margin-top: 20px; width: 100%; padding: 12px; background: #007BFF; color: white; border: none; border-radius: 4px; cursor: pointer; font-size: 16px; font-weight: bold; }
        button:hover { background: #0056b3; }
    </style>
</head>
<body>
    <div class="container">
        <h2>Preencha seus Dados</h2>
        <form action="/gerar" method="POST">
            <label>Nome Completo:</label>
            <input type="text" name="nome" required>

            <label>E-mail:</label>
            <input type="email" name="email" required>

            <label>Telefone:</label>
            <input type="text" name="telefone" required>

            <label>Resumo Profissional:</label>
            <textarea name="resumo" rows="3" required></textarea>

            <label>Experiência Profissional:</label>
            <textarea name="experiencia" rows="4" placeholder="Empresa - Cargo (Ano)" required></textarea>

            <label>Formação Acadêmica:</label>
            <textarea name="formacao" rows="3" placeholder="Curso - Instituição (Ano)" required></textarea>

            <button type="submit">Gerar Currículo</button>
        </form>
    </div>
</body>
</html>
"""

CURRICULO_HTML = """
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <title>Currículo - {{ dados.nome }}</title>
    <style>
        body { font-family: Georgia, serif; max-width: 800px; margin: 40px auto; padding: 20px; color: #333; line-height: 1.6; }
        h1 { margin-bottom: 5px; text-transform: uppercase; color: #111; letter-spacing: 1px; }
        .contato { font-style: italic; color: #666; margin-bottom: 25px; border-bottom: 2px solid #333; padding-bottom: 10px; font-size: 14px; }
        h2 { font-size: 18px; text-transform: uppercase; color: #0056b3; margin-top: 25px; border-bottom: 1px solid #ddd; padding-bottom: 3px; }
        p { margin: 8px 0; white-space: pre-line; }
    </style>
</head>
<body>

    <h1>{{ dados.nome }}</h1>
    <div class="contato">
        E-mail: {{ dados.email }} | Telefone: {{ dados.telefone }}
    </div>

    <h2>Resumo Profissional</h2>
    <p>{{ dados.resumo }}</p>

    <h2>Experiência Profissional</h2>
    <p>{{ dados.experiencia }}</p>

    <h2>Formação Acadêmica</h2>
    <p>{{ dados.formacao }}</p>

</body>
</html>
"""

# --- ROTAS FLASK ---
@app.route('/')
def formulario():
    return render_template_string(FORMULARIO_HTML)

@app.route('/gerar', methods=['POST'])
def gerar_curriculo():
    dados = {
        "nome": request.form.get("nome"),
        "email": request.form.get("email"),
        "telefone": request.form.get("telefone"),
        "resumo": request.form.get("resumo"),
        "experiencia": request.form.get("experiencia"),
        "formacao": request.form.get("formacao")
    }
    return render_template_string(CURRICULO_HTML, dados=dados)

if __name__ == '__main__':
    app.run(debug=True)
