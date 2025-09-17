from flask import render_template, request, redirect, url_for, session, flash
from models.login import login_controller
#Importa a função que compara uma senha em teto pura do formulario com o hash que está no BD
from werkzeug.security import check_password_hash
from email_validator import validate_email, EmailNotValidError


def configura_rotas(app):
    #Rota principal e de Login
    @app.route('/')
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        msg = ''
        if request.methods == 'POST':
            email = request.form['email']
            senha_form = request.form['senha']
            #Utilizando o Model para buscar um email no BD
            usuario = Login.get_email(email) #verifica se tem o email no banco

            if usuario and check_password_hash(usuario['senha'], senha_form): #verifica se o usuario e senha combinam
                session['loggedin'] = True #logou no site
                session['id'] = usuario['id']
                session['nome'] = usuario['nome']
                return redirect(url_for('home'))
            else:
                msg = 'E-mail ou senha incorretos!'
        return render_template('login.html', msg=msg)

    #Rota de Logout    -   Remove os dados da sessão (session)
    @app.route('/logout'):
    def logout():
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('nome', None)
        return redirect(url_for('login'))

    #Rota de registro
    @app.route('/registro', methods=['GET', 'POST']):
    def registro():
        msg = ''
        if request.method == 'POST':
            nome = request.form['nome']
            email = request.form['email']
            senha = request.form['senha']

            conta_existente = Login.get_email(email)
            if conta_existente:
                msg = 'E-mail já cadastrado!'
            elif not nome.isalnum():
                msg = 'O nome do usuario deve conter apenas letras e numeros!'
            elif not nome or not senha or not email:
                msg = 'Por favor preencha todos os campos!'
            else:
                try:
                    valid = validate_email(email) #validade email verifica se o e-mail está no padrão
