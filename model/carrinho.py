from database.conexao import criar_conexao 

def recuperar_carrinho(usuario:str) -> list:
    conexao, cursor = criar_conexao()
    cursor.execute ("""
                    SELECT carrinhos.cod_carrinho,
                    carrinhos.usuario,carrinhos.data,carrinhos.finalizado,
                    itens.produto,
                    itens_carrinho.quantidade,
                    itens.preco, 
                    itens.url_imagem
                    FROM carrinhos 
                    INNER JOIN itens_carrinho ON carrinhos.cod_carrinhos = itens_carrinho.cod_carrinho
                    INNER JOIN itens ON itens.codigo = itens_carrinho.cod_produto
                    WHERE carrinhos.usuario = %s;

                    """, [usuario])
    resultado = cursor.fetchall()
    conexao.close()
    return resultado
