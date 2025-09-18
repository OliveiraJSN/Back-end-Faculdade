import mysql.connector
# Função para criar um hash (criptografia) segura para senhas
from werkzeug.security import generate_password_hash
from config import Config

def inicia_bd():
    try:
        # Cria a conexão com o banco de dados usando as configurações do Config
        conn = mysql.connector.connect(**Config.DB_CONFIG)
        return conn
    except mysql.connector.Error as err:
        # Caso ocorra erro na conexão, exibe a mensagem
        print(f"Erro de conexão com o BD {err}")
        return None

class Login:
    @staticmethod
    def get_email(email):
        conn = inicia_bd()
        if conn:  # Cria conexão com o BD
            # dictionary=True traz o resultado no formato ex: {"email": "joao@gmail.com"}
            cursor = conn.cursor(dictionary=True)
            # Seleciona o usuário pelo e-mail
            cursor.execute(
                'SELECT * FROM login_usuarios.usuarios WHERE email = %s',
                (email,)
            )
            usuario = cursor.fetchone()  # Apenas um registro é retornado
            cursor.close()
            conn.close()
            return usuario

    @staticmethod
    def get_id(user_id):
        conn = inicia_bd()
        if conn:  # Cria conexão com o BD
            # dictionary=True traz o resultado no formato ex: {"Nome": "João"}
            cursor = conn.cursor(dictionary=True)
            # Seleciona o usuário pelo ID
            cursor.execute(
                'SELECT * FROM login_usuarios.usuarios WHERE id = %s',
                (user_id,)
            )
            usuario = cursor.fetchone()  # Apenas um registro é retornado
            cursor.close()
            conn.close()
            return usuario

    @staticmethod
    def criar_login_usuario(nome, email, senha):
        conn = inicia_bd()
        if conn:
            # Cria um hash seguro da senha antes de salvar
            hash_senha = generate_password_hash(senha)
            cursor = conn.cursor()
            # Insere o novo usuário no banco de dados
            cursor.execute(
                'INSERT INTO login_usuarios.usuarios (nome, email, senha) VALUES (%s, %s, %s)',
                (nome, email, hash_senha)
            )
            conn.commit()  # Confirma a inserção no banco de dados
            cursor.close()
            conn.close()
