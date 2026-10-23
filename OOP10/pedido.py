class pedido:
    def __init__(self, nome = 'Cliente', *pecas, **obs):
    
            self.nome = nome
            self.__pecas = []
            self.adic_pecas(*pecas)
            self.__obs = {}
            self.adic_obs(*obs)

    def adic_pecas(self, *pecas):
        for p in pecas:
            if isinstance(p, Peca):
                if p not in self.pecas:
                    self.__pecas.append(p)
                else:
                    raise ValueError('A Peça ja foi adicionada ao pedido')
            else:
                raise TypeError('Só é possível adicionar Peças ao pedido')

    def adic_obs(self, **obs):
        for key, value in obs.items():
            self.__obs[key] = value

class Peca:
    def __init__(self, modelo, valor):
        self.modelo = modelo
        self.valor = valor

    def __str__(self):
        return f'{self.__class__.__name__}: modelo {self.modelo}, valor: R$ {self.valor:_.2f}'

class Processador(Peca):
    def __init__(self, modelo, valor, clock):
        super().__init__(modelo, valor)
        self.clock = clock

    def __str__(self):
        return super().__str__() + f', clock: {self.clock} GHz'

class PlacaMae(Peca):
    def __init__(self, modelo, valor, padrao):
        super().__init__(modelo, valor)
        self.padrao = padrao

    def __str__(self):
        return super().__str__() + f', padrão: {self.padrao}'
    
class Memoria(Peca):
    def __init__(self, modelo, valor, capacidade):
        super().__init__(modelo, valor)
        self.capacidade = capacidade

    def __str__(self):
        return super().__str__() + f', capacidade: {self.capacidade} GB'
    
class Fonte(Peca):
    def __init__(self, modelo, valor, potencia):
        super().__init__(modelo, valor)
        self.potencia = potencia

    def __str__(self):
        return super().__str__() + f', potencia: {self.potencia} Watts'

class Disco(Peca):
    def __init__(self, modelo, valor, capacidade):
        super().__init__(modelo, valor)
        self.capacidade = capacidade

    def __str__(self):
        return super().__str__() + f', capacidade: {self.capacidade} GB'
    
class Gabinete(Peca):
    def __init__(self, modelo, valor, tipo):
        super().__init__(modelo, valor)
        self.tipo = tipo

    def __str__(self):
        return super().__str__() + f', tipo: {self.tipo}'
    
if __name__ == '__main__':

    p = Peca('pecax', 100)
    print(p)

    pro = Processador('i7', 3500, 3.2)
    print(pro)

    a = PlacaMae('i7', 3500, 3.2)
    print(a)

    b = Memoria('i7', 3500, 3.2)
    print(b)

    c = Fonte('i7', 3500, 3.2)
    print(c)

    d = Disco('i7', 3500, 3.2)
    print(d)

    e = Gabinete('i7', 3500, 3.2)
    print(e)