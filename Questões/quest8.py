'''
Questão 8 — Sistema de Loja: 
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