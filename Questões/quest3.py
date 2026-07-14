'''
Questão 3 — Carro
Crie uma classe Carro contendo:
    Modelo
    Ano
    Cor

Depois:
    Crie três carros.
    Faça os métodos ligar() e desligar().
    Troque a cor de um dos carros.
    Mostre o estado de cada carro.

Civic — Ano: 2012 — Cor: Prata
Corolla — Ano: 2018 — Cor: Branco Pérola
Gol — Ano: 2020 — Cor: Preto
'''

class Carro:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.estado = "desligado"

    def ligar(self):
        self.estado = "ligado"

    def desligar(self):
        self.estado = "desligado"

    def trocar_cor(self, cor):
        self.cor = cor

    def mostrar_dados(self):
        return f"{self.modelo} — Ano: {self.ano} — Cor: {self.cor} — Estado: {self.estado}"


carro1 = Carro("Civic", 2012, "Prata")
carro2 = Carro("Corolla", 2018, "Branco Pérola")
carro3 = Carro("Gol", 2020, "Preto")

carro2.ligar()
carro3.trocar_cor("Vermelho")

print(carro1.mostrar_dados())
print(carro2.mostrar_dados())
print(carro3.mostrar_dados())
