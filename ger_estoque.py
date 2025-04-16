estoque = {}

def adicionar_item():
    nome = input("Nome do item: ")
    quantidade = int(input("Quantidade: "))
    preco = float(input("Preço unitário: "))
    estoque[nome] = {"quantidade": quantidade, "preco": preco}
    print("Item adicionado com sucesso.")

def mostrar_estoque():
    if not estoque:
        print("Estoque vazio.")
    else:
        for item, info in estoque.items():
            print(f"{item} - {info['quantidade']} unidades - R${info['preco']:.2f} cada")

def remover_item():
    nome = input("Nome do item a remover: ")
    if nome in estoque:
        del estoque[nome]
        print("Item removido.")
    else:
        print("Item não encontrado.")

while True:
    print("\n--- Menu Estoque ---")
    print("1 - Adicionar item")
    print("2 - Mostrar estoque")
    print("3 - Remover item")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_item()
    elif opcao == "2":
        mostrar_estoque()
    elif opcao == "3":
        remover_item()
    elif opcao == "0":
        print("Encerrando...")
        break
    else:
        print("Opção inválida.")