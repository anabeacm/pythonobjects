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

3. Execução
    Crie uma biblioteca.
    Instancie pelo menos três livros e adicione-os à biblioteca.
    Realize um empréstimo de um dos livros.
    Tente emprestar novamente o mesmo livro para testar a validação.
    Devolva o livro.
    Liste todos os livros ao final mostrando seus estados.
'''
class Livro:
    def __init__(self, titulo, autor, disponivel=True):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = disponivel

    def emprestar(self):
        if not self.disponivel:
            print(f"\nLivro '{self.titulo}' está indisponível, já emprestado.")
        else: 
            self.disponivel = False
            print(f"\nLivro '{self.titulo}' emprestado com sucesso.")

    def devolver(self):
        if self.disponivel:
            print(f"\nLivro '{self.titulo}' já consta como disponível.")
        else: 
            self.disponivel = True
            print(f"\nLivro '{self.titulo}' devolvido com sucesso.")

    def exibir_dados(self):
        situacao = "Disponível" if self.disponivel else "Emprestado"
        print(f"Livro: {self.titulo} - Autor: {self.autor} - Situação: {situacao}")

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            livro.exibir_dados()

bib1 = Biblioteca("Biblioteca Central")

liv1 = Livro("Princesinha Sofia", "Disney")
liv2 = Livro("Alice no país das maravilhas", "Lewis", False)
liv3 = Livro("Livreto", "Ana", True)

bib1.adicionar_livro(liv1)
bib1.adicionar_livro(liv2)
bib1.adicionar_livro(liv3)

print("\nLista de livros:")
bib1.listar_livros()

liv1.emprestar()
liv1.emprestar()

liv1.devolver()

print("\nLista de livros:")
bib1.listar_livros()

'''
Retorno do terminal:

Lista de livros:
Livro: Princesinha Sofia - Autor: Disney - Situação: Disponível
Livro: Alice no país das maravilhas - Autor: Lewis - Situação: Emprestado
Livro: Livreto - Autor: Ana - Situação: Disponível

Livro 'Princesinha Sofia' emprestado com sucesso.

Livro 'Princesinha Sofia' está indisponível, já emprestado.

Livro 'Princesinha Sofia' devolvido com sucesso.

Lista de livros:
Livro: Princesinha Sofia - Autor: Disney - Situação: Disponível
Livro: Alice no país das maravilhas - Autor: Lewis - Situação: Emprestado
Livro: Livreto - Autor: Ana - Situação: Disponível

'''