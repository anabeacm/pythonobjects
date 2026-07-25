'''
Questão 11 — Sistema de Biblioteca:

Implemente as classes Livro e Biblioteca para simular o gerenciamento de um acervo de livros.

1. Atributos das Classes

Livro:
    titulo (string): Título do livro.
    autor (string): Nome do autor.
    disponivel (bool): Indica se o livro está disponível para empréstimo (inicia como True).

Biblioteca:
    nome (string): Nome da biblioteca.
    livros (list): Lista que armazenará objetos da classe Livro (deve iniciar vazia).

2. Métodos

Classe Livro:
    emprestar(): Altera o atributo disponivel para False caso o livro esteja disponível. Caso contrário, exibe uma mensagem informando que o livro já está emprestado.
    devolver(): Altera o atributo disponivel para True.
    exibir_dados(): Exibe o título, autor e situação do livro (Disponível ou Emprestado).

Classe Biblioteca:
    adicionar_livro(livro): Recebe um objeto Livro e o adiciona à lista.
    listar_livros(): Exibe os dados de todos os livros cadastrados.
    buscar_livro(titulo): Procura um livro pelo título e retorna o objeto encontrado (ou exibe uma mensagem caso não exista).

3. Execução

    Crie uma biblioteca.
    Instancie pelo menos três livros e adicione-os à biblioteca.
    Realize um empréstimo de um dos livros.
    Tente emprestar novamente o mesmo livro para testar a validação.
    Devolva o livro.
    Liste todos os livros ao final mostrando seus estados.
'''

'''
Retorno do terminal:

'''