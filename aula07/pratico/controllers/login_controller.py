from flask import render_template, request, redirect, url_for, session, flash
from models.login import Login
from werkzeug.security import check_password_hash
from email_validator import validate_email, EmailNotValidError

def configura_rotas(app):
    #Rota principal e de Login
    @app.route('/')
    @app.route('/login', methods=['GET', 'POST'])
    def login():
        msg = ''
        if request.method == "POST" and 'email' in request.form and 'senha' in request.form:
            email = request.form['email']
            senha_form = request.form['senha']

            usuario = Login.get_email(email)

            if usuario and check_password_hash(usuario['senha'], senha_form):
                session['loggedin'] = True
                session['id'] = usuario['id']
                session['nome'] = usuario['nome']
                return redirect(url_for('home'))
            else:
                msg = 'E-mail ou senha incorretos'
        return render_template('login.html', msg=msg)
    
    #Rota de Logout - Remove os dados da sessão (session)
    @app.route('/logout')
    def logout():
        session.pop('loggedin', None)
        session.pop('id', None)
        session.pop('nome', None)
        return redirect(url_for('login'))
    
    #Rota de registro - Formulário de cadastro de usuário
    @app.route('/registro', methods=['GET', 'POST'])
    def registro():
        msg = ''
        if request.method == 'POST' and 'nome' in request.form and 'senha' in request.form and 'email' in request.form:
            nome = request.form['nome']
            senha = request.form['senha']
            email = request.form['email']
            #Utiliza a Models para verificar se já existe uma conta
            conta_existente = Login.get_email(email)
            if conta_existente:
                msg = 'Já existe uma conta com este e-mail!'
            elif not nome.isalnum():
                msg = 'O nome do usuário deve conter apenas letras e números'
            elif not nome or not senha or not email:
                msg = 'Por favor, preencha todos os campos!'
            else:
                try:
                    #Valida o e-mail
                    valid = validate_email(email)
                    email_normalizado = valid.email

                    Login.criar_login_usuario(nome, email_normalizado, senha)
                    flash('Você foi registrado com sucesso! Faça o Login')
                    return redirect(url_for('login'))
                except EmailNotValidError:
                    msg = 'Endereço de e-mail inválido'
        elif request.method == 'POST':
            msg = 'Por favor, preencha o formulário!'
        return render_template('registro.html', msg=msg)
    
    #Rota da Página inicial (Protegida)
    @app.route('/home')
    def home():
        if 'loggedin' in session:
            return render_template('home.html', nome = session['nome'])
        return redirect(url_for('login'))
    
    #Rota do Perfil do Usuário (Protegida)
    @app.route('/perfil')
    def perfil():
        if 'loggedin' in session:
            usuario = Login.get_id(session['id'])
            return render_template('perfil.html', usuario=usuario)
        return redirect(url_for('login'))
