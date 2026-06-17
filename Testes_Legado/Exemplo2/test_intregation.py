from Exemplo2.app import Produto, Estoque

def test_adicionar_verificar_quantidade():
    estoque = Estoque()

    produto1 = Produto("Mouse",10)
    produto2 = Produto("Teclado",5)

    estoque.adicionar_produto(produto1)
    estoque.adicionar_produto(produto2)