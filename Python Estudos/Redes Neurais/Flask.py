
from flask import Flask

# Cria uma instância da classe Flask
app = Flask(__name__)

# Define uma rota padrão
@app.route('/')
def index():
    return 'Olá, mundo! Este é meu primeiro aplicativo Flask.'

# Define outra rota
@app.route('/saudacao/<nome>')
def saudacao(nome):
    return 'Olá, {}! Bem-vindo ao meu aplicativo Flask.'.format(nome)
    

# Executa o aplicativo se este arquivo for executado diretamente
if __name__ == '__main__':
    app.run(debug=True)
