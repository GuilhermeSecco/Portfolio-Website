from flask import Flask
from views import bp_simulador, index, index_en, projetos

app = Flask(__name__)
app.secret_key = 'Shiro'

#Rotas principais
app.add_url_rule('/', view_func=index)
app.add_url_rule('/en', view_func=index_en)
app.add_url_rule('/projetos', view_func=projetos)

#Registra o simulador via blueprint
app.register_blueprint(bp_simulador)

if __name__ == '__main__':
    app.run(debug=True)