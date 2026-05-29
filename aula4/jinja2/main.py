<<<<<<< HEAD
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def alunos():
    lista_alunos = [
        {"nome": "Ana", "nota": 8},
        {"nome": "Pedro", "nota": 5},
        {"nome": "Isabela", "nota": 7}
    ]
    return render_template('index.html', aluno=lista_alunos)

if __name__ == '__main__':
=======
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def alunos():
    lista_alunos = [
        {"nome": "Ana", "nota": 8},
        {"nome": "Pedro", "nota": 5},
        {"nome": "Isabela", "nota": 7}
    ]
    return render_template('index.html', aluno=lista_alunos)

if __name__ == '__main__':
>>>>>>> c1cde73a11a7dac0f90015f5bc7b5b1f31ba8d9d
    app.run(debug=True)