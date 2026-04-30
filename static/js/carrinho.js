async function mostrar_carrinho() {
    try {
        const resposta = await fetch("http://10.110.134.2:8080/api/get/carrinho");

        if (!resposta.ok) {
            alert("ERRO AO CARREGAR CARRINHO!");
        }
        else{

        

        const carrinho = document.getElementById("carrinho")
        carrinho.innerHTML = "";
      
        let total = 0;

        for (let dado of dados) {
            total = total + dado.preco

            let linha = `
                teste
                <img src="${dado.imagem}" alt 
                <li class="cart-item">
                    <span>${dado.nome}</span>
                    <span>R$ ${preco.toFixed(2)}</span>
                </li>
            `;

            lista.innerHTML += item;
        }

        totalElemento.textContent = total.toFixed(2);

    } catch (erro) {
        console.error(erro);
        alert("Erro ao conectar com o servidor");
    }
}