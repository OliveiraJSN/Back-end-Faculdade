from flask import Flask, render_template, url_for, request, redirect, flash
import mysql.connector
import secrets

app = Flask(__name__, template_folder='templates', static_folder='static')

app.secret_key = secrets.token_hex(32)

db_config ={
    'host': 'localhost',
    'user': 'root',
    'password': 'fukuda',
    'database': 'cinema'
}

@app.route('/')
def home():
    conn = conexao()
    if not conn:
        return "Erro de conexão com o banco de dados."
    
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT *, DATE_FORMAT(data_filme, '%d/%m/%Y') as data_filme FROM cinema.cinema_ingressos ORDER BY data_filme ASC")
        data = cursor.fetchall()
        return render_template('home.html', dados=data)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/add', methods=['GET', 'POST'])
def addUsuarios():
    if request.method == 'POST':
        nome_filme = request.form['nome_filme']
        genero = request.form['genero']
        sessoes = request.form['sessoes']
        nome_cliente = request.form['nome_cliente']
        assento = request.form['assento']
        data_filme = request.form['data_filme']

        conn = conexao()
        if not conn:
            flash('Erro de conexão com o banco de dados.', 'error')
            return render_template('add.html') 
        
        try:
            cursor = conn.cursor()
            query = "INSERT INTO cinema.cinema_ingressos (nome_filme, genero, sessoes, nome_cliente, assento, data_filme) VALUES (%s, %s, %s, %s, %s, %s)"
            cursor.execute(query, (nome_filme, genero, sessoes, nome_cliente, assento, data_filme))
            conn.commit()
            flash('Usuário cadastrado com sucesso!', 'success')
            return redirect(url_for("home"))
        finally:
            if conn.is_connected():
                cursor.close()
                conn.close()
    return render_template('add.html')

@app.route('/edit/<float:id>', methods=['GET', 'POST'])
def editUsuarios():
    conn = conexao()
    if not conn:
        return "Erro de conexão com o banco de dados."

    try:
        cursor = conn.cursor(dictionary=True)
        if request.method == 'POST':
            nome_filme = request.form['nome_filme']
            genero = request.form['genero']
            sessoes = request.form['sessoes']
            nome_cliente = request.form['nome_cliente']
            assento = request.form['assento']
            data_filme = request.form['data_filme']

            query = "UPDATE cinema.cinema_ingressos SET nome_filme = %s, genero = %s, sessoes = %s, nome_cliente = %s, assento = %s, data_filme = %s WHERE id = %s"
            cursor.execute(query, (nome_filme, genero, sessoes, nome_cliente, assento, data_filme, id))
            conn.commit()
            flash('Usuário atualizado com sucesso!', 'success')
            return redirect(url_for("home"))
        
        select_query = "SELECT * FROM cinema.cinema_ingressos WHERE id = %s"
        cursor.execute(select_query, (id,))
        user = cursor.fetchone()
        if not user:
            flash('Usuário não encontrado!', 'error')
            return redirect(url_for('home'))
        return render_template('edit.html', infos=user)
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()

@app.route('/delete/<float:id>', methods=['GET', 'POST'])
def deleteUsuarios():
    conn = conexao()
    if not conn:
        return "Erro de conexão com o banco de dados."
    
    try:
        cursor = conn.cursor()
        delete_query = "DELETE FROM cinema.cinema_ingressos WHERE id = %s"
        cursor.execute(delete_query, (id,))
        conn.commit()
        flash('Usuário deletado com sucesso!', 'success')
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()       
    return redirect(url_for("home"))

