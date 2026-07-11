'''
Questão 1 — Pessoa
Crie uma classe Pessoa que possua:
    Nome
    Idade

Depois:
    Crie três pessoas diferentes.
    Faça um método chamado apresentar().
    Altere a idade de uma delas.
    Mostre as informações antes e depois da alteração.
'''

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        return f"{self.nome} tem {self.idade} anos de idade"

    def aniversario(self):
        self.idade += 1

user1 = Pessoa("Ana", 18)
user2 = Pessoa("Pedro", 20)
user3 = Pessoa("Fábio", 40)

print(f"Antes do aniversário de {user1.nome}:")
print(user1.apresentar())
print(user2.apresentar())
print(user3.apresentar())

user1.aniversario()

print(f"\nDepois do aniversário de {user1.nome}:")

print(user1.apresentar())
print(user2.apresentar())
print(user3.apresentar())



