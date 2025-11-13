from flask import Flask
from views import bp_simulador, index, projetos

app = Flask(__name__)
app.secret_key = 'Shiro'

#Rotas principais
app.add_url_rule('/', view_func=index)
app.add_url_rule('/projetos', view_func=projetos)

#Registra o simulador via blueprint
app.register_blueprint(bp_simulador)

if __name__ == '__main__':
    app.run(debug=True)