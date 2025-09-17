from apiflask import APIFlask, Schema, fields
from apiflask.validators import Length
import mysql.connector
from mysql.connector import errorcode
from flask import Flask, render_template, request, redirect, url_for

#Configurar bando de dados
db_config = { 
    'host': 'localhost',
    'user': 'root',
    'password': 'Neto0302*',
    'database': 'crud_api'
}

#Função para conctar ao servidor
def conexao():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao se conectar com o BD: {err}")
        return None
    
#Função para inicar o bando de dados e a tabela
def inicia_bd():
    try:
        conn = mysql.connector.connect(
            host = db_config['host'],
            user = db_config['user'],
            password = db_config['password']
        )
        cursor = conn.cursor()
        #Cria a database se ele não existir
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_config['database']} DEFAULT CHARACTER SET utf8mb4")
        print(f"Banco de dados '{db_config['database']}' criado")

        cursor.close()
        conn.close()

        conn = conexao()
        if conn:
            cursor = conn.cursor()
            query_table = """
                CREATE TABLE IF NOT EXISTS livros(
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    titulo VARCHAR(255) NOT NULL,
                    autor VARCHAR(255) NOT NULL
                )
            """

            cursor.execute(query_table)
            print("Tabela livros criada com sucesso!")
            conn.commit()
            cursor.close()
            conn.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_CHANGE_USER_ERROR:
            print("Erro - Verifique o nome de usuario e senha")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print(f"Erro: A database '{db_config['database']}' não existe")
        else:
            print(f"Ocorreu um erro ao se conectar ao bando de dados: {err}")
        exit(1) #Encerra a aplicação senão conseguir conextar


# ------------------------------ DEFINIÇÃO DOS SCHEMAS (MODELOS DE DADOS) ------------------------

#Proposito: Define como devem ser os dados que um cliente envia para a API para criar um novo livro
class LivroInSchema(Schema):
    titulo = fields.String(required=True, validate=Length(min=1))
    autor = fields.String(required=True, validate=Length(min=1))



#Propósito: Definir o formato dos dados que a api envia como resposta, seja ao criar um novo livrou ou ao listar livros existentes
class LivroOutSchema(Schema):
    id = fields.Integer()
    titulo = fields.String()
    autor = fields.String()


# --------------------------------------- INICIALIAÇÃO DA APLICAÇÃO APLIFLASK -------------------------------------------

app = APIFlask(__name__,title="API - Versão 01", template_folder='templates', static_folder='static')

@app.post('/livros')
@app.input(LivroInSchema) #Validação dos dados de entrada inseridos
@app.output(LivroOutSchema, status_code=201) #Define o formato da saida

def criar_livro(json_data):

    titulo = json_data['titulo']
    autor = json_data['autor']

    conn = conexao()
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = 'INSERT INTO crud_api.livros (titulo, autor) VALUES (%s, %s)'
        cursor.execute(query, (titulo, autor))

        novo_livros_id = cursor.lastrowid

        conn.commit()
        cursor.close()
        conn.close()

        livro_criado = {'id': novo_livros_id, 'titulo': titulo, 'autor': autor}
        return livro_criado

#ENDPOINT PARA LISTAR TODOS LIVROS (GET)
@app.get('/livros')
@app.output(LivroOutSchema(many=True)) #Indica que a saida é uma lista

def listar_livros():
    conn = conexao()
    if conn:
        cursor = conn.cursor(dictionary=True)
        query = "SELECT * FROM crud_api.livros"
        cursor.execute(query)
        livros = cursor.fetchall()
        cursor.close()
        conn.close()
        return livros


# -------------------- FRONT END ----------------
@app.route('/')
def index():
    listar_livros()
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM crud_api.livros")
    livros = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', livros=livros)

@app.route('/cadastro', methods=['GET', 'POST'])
def cadastro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        
        conn = conexao()
        cursor = conn.cursor()
        query = "INSERT INTO crud_api.livros (titulo, autor) VALUES (%s, %s)"
        cursor.execute(query, (titulo, autor))
        conn.commit()
        cursor.close()

        return redirect(url_for("index"))

    else:
        print("Erro ao abrir cadastro")

    return render_template('cadastro.html')

        
if __name__ == '__main__':
    inicia_bd()
    app.run(debug=True)

#Conecte ao backend desenvolvido (API) a um frontend simulando um cenário real de desenvilvimento
#Criar uma página HTML simples, que irá consumir sua API de livros. Está página permitirá:
# - Ver a lista de livros cadastrados
# - Adicionar um livro atrvés de um formulário