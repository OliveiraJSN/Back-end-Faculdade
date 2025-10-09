const express = require("express");
const path = require("path");
const app = express();
const port = 3000;

// ------------- Configuração do Express ------------

// Define o ejs como o templete
app.set('view engine', 'ejs');


// Aponta a localização exata da pasta views
app.set('views', path.join(__dirname, 'views'));


app.use(express.static(path.join(__dirname, 'public')));

// ------------------ Banco de dados - Simulado ---------

const usuarios = [
  {id: 1, nome: "Juliana Silva", email: "ju.silva@gmail.com"},
  {id: 2, nome: "João Oliveira", email: "jo.osneto@gmail.com"},
  {id: 3, nome: "Tiago Carvalho", email: "tiago.carvalho@gmail.com"},
];

// --------------------------- ROTAS ------------------------
// Rota principal que ira renderizar nossa index.ejs
app.get('/', (req, res) =>{
  res.render('index', {usuarios: usuarios})
});

// --------------------------- SERVIDOR --------------------
app.listen(port, () =>{
  const url = `https://localhost:${port}`;
  console.log(`Servidor rodando!`);

  (async () => {
    try{ 
      /*
      O 1º await "diz": PARA A EXECUÇÃO DESTA FUNÇÃO ASYNC até que o import('open') seja carregado.
      import('open') é uma importação dinâmica, ou seja diferente de const open = require('open') que é estático
      */
      const openModule = await import('open');
      //O 2º await PARA A EXECUÇÃO DA FUNÇÃO ASYNC NOVAMENTE! até que a função de abrir o navegador termine.
      await openModule.default(url);
    } catch(error){
      console.error(`Erro ao tentat abrir o navegador:`, error);
    }
  })();
});

// Crie uma pagina de uma loja virtual aonde deve ser apresentada uma lista de produtos com seus respectivos preços

// Formate os valores dos produtos em reais por meio de uma função.