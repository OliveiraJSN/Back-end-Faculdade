#import requests
#from bs4 import BeautifulSoup
#res = requests.get('https://clube.valete.org.br') #faz a request do site
# print(res.status_code) #mostra o status da request
# print('\n') #espaço
# print(res.headers) #mostra o cabeçalho
# print('\n') #espaço
# print(res.content) #mostra o conteudo da pagina
#site = BeautifulSoup(res.text, 'html.parser') #variavel site recebe BeautifulSoup(res (site))
#print(site.prettify()) #deixa mais 'bonito'

from selenium import webdriver
from selenium.webdriver.edge.service import Service #esse vai ser o objeto que vai ter o arquivo executavel
from selenium.webdriver.edge.options import Options # opções de personalização na vizualização
from selenium.webdriver.common.by import By #acessar as tags do HTML
import time # coloca um timer para interagir com a pagina
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait #espera inteligente
from selenium.webdriver.support import expected_conditions as EC #EC apelido

#caminho para a pasta
service = Service('C:\\Users\\camil\\OneDrive Joao\\OneDrive\\Estudos\\Faculdade\\4º Periodo\\Desenvolvimento Back-End\\aula04\\msedgedriver.exe') #endereço do executavel baixado dentro da sua pasta

#Tem-se a possiblidade de setar o tamanho da janela do navegador
edge_options = Options()
#edge_options.add_argument("--window-size=800.800") abre a janela em janela 800 x 800
edge_options.add_argument("--start-maximized") #inicia a pagina maximizada na tela

#Informar o site
navegador = webdriver.Edge(service=service, options=edge_options) #variavel navegador recebe qual navegador será utlizado
navegador.get('https://www.airbnb.com.br/')
time.sleep(5)

try:
    #Maneira mais avançada botao_aceitar = WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Aceitar todos"]')))#espera 10 segundos até aparecer um elemento clicavel
    #clique no botão
    botao_aceitar = navegador.find_element(By.XPATH, '//button[contains(text(), "Aceitar todos")]')
    botao_aceitar.click()
    print("Botão 'Aceitar todos' clicado com sucesso!")

except Exception as e:
    print(f"Não foi possivel encontrar ou clicar no botão: {e}")


campo_input = navegador.find_element(By.XPATH, '//input[contains(@placeholder, "Buscar destinos")]')
campo_input.click()

    
time.sleep(3) #numero em segundos 
campo_input.send_keys("São Paulo")
campo_input.send_keys(Keys.ENTER)

input("Pressione ENTER, no terminal, para encerrar")
navegador.quit()