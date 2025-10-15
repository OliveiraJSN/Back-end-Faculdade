from flask import Flask
from controllers import user_controller

# Inicializa a aplicação Flask
app = Flask(__name__, template_folder='views/templates', static_folder='views/static')

# Registra as rotas a partir do controller.
user_controller.configure_routes(app)

# Executa a aplicação
if __name__ == '__main__':
    app.run(debug=True)