 async function mostrar_carrinho()
{
    const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho")
    if (!resposta.ok) {
        alert ("ERRO AO CARREGAR CARRINHO!")
    

    }
    else{
        const dados = await resposta.json()
        const carrinho = document.getElementById()
        carrinho.innerHTML = "";
        let total = 0;

        for (let dado of dados){
            total = total + dado.preco
            let linha = `
            teste
  <div id="cartSidebar" class="cart-sidebar">
  <div class="cart-header">
    <h2>Carrinho</h2>
    <button id="closeCart">✖</button>
  </div>

  <ul id="cartItems"></ul>

  <div class="cart-footer">
    <p>Total: R$ <span id="total">z</span></p>
  </div>
</div>

<button onclick="addItem('Produto A', 29.90)">Adicionar Produto A</button>
<button onclick="addItem('Produto B', 49.90)">Adicionar Produto B</button>


`
carrinho.innerHTML += linha

       }
document.querySelector(".cart-item__price").textContent = "R$" + total
    }
}
