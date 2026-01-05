from flask import Flask
from views import bp_simulador, index

app = Flask(__name__)
app.secret_key = 'Shiro'

#Rotas principais
app.add_url_rule('/', view_func=index)

#Registra o simulador via blueprint
app.register_blueprint(bp_simulador)

if __name__ == '__main__':
    app.run(debug=True)