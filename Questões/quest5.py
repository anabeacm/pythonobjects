'''
Questão 5 — Conta Bancária
Crie uma classe ContaBancaria contendo:
    Titular
    Saldo

Regras:
    O saldo não pode ser alterado diretamente.
    O saldo não pode ficar negativo.
    Criar métodos depositar(), sacar() e consultar_saldo().

Depois:
    Crie duas contas.
    Faça depósitos.
    Faça saques válidos.
    Tente realizar um saque inválido.
    Mostre o saldo final de cada conta.
'''

# Aprendendo conceitos de encapsulamento.

class ContaBancaria:
    def __init__(self, titular, saldo):

        self.titular = titular
        self._saldo = saldo
        ''' O _ no início do nome é uma convenção em
        Python que indica que o atributo é "interno"
        e não deve ser acessado diretamente.'''

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor # Só aceita valores positivos

    def sacar(self, valor):
        if valor <= self._saldo: # Verificação de saldo
            self._saldo -= valor # Finaliza saque e atualiza saldo

        else:
            print("\nSaldo insuficiente")
        
    def consultar_saldo(self):
        return f"O saldo do cliente {self.titular} é de {self._saldo} reais"


conta1 = ContaBancaria("Bia", 10000)
conta2 = ContaBancaria("João", 30000)

conta1.depositar(200)
conta2.depositar(400)

conta1.sacar(300)
conta2.sacar(100)

conta2.sacar(9000000)

print(conta1.consultar_saldo())
print(conta2.consultar_saldo())