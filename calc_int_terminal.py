def menu():
    print("\nCalculadora Interativa")
    print("1 - Adição")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")

def calcular(op, a, b):
    if op == 1:
        return a + b
    elif op == 2:
        return a - b
    elif op == 3:
        return a * b
    elif op == 4:
        return a / b if b != 0 else "Erro: Divisão por zero"

while True:
    menu()
    opcao = int(input("Escolha uma opção: "))
    if opcao == 0:
        print("Saindo...")
        break
    if opcao in [1, 2, 3, 4]:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = calcular(opcao, num1, num2)
        print("Resultado:", resultado)
    else:
        print("Opção inválida.")