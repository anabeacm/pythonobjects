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

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def exibir_dados(self):
        print(f"Produto: {self.nome} | Preço: R$ {self.preco:.2f}")


class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, nome):
        for item in self.produtos:
            if item.nome == nome:
                self.produtos.remove(item)
                print(f"Produto '{nome}' removido com sucesso.")
                return

        print(f"Produto '{nome}' não encontrado.")

    def calcular_total(self):
        total = 0

        for item in self.produtos:
            total += item.preco

        return total

    def listar_pedido(self):
        print(f"\nCliente: {self.cliente}")
        print("Produtos:")

        for item in self.produtos:
            print(f"- {item.nome} | R$ {item.preco:.2f}")

        print(f"Valor total: R$ {self.calcular_total():.2f}")

ped1 = Pedido("Matheus")

p1 = Produto("Carregador", 15.00)
p2 = Produto("Caixa", 10.00)
p3 = Produto("Pilha", 5.00)
p4 = Produto("Microfone", 400.00)

ped1.adicionar_produto(p1)
ped1.adicionar_produto(p2)
ped1.adicionar_produto(p3)
ped1.adicionar_produto(p4)

print("Pedido inicial:")
ped1.listar_pedido()

ped1.remover_produto("Caixa")

print("\nApós remover um produto:")
ped1.listar_pedido()

p5 = Produto("Teletransportador", 3000.00)
ped1.adicionar_produto(p5)

print("\nApós adicionar um novo produto:")
ped1.listar_pedido()

'''
Retorno do terminal:

Pedido inicial:

Cliente: Matheus
Produtos:
- Carregador | R$ 15.00
- Caixa | R$ 10.00
- Pilha | R$ 5.00
- Microfone | R$ 400.00
Valor total: R$ 430.00
Produto 'Caixa' removido com sucesso.

Após remover um produto:

Cliente: Matheus
Produtos:
- Carregador | R$ 15.00
- Pilha | R$ 5.00
- Microfone | R$ 400.00
Valor total: R$ 420.00

Após adicionar um novo produto:

Cliente: Matheus
Produtos:
- Carregador | R$ 15.00
- Pilha | R$ 5.00
- Microfone | R$ 400.00
- Teletransportador | R$ 3000.00
Valor total: R$ 3420.00

'''