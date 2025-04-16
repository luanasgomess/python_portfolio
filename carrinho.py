carrinho_compras = {}

def adicionar_produto(produto, preco):
    carrinho_compras[produto] = preco

def total_carrinho_compras():
    return sum(carrinho_compras.values())

adicionar_produto("Camiseta", 50)
adicionar_produto("Tênis", 120)
adicionar_produto("Meias", 30)
adicionar_produto("Bolsa", 150)
adicionar_produto("Mochila", 200)
adicionar_produto("Calça jeans", 100)

print(f"Total: R${total_carrinho_compras()}")