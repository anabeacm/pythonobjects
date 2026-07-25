'''
Questão 9 — Sistema de Cadastro de Pessoas:
Implemente uma classe chamada Pessoa para representação e manipulação de dados cadastrais simples.

1. Atributos da Classe
    nome (string): Nome completo da pessoa.
    idade (int): Idade da pessoa em anos.

2. Métodos
    alterar_nome(novo_nome): Atualiza o atributo nome da pessoa.
    alterar_idade(nova_idade): Atualiza o atributo idade da pessoa.
    exibir_dados(): Imprime o nome e a idade da pessoa de forma organizada.

3. Execução
    Crie uma lista vazia chamada cadastro_pessoas.
    Instancie pelo menos três objetos da classe Pessoa e adicione-os à lista.
    Utilize os métodos alterar_nome() e alterar_idade() para modificar os dados de uma das pessoas da lista.
    Percorra a lista de pessoas e execute o método exibir_dados() para cada uma delas no terminal.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    def alterar_nome(self, novo_nome):
        self.nome = novo_nome
    def alterar_idade(self, nova_idade):
        self.idade = nova_idade
    def exibir_dados(self):
        print(f"{self.nome} - {self.idade}")

cadastro_pessoas = []

p1 = Pessoa("Afonso", 22)
p2 = Pessoa("Sofia", 40)
p3 = Pessoa("Ana", 66)

cadastro_pessoas.append(p1)
cadastro_pessoas.append(p2)
cadastro_pessoas.append(p3)

print("\nPessoas cadastradas:")
for pessoa in cadastro_pessoas:
    pessoa.exibir_dados()

p1.alterar_nome("Ítalo")
p1.alterar_idade(80)

print("\nPessoas cadastradas:")
for pessoa in cadastro_pessoas:
    pessoa.exibir_dados()


'''
Retorno do terminal:

Pessoas cadastradas:
Afonso - 22
Sofia - 40
Ana - 66

Pessoas cadastradas:
Ítalo - 80
Sofia - 40
Ana - 66
'''