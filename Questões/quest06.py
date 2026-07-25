'''
Questão 6 — Biblioteca
Crie duas classes:
    Livro
    Biblioteca
     biblioteca deve possuir vários livros.

Depois:
    Cadastre cinco livros.
    Crie um método para listar todos os livros.
    Crie um método para procurar um livro pelo título.
'''

# Iniciando compreensão de conceitos de composição em um sistema simples

class Livro:
    def __init__(self, titulo, autor, datapublic):
        self.titulo = titulo
        self.autor = autor
        self.datapublic = datapublic


class Biblioteca:
    def __init__(self):
        self.livros = []

    def cadastrar_livro(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for livro in self.livros:
            print(f"Título: {livro.titulo}")
            print(f"Autor: {livro.autor}")
            print(f"Data de publicação: {livro.datapublic}\n")

    def procurar_livro(self, titulo):
        for livro in self.livros:
            if livro.titulo == titulo:
                print(f"Titulo: {livro.titulo}")
                print(f"Autor: {livro.autor}")
                print(f"Data de publicação: {livro.datapublic}\n")
                return

        print("Livro não encontrado")

biblioteca = Biblioteca()

livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899)
livro2 = Livro("1984", "George Orwell", 1949)
livro3 = Livro("O Hobbit", "J. R. R. Tolkien", 1937)
livro4 = Livro("O Pequeno Príncipe", "Antoine de Saint-Exupéry", 1943)
livro5 = Livro("A Revolução dos Bichos", "George Orwell", 1945)

biblioteca.cadastrar_livro(livro1)
biblioteca.cadastrar_livro(livro2)
biblioteca.cadastrar_livro(livro3)
biblioteca.cadastrar_livro(livro4)
biblioteca.cadastrar_livro(livro5)

print("\nListando livros na biblioteca:")
biblioteca.listar_livros()

print("\nBuscando livro 1984:")
biblioteca.procurar_livro("1984")

'''
Retorno do terminal:

Listando livros na biblioteca:
Título: Dom Casmurro
Autor: Machado de Assis
Data de publicação: 1899

Título: 1984
Autor: George Orwell
Data de publicação: 1949

Título: O Hobbit
Autor: J. R. R. Tolkien
Data de publicação: 1937

Título: O Pequeno Príncipe
Autor: Antoine de Saint-Exupéry
Data de publicação: 1943

Título: A Revolução dos Bichos
Autor: George Orwell
Data de publicação: 1945


Buscando livro 1984:
Titulo: 1984
Autor: George Orwell
Data de publicação: 1949
'''