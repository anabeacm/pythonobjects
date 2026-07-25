'''
Questão 10 — Mini Sistema Bancário:
Implemente uma classe chamada ContaBancaria utilizando conceitos de encapsulamento para simular operações bancárias essenciais.

1. Atributos da Classe
    titular (string): Nome do dono da conta.
    numero_conta (int ou string): Número identificador da conta.
    __saldo (float): Saldo da conta. Deve ser um atributo privado (utilizando dois sublinhados __) para impedir o acesso direto.

2. Métodos
    depositar(valor): Adiciona o valor fornecido ao saldo private, desde que o valor seja maior que zero.
    sacar(valor): Subtrai o valor do saldo private, impedindo a operação caso o saldo fique negativo (exiba uma mensagem de erro se o saldo for insuficiente).
    consultar_saldo(): Retorna ou exibe o valor do saldo de forma segura, mantendo o encapsulamento.
    exibir_dados(): Imprime o titular, número da conta e o saldo atualizado.

3. Execução
    Crie uma lista chamada contas_bancarias para armazenar as contas do sistema.
    Instancie pelo menos duas contas com saldos iniciais distintos e adicione-as à lista.
    Realize uma operação de depósito e uma de saque em uma das contas.
    Tente realizar um saque com valor superior ao saldo disponível para testar a validação de saldo negativo.
    Tente acessar diretamente o atributo privado de saldo (ex: conta.__saldo) fora da classe para comprovar que o acesso está bloqueado.
    Percorra a lista contas_bancarias exibindo os dados finais de cada conta no terminal.
'''