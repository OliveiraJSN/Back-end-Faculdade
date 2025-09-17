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

db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'Neto0302*',
    'database': 'valete'
}

service = Service("C:\\Users\\camil\\OneDrive Joao\\OneDrive\\Estudos\\Faculdade\\4º Periodo\\Desenvolvimento Back-End\\aula04\\msedgedriver.exe")

edge_options = Options()
edge_options.add_argument("--start-maximized")

navegador = webdriver.Edge(service=service, options=edge_options)
navegador.get('https://app.valete.org.br/')

time.sleep(2)

#entrar
campo_email = navegador.find_element(By.XPATH, '//input[contains(@placeholder, "E-mail")]')
campo_email.click()
time.sleep(2)
campo_email.send_keys("joao_osneto@hotmail.com")

campo_senha = navegador.find_element(By.XPATH, '//input[contains(@placeholder, "Senha")]')
campo_senha.click()
time.sleep(2)
campo_senha.send_keys("Neto0302")

clicar_botao = navegador.find_element(By.CLASS_NAME, "transition")
time.sleep(1)
clicar_botao.click()

time.sleep(5)

print("\n ----- Você logou com sucesso -----\n")

catalogos = []

categorias = navegador.find_elements(By.CLASS_NAME, "-mx-6")

for categoria in categorias:
    try:
        nome_podcast = categoria.find_element(By.TAG_NAME, "a").text
        
    except:
        continue

print(catalogos)

    # catalago = [nome_podcast]
    # catalogos.append(catalogo)

# print(catalogos)