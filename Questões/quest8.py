'''
Questão 8 — Sistema de Loja

Implemente as classes Produto e Loja para simular o gerenciamento do estoque de um comércio.

1. Atributos das Classes

Produto:
    nome (string): Nome do produto.
    preco (float): Preço unitário do produto.

Loja:
    nome_loja (string): Nome do estabelecimento.
    produtos (list): Lista que armazenará os objetos da classe Produto (deve iniciar vazia).

2. Métodos

Classe Produto:
    alterar_preco(novo_preco): Atualiza o preço do produto com o novo valor fornecido.

Classe Loja:
    cadastrar_produto(produto): Recebe um objeto Produto e o adiciona à lista de produtos.
    listar_produtos(): Percorre a lista e exibe o nome e o preço de todos os produtos cadastrados.
    procurar_produto(nome): Busca um produto na lista pelo nome e retorna o objeto encontrado (ou exibe uma mensagem caso não exista).

3. Execução:
    Instancie um objeto da classe Loja.
    Crie pelo menos três objetos da classe Produto e utilize o método cadastrar_produto() para adicioná-los à loja.
    Utilize o método alterar_preco() em um dos produtos.
    Execute o método listar_produtos() para exibir o catálogo atualizado.
    Realize uma busca por um produto cadastrado utilizando o método procurar_produto().
'''

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def alterar_preco(self, novo_preco):
        self.preco = novo_preco

    def exibir(self):
        print(f"{self.nome} - R$ {self.preco:.2f}")

class Loja:
    def __init__(self, nome_loja):
        self.nome_loja = nome_loja
        self.produtos = []

    def cadastrar_produto(self, produto):
        self.produtos.append(produto)

    def listar_produtos(self):
        print(f"Produtos da loja {self.nome_loja}:")
        for produto in self.produtos:
            produto.exibir()

    def procurar_produto(self, nome):
        for produto in self.produtos:
            if produto.nome == nome:
                print("Produto encontrado:")
                produto.exibir()
                return produto

        print("Produto não existe.")
        return None


loja1 = Loja("Maria Bonita")

arroz = Produto("Arroz", 26.00)
feijao = Produto("Feijão", 40.00)
macarrao = Produto("Macarrão", 8.50)

loja1.cadastrar_produto(arroz)
loja1.cadastrar_produto(feijao)
loja1.cadastrar_produto(macarrao)

print("\nListando Produtos:")
loja1.listar_produtos()

arroz.alterar_preco(30.00)

print("\nListando Produtos:")
loja1.listar_produtos()

print("\nBuscando Arroz:")
loja1.procurar_produto("Arroz")

print("\nBuscando Café:")
loja1.procurar_produto("Café")

'''
Retorno do terminal:

Listando Produtos:
Produtos da loja Maria Bonita:
Arroz - R$ 26.00
Feijão - R$ 40.00
Macarrão - R$ 8.50

Listando Produtos:
Produtos da loja Maria Bonita:
Arroz - R$ 30.00
Feijão - R$ 40.00
Macarrão - R$ 8.50

Buscando Arroz:
Produto encontrado:
Arroz - R$ 30.00

Buscando Café:
Produto não existe.

'''