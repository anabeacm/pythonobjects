'''
Aula 1:
Funcionamento de memória:
- Armazenamento em variável simples (estado)
- Armazenamento em variáveis compostas -> Lista (estados e índices)
- Armazenamento em variáveis com elementos nomeados -> Dicionários (índices literais/configuráveis)

Necessidade de separação entre dados e funções (dados + funções):
- Permitir que uma variável armazene dados e execute funcionalidades -> Objeto

Criando Classes e Objetos simples na prática: Python padronizado com objetos.
'''

# Declaração da Classe

class Gafanhoto:
    def __init__(self): # Método construtor

    # Atributos de instância
        self.nome = ""
        self.idade = 0

    # Métodos
    def aniversario(self):
        self.idade = self.idade + 1
    
    def mensagem(self):
        return f"{self.nome} é Gafanhoto, tem {self.idade} anos de idade!"

# Declaração dos Objetos

g1 = Gafanhoto() # Instânciação

g1.nome = "Maria"
g1.idade = 16
g1.aniversario()

print(g1.mensagem())
