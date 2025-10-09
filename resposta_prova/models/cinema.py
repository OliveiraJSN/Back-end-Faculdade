import mysql.connector
from config import db_config

def conexao():
    try:
        conn = mysql.connector.connect(**db_config)
        return conn
    except mysql.connector.Error as err:
        print(f"Erro ao conectar ao BD: {err}")
        return None


class Cinema:

  @staticmethod
  def get_all():
    filmes = []
    conn = conexao()
    if conn:
      cursor = conn.cursor(dictionary=True)
      query = "SELECT * FROM cinema.cinema_ingressos"
      cursor.execute(query)
      filmes = cursor.fetchall()
      cursor.close()
      conn.close()
    return filmes

  @staticmethod
  def get_by_id(id):
      conn = conexao()
      if conn:
          cursor = conn.cursor(dictionary=True)
          query = "SELECT * from cinema.cinema_ingressos WHERE id = %s"
          values = (id,)
          cursor.execute(query, values)
          user = cursor.fetchone()
          cursor.close()
          conn.close()
          return user
      return None      
      

  # CREATE
  @staticmethod
  def create(nome_filme, genero, sessoes, nome_cliente, assento, data_filme):
      conn = conexao()
      if conn:
          cursor = conn.cursor()
          query = "INSERT INTO cinema.cinema_ingressos(nome_filme, genero, sessoes, nome_cliente, assento, data_filme) VALUES (%s, %s, %s, %s, %s, %s)"
          values = (nome_filme, genero, sessoes, nome_cliente, assento, data_filme)
          cursor.execute(query, values)
          conn.commit()
          cursor.close()
          conn.close()
          return True
      return False

  # UPDATE
  @staticmethod
  def update(nome_filme, genero, sessoes, nome_cliente, assento, data_filme, id):
      conn = conexao()
      if conn:
          cursor = conn.cursor()
          query = "UPDATE cinema.cinema_ingressos SET nome_filme=%s, genero=%s, sessoes=%s,nome_cliente=%s, assento=%s, data_filme=%s WHERE id=%s" 
          values = (nome_filme, genero, sessoes, nome_cliente, assento, data_filme, id)
          cursor.execute(query, values)
          conn.commit()
          cursor.close()
          conn.close()
          return True
      return False

  # DELETE
  @staticmethod
  def delete(id):
      conn = conexao()
      if conn:
          cursor = conn.cursor()
          query = "DELETE FROM cinema.cinema_ingressos WHERE id = %s"
          values = (id,)
          cursor.execute(query, values)
          conn.commit()
          cursor.close()
          conn.close()
          return True
      return False

