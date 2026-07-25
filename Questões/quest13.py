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

'''
Retorno do terminal:

'''