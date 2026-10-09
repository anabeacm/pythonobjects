from abc import ABC, abstractmethod

'''
ABC is a helper base class that you inherit from when defining an Abstract Base Class.
abstractmethod is a decorator used to mark methods that must be implemented by subclasses.
'''


class Veiculo(ABC):
    def __init__(self, nome, estado = 'desligado', operacao = 'parado'):
        self.__nome = nome
        self.__estado = estado
        self.__operacao = operacao

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome_):
        if isinstance(nome_, str) and len(nome_) > 0:
            self.__nome = nome_
        else:
            raise RuntimeError('Name must be an non empty string')

    @property
    def estado(self):
        return self.__estado

    @estado.setter
    def estado(self, estado_):
        if isinstance(estado_, str) and len(estado_) > 0:
            self.__estado = estado_
        else:
            raise RuntimeError('State must be an non empty string')

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao_):
        if self.__estado == 'ligado':
            self.__operacao = operacao_
            print(f'Estado: {self.__estado}')
            print(f'Operação: {self.__operacao}')
                
    def ligar(self):
        if self.__estado == 'desligado':
            self.__estado = 'ligado'
        print(f'O estado do veículo é {self.__estado} e operação {self.__operacao}')

    def desligar(self):
        if self.__estado == 'ligado':
            self.__estado = 'desligado'
        print(f'O estado do veículo é {self.__estado} e operação {self.__operacao}')

class Terrestre(Veiculo):

    def __init__(self, nome, estado='desligado', operacao='parado'):
        super().__init__(nome, estado, operacao)

    @abstractmethod
    def deslocar(self, valor):
        pass

class Carro(Terrestre):
    def __init__(self, nome, estado='desligado', operacao='parado'):
        super().__init__(nome, estado, operacao)

    def operacao(self):
        return super().operacao()

    def deslocar(self, valor):
        if self.estado == 'ligado':
            if valor > 0:
                self.operacao = 'Em deslocamento para frente'
            elif valor < 0:
                self.operacao = 'Em deslocamento para trás'

carro = Carro('Fusca')
carro.ligar()
carro.deslocar(10)
print(carro.operacao)
carro.deslocar(-5)
print(carro.operacao)