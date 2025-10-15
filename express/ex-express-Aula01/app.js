const express = require("express");
const path = require("path");
const app = express();
const port = 3000;

app.set('view engine', 'ejs');

app.set('views', path.join(__dirname, 'views'));

app.use(express.static(path.join(__dirname, 'public')));

const produtos = [
  {id: 1, nome: "Camiseta Preta", preco: "25.00"},
  {id: 2, nome: "Camiseta Branca", preco: "25.00"},
  {id: 3, nome: "Bermuda Azul", preco: "29.90"},
  {id: 4, nome: "Calça Jeans", preco: "89.90"},
];

app.get('/', (req, res) => {
  res.render('index', {produtos: produtos})
});

app.listen(port, () =>{
  const url = `https://localhost:${port}`;
  console.log(`Servidor rodando!`);

  (async () => {
    try{
      const openModule = await import('open');
      await openModule.default(url);
    } catch(error){
      console.error(`Erro ao tentar abrir o navegador:`, error);
    }
  })();
});