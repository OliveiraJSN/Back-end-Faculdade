const express = require('express'); //Bibliotecas
const mysql = require('mysql2');

const app = express();
const port = 3000;

app.use(express.urlencoded({ extended : true }));
//app.use(express.json()); possivel ser utilizado também

//caminhos das pastas
app.set('view engine', 'ejs');

app.use(express.static('public')); //lado do cliente, CSS e JavaScript do lado do cliente

const pool = mysql.createPool({ //conexão com o BD
  connectionLimit: 10, //quantidade limitada de acessos ao site
  host: 'localhost',
  user: 'root',
  password: 'Neto0302*',
  database: 'crud_express_mysql'
});

console.log(`Pool de conexões com o MySQL realizada com sucesso!`)

// ----------- ROTA PRINCIPAL - SELECT (READ) -------------------------

app.get('/', (req, res) => {
  const sql = 'SELECT * FROM crud_express_mysql.produtos';
  pool.query(sql, (erro, dadosTabela) => {
    if (erro){
      console.error('Erro na query SELECT:', erro);
      return res.status(500).send('Erro ao buscar produtos');
    }
    res.render('produtos', { produtos: dadosTabela });
  });
});


// ------------------- ROTA PARA ADICIONAR PRODUTO - INSERT - (CREATE) --------------------------
//req.body: É o objeto que contém os dados enviados pelo formulario
//O app.use(express.urlencoded({ ..... })); "traduzem" os dados do formulário e preenchem o req.body

app.post('/adicionar', (req, res) =>{
  const {nome, preco, descricao} = req.body;
  const sql = 'INSERT INTO crud_express_mysql.produtos (nome, preco, descricao) VALUES (?, ?, ?)'
  pool.query(sql, [nome, preco, descricao], (erro, retorno) => {
    if (erro){
      console.error('Erro na query SELECT:', erro);
      return res.status(500).send('Erro ao adicionar um produto');
    }
    console.log('Produto adicionado com sucesso!');
    res.redirect('/');
  });
});


// ------------------- ROTA PARA EXIBIT O FORMULARIO DE EDIÇÃO - UPDATE - PARTE 1----------------
app.get('/editar/:id', (req, res) =>{
  const { id } = req.params; //pega os dados da url
  const sql = 'SELECT * FROM crud_express_mysql.produtos WHERE id = ?';
  pool.query(sql, [id], (erro, dadosTabela) => {
    if (erro){
      console.error('Erro na query SELECT:', erro);
      return res.status(500).send('Erro ao buscar um produto para edição.');
    }
    if(dadosTabela.length === 0){
      return res.status(404).send('Produto não encontrado');
    }
    res.render('edit_produtos', { produto: dadosTabela});
  });
});

// ------------------- ROTA PARA EXIBIR O FORMULARIO DE EDIÇÃO - UPDATE - PARTE 2----------------
app.post('/atualizar/:id', (req, res) =>{
  const { id } = req.params;
  const {nome, preco, descricao} = req.body;
  const sql = 'UPDATE crud_express_mysql.produtos SET nome = ?, preco = ?, descricao = ? WHERE id = ?';
  pool.query(sql, [nome, preco, descricao, id], (erro, dadosTabela) =>{
    if (erro){
      console.error('Erro na query UPDATE:', erro);
      return res.status(500).send('Erro ao atulizar um produto.');
    }
    console.log("Produto atualizado com sucesso!");
    res.redirect('/');
  });
});

// ----------------------------- ROTA PARA DELETAR - DELETE--------------------
app.post('/deletar/:id', (req, res) =>{
  const { id } = req.params;
  const sql = 'DELETE FROM crud_express_mysql.produtos WHERE id = ?'
  pool.query(sql, [id], (erro, retorno) =>{
    if (erro){
      console.error('Erro na query DELETE:', erro);
      return res.status(500).send('Erro ao deletar um produto.');
    }
    console.log('Produto deletado com sucesso!');
    res.redirect('/');
  })
});


// --------------------------  INICIANDO SERVIDOR ----------------------------------
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
      console.error(`Erro ao tentar abrir o navegador:`, error);
    }
  })();
});