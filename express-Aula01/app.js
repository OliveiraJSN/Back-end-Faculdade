const express = require("express");

//Iniciando o framework express
const app = express();

/*
Método GET é utilizando quando um cliente (navegador) que obter dados de um servidor.

req (Request): Objeto que contem as infors sobre a requisição que chegou ao cliente

res (Response): Objeto que representa a resposta que o servidor vai enviar de volta ao cliente

res.send(): Instrui o servidor a enviar uma resposta
*/
app.get("/", function(req, res){
  res.send("<h1>Ola Mundo!</h1>");
})

//Inicnado Servidor 
app.listen(3000, function(){
  console.log(`Servidor está funcionando!`);
})

