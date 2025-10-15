from flask import Flask, render_template, request, url_for, redirect, flash
import mysql.connector
import secrets

app = Flask(__name__, template_folder='templates', static_folder='static')

app.secret_key = secrets.token_hex(32)

#conexão com banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Neto0302*',
    'database': 'clinicamedica'
}

#CRUD - READ
@app.route('/')
def home():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM clinicamedica.consultas")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('home.html', dados=data)


#CRUD - CREATE
@app.route('/cadastrar', methods=['GET', 'POST'])
def cadastrarConsulta():
    if request.method == 'POST':
        nome_paciente = request.form['nome_paciente']
        nome_medico = request.form['nome_medico']
        especialidade = request.form['especialidade']
        data_consulta = request.form['data_consulta']

        #conexão com o BD
        conn = mysql.connector.connect(**db_config)
        cursor = conn.cursor()
        query = 'INSERT INTO clinicamedica.consultas (nome_paciente, nome_medico, especialidade, data_consulta) VALUES (%s, %s, %s, %s)'
        cursor.execute(query, (nome_paciente, nome_medico, especialidade, data_consulta))
        conn.commit()
        cursor.close()  
        conn.close()
        flash("Consulta cadastrada com sucesso!", "success")
        return redirect(url_for("home"))
    return render_template("add.html")

#CRUS - UPDATE
@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editarConsultas(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    if request.method == 'POST':
        nome_paciente = request.form['nome_paciente']
        nome_medico = request.form['nome_medico']
        especialidade = request.form['especialidade']
        data_consulta = request.form['data_consulta']

        #Executa a atualização
        qury = "UPTADE clinicamedica.consultas SET nome_paciente = %s, nome_medico = %s, especialidade = %s, data_consulta = %s WHERE id = %s"
        cursor.execute(query, (nome_paciente, nome_medico, especialidade, data_consulta, id))
        conn.commit()
        cursor.close()
        flash("Consulta editada com sucesso", "success")
        return redirect(url_for("home"))
    
    #Carregar dados para edição (GET)
    select_query = "SELECT * FROM clinicamedica.consultas WHERE id = %s"
    cursor.execute(select_query, (id,))
    user = cursor.fetchone()
    return render_template('edit.html', infos=user)


#CRUD - DELETE
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def deleteConsultas(id):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)

    #Executa a deleção de regristros
    delete_query = "DELETE FROM clinicamedica.consultas WHERE id = %s"
    cursor.execute(delete_query, (id,))
    conn.commit()
    cursor.close()
    conn.close()
    flash("Consulta deletada com sucesso!", "success")
    return redirect(url_for("home"))

if __name__ == '__main__':
    app.run(debug=True)