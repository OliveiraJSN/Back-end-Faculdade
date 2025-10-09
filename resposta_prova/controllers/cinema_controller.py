from flask import render_template, request, redirect, url_for, flash
from models.cinema import Cinema
from datetime import datetime

def configure_routes(app):
  @app.route('/')
  def index():
    filmes = Cinema.get_all()
    return render_template('index.html', filmes=filmes)

  @app.route('/add', methods = ['GET', 'POST'])
  def addUsuarios():
    if request.method == 'POST':
      nome_filme = request.form['nome_filme']
      genero = request.form['genero']
      sessoes = request.form['sessoes']
      nome_cliente = request.form['nome_cliente']
      assento = request.form['assento']
      data_filme = request.form['data_filme']

      Cinema.create(nome_filme, genero, sessoes, nome_cliente, assento, data_filme)
      return redirect(url_for('index'))

    return render_template('add.html')

  @app.route('/edit/<int:id>', methods = ['GET', 'POST'])
  def editarUsuarios(id):
    if request.method == 'POST':
      nome_filme = request.form['nome_filme']
      genero = request.form['genero'] 
      sessoes = request.form['sessoes']
      nome_cliente = request.form['nome_cliente']
      assento = request.form['assento']
      data_filme = request.form['data_filme']

      Cinema.update(nome_filme, genero, sessoes, nome_cliente, assento, data_filme, id)
      return redirect(url_for('index'))

    user = Cinema.get_by_id(id)
    if not user:
      flash("Usuário não encontrado!", 'error')
      return redirect(url_for('index'))

    return render_template('edit.html', infos=user)


  @app.route('/delete/<int:id>', methods = ['POST'])
  def deleteUsuarios(id):
    Cinema.delete(id)
    return redirect(url_for('index'))