import mysql.connector
#Importa as configurações do BD da config.py
from config import db_config 

def inicia_bd():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Erro de conexão com o BD: {err}")
        return None
    
#Modelo para representar um usuário.
class User:
    @staticmethod
    def get_usuarios():
        users = []
        conn = inicia_bd()
        if conn:
            cursor = conn.cursor(dictionary=True)
            try:
                cursor.execute("SELECT * FROM bd_mvc.users")
                users = cursor.fetchall()
            except mysql.connector.Error as err:
                print(f"Erro ao buscar usuários: {err}")
            finally:
                cursor.close()
                conn.close()
        return users
    
    #Criar um novo usuário no BD
    @staticmethod
    def criar_usuario(name, email):
        conn = inicia_bd()
        if conn:
            cursor = conn.cursor()
            try:
                query = "INSERT INTO bd_mvc.users (name, email) VALUES (%s, %s)"
                cursor.execute(query, (name, email))
                conn.commit()
            except mysql.connector.Error as err:
                print(f"Erro ao criar um usuário: {err}")
                conn.rollback() #Desfaz a transação em caso de erro
            finally:
                cursor.close()
                conn.close()