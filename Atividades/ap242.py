from abc import ABC, abstractmethod

class Veiculo:
    identificador = 0

    @classmethod
    def countidentificador(cls):
        Veiculo.identificador += 1
        return Veiculo.identificador

    def __init__(self, nome='veiculo', estado='desligado', operacao='parado'):
        self.__id = Veiculo.countidentificador()
        self.nome = nome
        self.__estado = estado
        self.__operacao = operacao

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome_):
        if isinstance(nome_, str) and len(nome_) > 0:
            self.__nome = nome_
        else:
            raise RuntimeError('O nome deve ser uma string não vazia.')

    @property
    def estado(self):
        return self.__estado

    @property
    def operacao(self):
        return self.__operacao

    @operacao.setter
    def operacao(self, operacao_):
        if self.__estado != 'ligado':
            print('O veículo precisa estar ligado para mudar de operação.')
            return

        if self.__operacao != operacao_:
            self.__operacao = operacao_
            print(f'Estado: {self.__estado}')
            print(f'Operação: {self.__operacao}')


    def ligar(self):
        if self.__estado == 'desligado':
            self.__estado = 'ligado'
            print(f'Estado: {self.__estado}')
            print(f'Operação: {self.__operacao}')
        else:
            print('O veículo já está ligado.')

    def desligar(self):
        if self.__estado == 'ligado':
            self.__operacao = 'parado'
            self.__estado = 'desligado'
            print(f'Estado: {self.__estado}')
            print(f'Operação: {self.__operacao}')
        else:
            print('O veículo já está desligado.')

class Terrestre(ABC):

    @abstractmethod
    def deslocar(self, valor):
        pass

class Carro(Veiculo, Terrestre):

    def __init__(self, nome='veiculo', estado='desligado', operacao='parado'):
        super().__init__(nome, estado, operacao)

    def deslocar(self, valor):
        if self.estado != 'ligado':
            print('O carro precisa estar ligado para se deslocar.')
            return

        if valor > 0:
            self.operacao = 'Em deslocamento para frente'
        elif valor < 0:
            self.operacao = 'Em deslocamento para trás'
        else:
            self.operacao = 'parado'

class Maritimo(ABC):

    @abstractmethod
    def navegar(self, valor):
        pass

class Barco(Veiculo, Maritimo):

    def __init__(self, nome='veiculo', estado='desligado', operacao='parado'):
        super().__init__(nome, estado, operacao)

    def navegar(self, valor):
        if self.estado != 'ligado':
            print('O barco precisa estar ligado para navegar.')
            return

        if valor > 0:
            self.operacao = 'Em navegação para frente'
        elif valor < 0:
            self.operacao = 'Em navegação para trás'
        else:
            self.operacao = 'parado'

class Aereo(ABC):

    def __init__(self, nome='veiculo', estado='desligado', operacao='parado'):
        super().__init__(nome, estado, operacao)
        
    @abstractmethod
    def decolar(self):
        pass

    @abstractmethod
    def pousar(self):
        pass

    @abstractmethod
    def voar(self):
        pass

class Foguete(Veiculo, Aereo):

    def decolar(self):
        if self.estado == 'ligado':
            self.operacao = 'Decolando'
        else:
            print('O foguete precisa estar ligado para decolar.')

    def pousar(self):
        if self.estado == 'ligado':
            self.operacao = 'Pousando'
        else:
            print('O foguete precisa estar ligado para pousar.')

    def voar(self):
        if self.estado == 'ligado':
            self.operacao = 'Voando'
        else:
            print('O foguete precisa estar ligado para voar.')

if __name__ == '__main__':

    carro = Carro('Fusca')
    carro.ligar()
    carro.deslocar(10)
    print(carro.operacao)
    carro.deslocar(-5)
    print(carro.operacao)

    print()

    barco = Barco('Boat')
    barco.ligar()
    barco.navegar(10)
    print(barco.operacao)
    barco.navegar(-5)
    print(barco.operacao)

    print()

    foguete = Foguete('NASA')
    foguete.decolar()
    foguete.pousar()
    foguete.voar()
    foguete.ligar()
    foguete.decolar()
    print(foguete.operacao)
    foguete.pousar()
    print(foguete.operacao)
    foguete.voar()
    print(foguete.operacao)

    print()

    print(carro.id)
    print(barco.id)
    print(foguete.id)
