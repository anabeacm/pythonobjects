'''
Questão 13 — Sistema de Turmas:

Implemente as classes Aluno e Turma para simular o gerenciamento de uma turma escolar.

1. Atributos das Classes

Aluno:
    nome (string): Nome do aluno.
    matricula (int ou string): Número de matrícula.
    nota (float): Nota final do aluno.

Turma:
    nome (string): Nome da turma.
    alunos (list): Lista de objetos da classe Aluno (deve iniciar vazia).

2. Métodos

Classe Aluno:
    alterar_nota(nova_nota): Atualiza a nota do aluno.
    exibir_dados(): Exibe o nome, matrícula e nota do aluno.

Classe Turma:
    adicionar_aluno(aluno): Adiciona um objeto Aluno à turma.
    remover_aluno(matricula): Remove da turma o aluno cuja matrícula foi informada.
    buscar_aluno(matricula): Procura um aluno pela matrícula e retorna o objeto encontrado (ou exibe uma mensagem caso não exista).
    calcular_media(): Calcula e retorna a média das notas da turma.
    listar_aprovados(): Exibe apenas os alunos com nota maior ou igual a 7,0.
    listar_alunos(): Exibe os dados de todos os alunos cadastrados.

3. Execução

    Crie uma turma.
    Instancie pelo menos quatro alunos.
    Adicione todos à turma.
    Altere a nota de um dos alunos.
    Remova um aluno.
    Exiba todos os alunos restantes.
    Exiba a média da turma.
    Liste apenas os alunos aprovados.
'''
class Aluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self.nota = nota

    def alterar_nota(self, nova_nota):
        self.nota = nova_nota

    def exibir_dados(self):
        print(f"{self.nome} | {self.matricula} | {self.nota}")


class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

    def remover_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                self.alunos.remove(aluno)
                return
        print("Aluno não encontrado.")

    def buscar_aluno(self, matricula):
        for aluno in self.alunos:
            if aluno.matricula == matricula:
                return aluno
        print("Aluno não encontrado.")
        return None

    def calcular_media(self):
        if len(self.alunos) == 0:
            return 0

        total = 0

        for aluno in self.alunos:
            total += aluno.nota

        return total / len(self.alunos)

    def listar_aprovados(self):
        for aluno in self.alunos:
            if aluno.nota >= 7.0:
                aluno.exibir_dados()

    def listar_alunos(self):
        for aluno in self.alunos:
            aluno.exibir_dados()

turma = Turma("Telecom")

aluno1 = Aluno("Ana", 1, 8.5)
aluno2 = Aluno("Joao", 2, 6.0)
aluno3 = Aluno("Maria", 3, 9.2)
aluno4 = Aluno("Pedro", 4, 7.1)

turma.adicionar_aluno(aluno1)
turma.adicionar_aluno(aluno2)
turma.adicionar_aluno(aluno3)
turma.adicionar_aluno(aluno4)

aluno2.alterar_nota(7.5)

turma.remover_aluno(4)

print("Alunos:")
turma.listar_alunos()

print("\nBusca:")
aluno = turma.buscar_aluno(3)
if aluno:
    aluno.exibir_dados()

print("\nMedia:")
print(turma.calcular_media())

print("\nAprovados:")
turma.listar_aprovados()

'''
Retorno do terminal:
Alunos:
Ana | 1 | 8.5
Joao | 2 | 7.5
Maria | 3 | 9.2

Busca:
Maria | 3 | 9.2

Media:
8.4

Aprovados:
Ana | 1 | 8.5
Joao | 2 | 7.5
Maria | 3 | 9.2
'''