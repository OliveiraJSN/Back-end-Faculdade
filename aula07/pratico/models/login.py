import mysql.connector
#Função para criar um hash (criptografia) segura para senhas
from werkzeug.security import generate_password_hash
from config import Config

def inicia_bd():
    try:
        conn = mysql.connector.connect(**Config.DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        print(f"Erro de conexão com o BD {err}")
        return None;
    
class Login:
    @staticmethod
    def get_email(email):
        conn = inicia_bd()
        if conn: #Cria conexão com o BD
            cursor = conn.cursor(disctionary=True) #dictonary traz no formato ex: "email: joao@gmail.com" se não fiz retorno só "joao@gamil.com"
            curosr.execute('SELECT * FROM login_usuarios.usuarios WHERE email = %s', (email,)) #tem que colocar virgula no final
            usuario = cursor.fetchone() #apenas um envio por vez no bando de dados
            cursor.close()
            conn.close()
            return usuario
        
    
    @staticmethod
    def get_id(user_id):
        conn = inicia_bd()
        if conn: #Cria conexão com o BD
            cursor = conn.cursor(disctionary=True) #dictonary traz no formato ex: "Nome: João" se não fiz retorno só "João"
            curosr.execute('SELECT * FROM login_usuarios.usuarios WHERE id = %s', (user_id,)) #tem que colocar virgula no final
            usuario = cursor.fetchone() #apenas um envio por vez no bando de dados
            cursor.close()
            conn.close()
            return usuario

    
    @staticmethod
    def criar_login_usuario(nome, email, senha):
        conn = inicia_bd()
        if conn:
            hash_senha = generate_password_hash(senha)
            cursor = conn.cursor()
            cursor.execute('INSERT INTO login_usuarios.usuarios (nome, email, senha) VALUES (%s, %s, %s)', (nome, email, hash_senha)) #cursor.execute envia ao bando de dados as informações
            conn.commit() #confirma o envio
            curosr.close()
            conn.close()
