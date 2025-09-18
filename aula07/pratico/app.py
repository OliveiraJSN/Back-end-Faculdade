from flask import Flask
from controllers import login_controller

app = Flask(__name__, template_folder='views/templates', static_folder='views/static')

#Carrega as configurações do arquivo config.py
#"Vá até o config.py, enconre a classe Config, 
#leia as variáveis e carregue-as para dentro do
#objeto de configuração da aplicação (app.config)"
app.config.from_object('config.Config')

#Registra as rotas diretamente na aplicação
login_controller.configura_rotas(app)

if __name__ == '__main__':
    app.run(debug=True)






# Crie uma aplicação onde o usuário depois de logado tenha a 
# possibilidade de cadastrar um produto. A tabela de produtos
# deve possuir pelo menos as informações referente ao nome e
# descrição de um produto qualquer.