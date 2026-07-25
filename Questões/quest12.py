'''
Questão 12 — Sistema de Pedidos:

Implemente as classes Produto e Pedido para simular um sistema simples de compras.

1. Atributos das Classes

Produto:
    nome (string): Nome do produto.
    preco (float): Preço unitário.

Pedido:
    cliente (string): Nome do cliente.
    produtos (list): Lista de objetos Produto (deve iniciar vazia).

2. Métodos

Classe Produto:
    exibir_dados(): Exibe o nome e o preço do produto.

Classe Pedido:
    adicionar_produto(produto): Adiciona um objeto Produto ao pedido.
    remover_produto(nome): Remove do pedido o primeiro produto cujo nome corresponda ao informado. Caso não exista, exibe uma mensagem.
    calcular_total(): Retorna o valor total do pedido.
    listar_pedido(): Exibe o nome do cliente, todos os produtos cadastrados e o valor total da compra.

3. Execução

    Crie um pedido para um cliente.
    Instancie pelo menos quatro produtos.
    Adicione todos os produtos ao pedido.
    Remova um dos produtos.
    Adicione outro produto.
    Exiba o resumo final do pedido contendo os produtos restantes e o valor total.
'''

'''
Retorno do terminal:

'''