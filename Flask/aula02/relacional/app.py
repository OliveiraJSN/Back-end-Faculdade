from flask import Flask, render_template, request, url_for, redirect, flash
import mysql.connector
import secrets

app = Flask(__name__, template_folder='templates', static_folder='static')

#A secret_key é uma chave secreta usada para:
# - Garantir segurança em operações que dependem de sessões

app.secret_key = secrets.token_hex(32)

#Configuração de conexão
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Neto0302*',
    'database': 'crud'
}

#CRUD - READ
@app.route('/')
def home():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM crud.users")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('home.html', dados=data)

#CRUD - CREATE
@app.route('/add', methods=['GET', 'POST'])
def addUsuario():
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        cidade = request.form['cidade']

        #conexão ao BD
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = 'INSERT INTO crud.users (nome, idade, cidade) VALUES (%s, %s, %s)'
        cursor.execute(query, (nome, idade, cidade))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Usuario cadastrado com sucesso!", "success")
        return redirect(url_for("home"))
    return render_template('add.html')

#CRUD - UPDATE
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def editUsuarios(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    
    if request.method == 'POST':
        nome = request.form['nome']
        idade = request.form['idade']
        cidade = request.form['cidade']

        #Executa a atualização
        query = "UPDATE crud.users SET nome = %s, idade = %s, cidade = %s WHERE id = %s"
        cursor.execute(query, (nome, idade, cidade, id))
        conn.commit()
        cursor.close()
        flash('Usuario atualizado com sucesso', 'success')
        return redirect(url_for("home"))
    
    #Carregar dados para edição (GET)
    select_query = "SELECT * FROM crud.users WHERE id = %s"
    cursor.execute(select_query, (id,))
    user = cursor.fetchone()
    return render_template('edit.html', infos=user)



#CRUD - DELETE
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def deleteUsuarios(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    #Executa a deleção de regristros
    delete_query = "DELETE FROM crud.users WHERE id = %s"
    cursor.execute(delete_query, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash("Usuario deletado com sucesso!", 'success')
    return redirect(url_for("home"))


if __name__ == '__main__':
    app.run(debug=True)

#conn = mysql.connector.connect(**db_config): Estabelece a conexão com o BD MySQL. O parâmetro **db_config desempacota o direcionario passando seus 

#data = cursor.fechall(): busca todos os registros da consulta executada e os armazenam na variàvel data.