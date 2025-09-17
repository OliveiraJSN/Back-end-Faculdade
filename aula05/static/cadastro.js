const API_URL = "http://127.0.0.1:5000/livros";

//função para listar os livros
async function carregarLivros(){
    const resp = await fetch(API_URL);
    const livros = await resp.json();

    const lista = document.getElementById("livros-lista");
    lista.innerHTML = "";
    livros.forEch(livro => {
        const li = document.createElement("li");
        li.textContent = `${livro.titulo} - ${livro.autor}`;
        lista.appendChild(li);
    });
}

//função para cadastrar livros
document.getElementById('form-livro').addEventListener("submit", async (e) => { e.preventDefault()
    const titulo = document.getElementById("titulo").value;
    const autor = document.getElementById("autor").value;

    await fetch(API_URL, {
        method: "POST",
        header: { "Content-Type": "application/json"},
        body: JSON.stringify({ titulo, autor})
    });

    document.getElementById("form-livro").rest();
    carregarLivros();
})