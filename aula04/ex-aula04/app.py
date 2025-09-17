from flask import Flask, request, redirect
import mysql.connector
import secrets
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

#declara banco de dados
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Neto0302*',
    'database': 'ex_backend'
}

#
service = Service("C:\\Users\\camil\\OneDrive Joao\\OneDrive\\Estudos\\Faculdade\\4º Periodo\\Desenvolvimento Back-End\\aula04\\msedgedriver.exe")

edge_options = Options()
edge_options.add_argument("--start-maximized")

navegador = webdriver.Edge(service=service, options=edge_options)
navegador.get('https://books.toscrape.com/')

time.sleep(3)

livros = []

# pega todos os artigos (cada artigo = 1 livro)
artigos = navegador.find_elements(By.TAG_NAME, "article")

for artigo in artigos:
    nome_livro = artigo.find_element(By.TAG_NAME, "h3").find_element(By.TAG_NAME, "a").get_attribute("title")
    valor = artigo.find_element(By.CLASS_NAME, "price_color").text
    estoque = artigo.find_element(By.CLASS_NAME, "instock.availability").text
    
    livro = [nome_livro, valor, estoque]
    livros.append(livro)


conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

for livro in livros:  # percorre cada [nome, valor, estoque]
    query = 'INSERT INTO ex_backend.livros (nome_livro, valor, estoque) VALUES (%s, %s, %s)'
    cursor.execute(query, (livro[0], livro[1], livro[2]))

conn.commit()
cursor.close()
conn.close()


navegador.quit()