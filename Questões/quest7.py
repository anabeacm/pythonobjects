'''
Questão 7 — Gestão de Alunos: Implemente uma classe chamada Aluno para gerenciar as informações acadêmicas de um estudante.

1. Atributos da Classe:
    nome (string): Nome do aluno.
    matricula (string ou int): Número de identificação do aluno.
    nota (float): Nota final do aluno.

2. Métodos:
    alterar_nota(nova_nota): Recebe um novo valor de nota e atualiza o atributo do aluno.
    verificar_aprovacao(): Retorna True (ou uma mensagem) se a nota do aluno for maior ou igual a 7.0, e False caso contrário.
    exibir_dados(): Imprime o nome, matrícula, nota e o status de aprovação do aluno de forma organizada.

3. Execução:
    Instancie quatro objetos da classe Aluno com dados fictícios.
    Utilize o método alterar_nota() para atualizar a nota de pelo menos um dos alunos.
    Percorra a lista de alunos e utilize os métodos criados para exibir os dados e o status de aprovação de cada um deles no terminal.
'''

class Aluno:
    def __init__(self, nome, matricula, nota):
        self.nome = nome
        self.matricula = matricula
        self._nota = nota

    def alterar_nota(self, nova_nota):
        self._nota = nova_nota

    def verificar_aprovacao(self):
        if self._nota >= 7:
            return "Aluno aprovado"
        else:
            return "Aluno reprovado"

    def exibir_dados(self):
        print(f"Nome do aluno: {self.nome}")
        print(f"Matrícula do aluno: {self.matricula}")
        print(f"Nota do aluno: {self._nota}")
        print(f"Situação: {self.verificar_aprovacao()}")
        print("-" * 30)

Alu1 = Aluno("Matheus", 2023, 7.0)
Alu2 = Aluno("Júlia", 2024, 9.0)
Alu3 = Aluno("Sofia", 2025, 8.0)
Alu4 = Aluno("Jaime", 2020, 6.9)

alunos = [Alu1, Alu2, Alu3, Alu4]

print("\nDados dos alunos:")
for aluno in alunos:
    aluno.exibir_dados()

print("\nAlterando notas -----")
Alu1.alterar_nota(5.0)

print("\nSituação dos alunos após a alteração:")
for aluno in alunos:
    aluno.exibir_dados()