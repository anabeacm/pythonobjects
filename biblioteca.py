# Classe biblioteca

class Biblioteca:
    def __init__(self, nome: str = "Biblioteca Central"):
        self.nome = nome
        self.__livros = []

# Gets Sets B
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome_):
        if isinstance(nome_, str) and len(nome_) != 0:
            self.__nome = nome_
        else:
           raise RuntimeError('Nome deve ser uma string não vazia')     

# Métodos B

    def adicionar(self, livro):
        if not isinstance(livro, Livro):
            raise RuntimeError('O objeto deve ser um livro')

        if livro in self.__livros:
            raise RuntimeError('O livro já está cadastrado')

        self.__livros.append(livro)

    def remover(self, livro):
        if not isinstance(livro, Livro):
            raise RuntimeError('O objeto deve ser um livro')
        
        if livro not in self.__livros:
            raise RuntimeError('O livro não está na biblioteca')

        self.__livros.remove(livro)

# Dunders B

    def __len__(self):
        return len(self.__livros)        

    def __contains__(self, livro):
        return livro in self.__livros

    def __getitem__(self, indice):
        if not isinstance(indice, int):
            raise RuntimeError('O índice deve ser um inteiro')

        if indice < 0 or indice >= len(self.__livros):
            raise RuntimeError('Índice inválido')

        return self.__livros[indice]


# Print B

    def __str__(self):
        return f'Biblioteca {self.nome} contains {self.__livros} books'

# Classe Livro

class Livro:
    def __init__(self, titulo: str = "Sem título", autor: str = "Desconhecido", codigo: str = "0001", ano: int = 2000):
        self.titulo = titulo
        self.autor = autor
        self.codigo = codigo
        self.ano = ano

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo_):
        if isinstance(titulo_, str) and len(titulo_) != 0:
            self.__titulo = titulo_
        else:
            raise RuntimeError('Título deve ser uma string não vazia')

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor_):
        if isinstance(autor_, str) and len(autor_) != 0:
            self.__autor = autor_
        else:
            raise RuntimeError('Autor deve ser uma string não vazia')

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo_):
        if isinstance(codigo_, str) and len(codigo_) != 0:
            self.__codigo = codigo_
        else:
            raise RuntimeError('Código deve ser uma string não vazia')
        
    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, ano_):
        if isinstance(ano_, int) and ano_ > 0:
            self.__ano = ano_
        else:
            raise RuntimeError('Ano deve ser um inteiro maior que zero')

# Métodos L

# Dunders L

    def __eq__(self, other):
        return self.codigo == other.codigo

# Print L

    def __str__(self):
        return f'Informações do Livro [{self.titulo}]: {self.autor}; {self.ano}; {self.codigo} '

# Main

if __name__ == '__main__':
    pass

# Instâncias


# Try cach
    try:
        bib1 = Biblioteca("")
        print(bib1)
    except Exception as e:
        print(e)

    try:
        liv1 = Livro("")
        print(liv1)
    except Exception as e:
        print(e)