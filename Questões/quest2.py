'''
Questão 2 — Livro
Crie uma classe Livro contendo:
    Título
    Autor
    Número de páginas

Depois:
    Crie quatro livros.
    Faça um método mostrar_dados().
    Altere o número de páginas de um livro.
    Exiba todas as informações.
'''
class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def mostrar_dados(self):
        return f"O livro '{self.titulo}', escrito por {self.autor}, possui {self.paginas} páginas."

    def alterar_paginas(self, paginas):
        self.paginas = paginas


livro1 = Livro("Feiura", "Monteiro Lobato", 400)
livro2 = Livro("Lindeza", "Ana Beatriz", 500)
livro3 = Livro("Gostosura", "Julieta", 600)
livro4 = Livro("Fofura", "Claudinho", 700)

print(livro1.mostrar_dados())
print(livro2.mostrar_dados())
print(livro3.mostrar_dados())
print(livro4.mostrar_dados())

livro4.alterar_paginas(850)

print(livro4.mostrar_dados())
