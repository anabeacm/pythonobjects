'''
Questão 15 — Sistema de Gerenciamento de Universidade

Implemente as classes Disciplina, Aluno e Universidade para simular um sistema acadêmico simples utilizando conceitos de Programação Orientada a Objetos.

1. Atributos das Classes

Disciplina:
    nome (string): Nome da disciplina.
    carga_horaria (int): Carga horária da disciplina em horas.
    professor (string): Nome do professor responsável.

Aluno:
    nome (string): Nome completo do aluno.
    matricula (int ou string): Número de matrícula.
    disciplinas (list): Lista de objetos da classe Disciplina (deve iniciar vazia).
    notas (dict): Dicionário onde a chave é o nome da disciplina e o valor é a nota do aluno (deve iniciar vazio).

Universidade:
    nome (string): Nome da universidade.
    alunos (list): Lista de objetos da classe Aluno (deve iniciar vazia).
    disciplinas (list): Lista de objetos da classe Disciplina (deve iniciar vazia).

2. Métodos

Classe Disciplina:
    alterar_professor(novo_professor): Atualiza o professor responsável pela disciplina.
    exibir_dados(): Exibe o nome da disciplina, o professor e a carga horária.

Classe Aluno:
    matricular_disciplina(disciplina): Recebe um objeto Disciplina e o adiciona à lista de disciplinas do aluno, caso ele ainda não esteja matriculado.
    remover_disciplina(nome_disciplina): Remove uma disciplina da lista do aluno pelo nome.
    lançar_nota(nome_disciplina, nota): Registra ou atualiza a nota do aluno em uma disciplina.
    consultar_nota(nome_disciplina): Exibe ou retorna a nota do aluno em uma disciplina.
    calcular_media(): Calcula e retorna a média das notas cadastradas.
    verificar_aprovacao(nome_disciplina): Informa se o aluno foi aprovado (nota maior ou igual a 7,0), reprovado ou se ainda não possui nota registrada.
    exibir_dados(): Exibe o nome do aluno, matrícula, disciplinas matriculadas e suas respectivas notas.

Classe Universidade:
    cadastrar_aluno(aluno): Adiciona um objeto Aluno à universidade.
    cadastrar_disciplina(disciplina): Adiciona um objeto Disciplina à universidade.
    buscar_aluno(matricula): Procura um aluno pela matrícula e retorna o objeto encontrado (ou exibe uma mensagem caso não exista).
    buscar_disciplina(nome): Procura uma disciplina pelo nome e retorna o objeto encontrado (ou exibe uma mensagem caso não exista).
    listar_alunos(): Exibe os dados de todos os alunos cadastrados.
    listar_disciplinas(): Exibe os dados de todas as disciplinas cadastradas.
    listar_aprovados(nome_disciplina): Exibe apenas os alunos aprovados na disciplina informada.
    calcular_media_geral(): Calcula e exibe a média das médias de todos os alunos cadastrados.

3. Execução

    Crie uma universidade.

    Instancie pelo menos quatro disciplinas diferentes e cadastre-as na universidade.

    Instancie pelo menos três alunos e cadastre-os na universidade.

    Matricule cada aluno em pelo menos duas disciplinas.

    Lance notas para todas as disciplinas cursadas pelos alunos.

    Atualize a nota de um dos alunos utilizando lançar_nota().

    Troque o professor de uma das disciplinas utilizando alterar_professor().

    Remova uma disciplina da matrícula de um dos alunos.

    Utilize buscar_aluno() para localizar um aluno pela matrícula.

    Utilize buscar_disciplina() para localizar uma disciplina pelo nome.

    Exiba todos os alunos cadastrados.

    Exiba todas as disciplinas cadastradas.

    Liste apenas os alunos aprovados em uma disciplina específica.

    Exiba a média de cada aluno.

    Exiba a média geral da universidade.

4. Restrições

    • Não utilizar variáveis globais.
    • Toda manipulação dos dados deve ocorrer por meio dos métodos das classes.
    • Sempre que possível, reutilize métodos já implementados para evitar repetição de código.
    • Não permitir que um aluno seja matriculado duas vezes na mesma disciplina.
    • Caso uma disciplina ou aluno não seja encontrado, exiba uma mensagem adequada.
    • O programa deve permanecer executando normalmente mesmo após operações inválidas (como buscar um aluno inexistente ou remover uma disciplina não matriculada).
'''

'''
Retorno do terminal:

'''