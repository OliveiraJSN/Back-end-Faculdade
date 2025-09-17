# Dexenvolvimento Back-end aula 04

# ----------------------------

#### O que é API



* APIs são interfaces que desempenham um papel de conectividade e interação entre diferentes sistemas e aplicações
* APIs operam por meio de requisições HTTP, o mesmo protocolo utilizado para carregar páginas da web;
* O protocolo HTTP permite a comunicação entre máquinas diferentes (cliente-servidor)
* O uso do protocolo HTTP garante uma comunicação uniforme e amplamente aceita, esta fato contribui para aplicações flexíveis e escaláveis



#### Existem diversos tipos de APIs, como:

1. SOAP
2. XML RPC
3. GRAPHQL
4. JSON RPC
5. WEBSOCKETS
6. API REST
7. API RESTFULL





#### MÉTODOS HTTP

GET: Obtenção de dados;

POST: Envio de dados (novo cadastro);

PUT: Atualizar dados;
DELETE: Exclusão de um registro no servidor





#### STATUS CODE

Código padronizado para comunicar ao cliente o statuso de requisição HTTP



Status code mais conhecidos

200: sucesso;

201: cadastro realizado com sucesso





#### JSON

Um mode de transportar dados na web (cliente-servidos);

Sua sintaxe é derivada de objetos JavaScript. Em Python isso corresponde a um dicionário



{

 	"nome": "João Oliveira"

 	"profissão": "Engenheiro de Software"

}



Utiliza somete aspas duplas;

não possil comentários;

--7



#### O que é uma rest API?

REST é um conjunto de restrições para criação de APIs, ou seja, é um estido de arquitetura e não uma tecnologia;

Criar e utilizar de forma intencional o que o protocolo HTTP nos fornce, como

*  	Status code
*  	Métodos HTTP
*  	Rotas

Utiliza de forma padronizada o protocolo HTTP para criar suas respectivas APIs



#### API RESTfull

Nivel 1 - Inicio: Todas as operações são enviadas para um único endpoint. Normalmente utiliza-se somente o POST para todas as ações do CRUD;

Nivel 2 - Recursos: Em vez de um único endpoint, a API expões URls distinto para cada recurso lógico (ex:/livros, /autores);

Nivel 3 - Métodos HTTP: As ações são mapeadas diretamente aos métodos GET, POST, PUT e DELETE e aos status code;

Nivel 4 - API navegável: As respostas da API incluem links que informam ao cliente quais são as próximas ações possíveis.





#### API - CARACTERÍSTICAS

utilização de endpoints (Rotas)

Use de métodos HTTP para ações

Comunicação sem interface gráfica

* O Código não gera telas, botões ou formulários HTML;
* Recebe uma requisição, processa e deveolve uma resposta com dados;

Troca de dados via formato JSON

Separação de responsabilidades







**pip instal api flask (instalar biblioteca para API no flask)**

