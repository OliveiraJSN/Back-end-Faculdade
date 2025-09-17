from flask import Flask, render_template, request, redirect
# --- pip install flask-sqlalchemy ------
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, template_folder='templates')

# Ajuste da configuração do banco de dados
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///meuDB.db'
db = SQLAlchemy(app)

class Tarefas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    descricao = db.Column(db.String(100), unique=True, nullable=False)
    
# Rota principal
@app.route('/')
def index():
    # Recupera todas as tarefas do banco de dados
    tarefas = Tarefas.query.all()
    return render_template('index.html', tarefas=tarefas)

#CRUD - CREATE
@app.route('/criar', methods=['POST'])
def criar_tarefas():
    descricao = request.form['descricao']

    #treco abaixo valida se a tarefa já foi cadastrada
    tarefa_existente = Tarefas.query.filter_by(descricao=descricao).first
    if tarefa_existente:
        return 'Erro: Tareaf já foi cadastrada!', 400
    #Criando uma nova instância
    new_task = Tarefas(descricao=descricao)
    db.session.add(new_task)
    db.session.commit()
    return redirect('/')

    

#'/deletar/<int:id_tarefa>': Esta é uma rota dinâmica
#<...>: Indica que esta parte da 

#CRUD - DELETE
@app.route('/deletar/<int:id_tarefa>', methods=['POST'])
def deletar_tarefas(id_tarefa):
    tarefa = Tarefas.query.get(id_tarefa)
    if tarefa:
        db.session.delete(tarefa)
        db.session.commit()
    return redirect('/')

#CRUP - UPTADE
@app.route('/atualizar/<int:id_tarefa>', methods=['POST'])
def atualizar_tarefas(id_tarefa):
    tarefa = Tarefas.query.get(id_tarefa)
    if tarefa:
        tarefa.descricao = request.form['descricao']
        db.session.commit()
    return redirect('/')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)