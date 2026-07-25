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

class ContaBancaria:
    def __init__(self, titular, numero_conta, saldo):
        self.titular = titular
        self.numero_conta = numero_conta
        self.__saldo = saldo  # Atributo privado (name mangling)

    def depositar(self, valor):
        if valor > 0:
            self.__saldo += valor
        else:
            print("Valor inválido, operação não pode ser concluída.")

    def sacar(self, valor):
        if valor > 0 and valor <= self.__saldo:
            self.__saldo -= valor
        else:
            print("Saldo insuficiente, operação não pode ser concluída.")

    def consultar_saldo(self):
        return f"R$ {self.__saldo:.2f}"

    def exibir_dados(self):
        print(
            f"Titular: {self.titular} | "
            f"Número da conta: {self.numero_conta} | "
            f"Saldo: {self.consultar_saldo()}"
        )

contas_bancarias = []

c1 = ContaBancaria("João", 1, 300.00)
c2 = ContaBancaria("Alice", 2, 4000.99)

contas_bancarias.append(c1)
contas_bancarias.append(c2)

print("\nContas cadastradas")
for conta in contas_bancarias:
    conta.exibir_dados()

print("\nOperações")
c1.depositar(-300.00) # print Valor inválido
c2.depositar(500.00) # Depósito válido

c1.sacar(40.00) # Saque válido
c2.sacar(400.00) # Saque válido

c2.sacar(90000.00) # print Saldo insuficiente

print("\nContas após as operações")
for conta in contas_bancarias:
    conta.exibir_dados()

print("\nTestando encapsulamento:")
try:
    print(c1.__saldo)
except AttributeError:
    print("Não é possível acessar diretamente um atributo privado.")