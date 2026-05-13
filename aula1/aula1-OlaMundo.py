from flask import Flask


app = Flask(__name__) # inicio o flask

@app.route('/') # Isso é o decorator, ele é usado para mapear a função abaixo para a rota '/'
def ola_mundo():
    return 'Olá, Mundo!' # Isso é o que será retornado quando a rota '/' for acessada

@app.route('/hello') # Isso é outro decorator, mapeando a função abaixo para a rota '/hello'
def hello():
    return 'Hello, World!' # Isso é o que será retornado quando a rota '/hello' for acessada

if __name__ == '__main__':
    app.run(debug=True) # Isso inicia o servidor Flask em modo de depuração, o que é útil para desenvolvimento


# Atividade 1

@app.route('/') 
def decorator():
    return 'O que é: Um decorator (decorador) em Python é uma função que recebe outra função como parâmetro e estende seu comportamento sem modificar explicitamente seu código-fonte.' \
    'pra que serve: Reutilização de Código (DRY - Dont Repeat Yourself): Aplicar a mesma lógica a múltiplas funções.Separar Preocupações: Manter a lógica de negócios separada de infraestrutura (ex: verificar login antes de processar dados).Modificar Comportamento: Adicionar código antes ou depois da execução de uma função.' \
    'como utilizar: Quando o Flask inicia, ele lê seu código. Ao encontrar o @app.route('/sobre'), ele registra internamente que a função sobre() deve ser executada quando a rota /sobre for acessada.'
 