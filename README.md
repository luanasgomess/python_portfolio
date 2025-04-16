# Carrinho de compras simples (Python puro)

Este é um projeto básico em Python que simula um carrinho de compras, permitindo adicionar produtos e calcular o valor total da compra.

## Funcionalidades

Adicionar produtos ao carrinho com seus respectivos preços Calcular o valor total da compra com base nos produtos adicionados

## Como usar
Calcula o valor total de cada item




# Calculadora Interativa (Python puro)

Uma calculadora simples de terminal, feita apenas com Python. Permite ao usuário realizar operações básicas: adição, subtração, multiplicação e divisão.

## Funcionalidades

- Interface interativa no terminal
- Operações matemáticas básicas
- Tratamento de divisão por zero

## Como usar

Execute o arquivo `calculadora.py` com Python 3 instalado.




# Sistema de Login (Python puro)

Login simples via terminal, utilizando Python puro. Os usuários e senhas são armazenados em um arquivo `.txt`.

## Funcionalidades

- Login com verificação de credenciais
- Armazenamento local de usuários no arquivo `usuarios.txt`

## Como usar

Crie um arquivo `usuarios.txt` com o seguinte formato:
usuario1:senha1
usuario2:senha2




# Gerenciador de Estoque (Python puro)

Gerenciador de estoque simples feito em Python puro, utilizando um arquivo `.txt` (JSON) para persistência dos dados.

## Funcionalidades

- Adicionar, exibir e remover produtos do estoque
- Dados salvos automaticamente em `estoque.txt`
- Interface via terminal

## Como usar

Basta executar `estoque.py`. O arquivo `estoque.txt` será criado automaticamente.

Os dados são armazenados em formato JSON, como no exemplo:
```json
{
  "Caneta": {"quantidade": 10, "preco": 1.5},
  "Caderno": {"quantidade": 5, "preco": 10.0}
}

