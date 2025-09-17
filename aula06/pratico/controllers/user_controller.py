from flask import render_template, request, redirect, url_for
from models.user import User

# Esta função recebe a instância da aplicação (app) e registra as rotas.
def configure_routes(app):

    #Rota principal que exibe a lista de usuários.
    @app.route('/')
    def index():
        # Busca todos os usuários usando o Model
        users = User.get_usuarios()
        # Renderiza o template 'index.html', passando a lista de usuários
        return render_template('index.html', users=users)

    #Rota que exibe o formulário de adição de usuário.
    @app.route('/contact')
    def contact():
        return render_template('contact.html')

    #Rota para processar a criação de um novo usuário.
    @app.route('/users/new', methods=['POST'])
    def create_user():
        name = request.form['name']
        email = request.form['email']
        
        # Chama o método do Model para criar o usuário no banco de dados
        User.criar_usuario(name, email)
        
        # Redireciona o usuário para a página principal
        return redirect(url_for('index'))