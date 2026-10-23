class Pedido:
    def __init__(self, nome = 'Cliente', *pecas, **obs):

        self.nome = nome
        self.pecas = []
        self.adic_pecas(*pecas)
        self.observacao = obs
        self.compra = self.valor_total(*pecas)
        #self.adic_obs(obs.items())

    def adic_pecas(self, *pecas):

        for peca in pecas:
            if isinstance(peca, Peca):
                if peca not in self.pecas:

                    self.pecas.append(peca)

                else:
                    raise ValueError('A Peça ja foi adicionada ao pedido')
            else:
                raise TypeError('Só é possível adicionar Peças ao pedido')
            
    def adic_obs(self,x):
        res = ''
        for k, v in x:

            res += f'{k}:' + str(v) + '\n'

        self.observacao = res

            

    def valor_total(self,*valor):
        
        res=sum(valor)
            #res += k.valor

        self.compra = res
            
    def __str__(self):

        
        res = f'Pedido do cliente ({self.nome}): \n'

        res += f'Peças: \n'

        for p in self.pecas:

            res += str(p)
        
        res += f'\nObservações:\n'
        for k,v in self.observacao.items():

            res += f'{k}:' + str(v) + '\n'
        
        #res += f'Valor Total: {self.compra}'

        return res
        
    

class Peca:
    def __init__(self, modelo= 'Peça', valor= 0.0):

        self.modelo = modelo
        self.valor = valor

    @property
    def modelo(self):

        return self._modelo
    
    @modelo.setter
    def modelo(self, modelo):
        if isinstance(modelo, str):
            if len(modelo) > 0:

                self._modelo = modelo
            
            else:
                raise ValueError('O modelo não pode ser uma string vazia')
        else:
            raise TypeError('O modelo tem que ser uma string')
    
    @property
    def valor(self):

        return self._valor
    
    @valor.setter
    def valor(self, valor):
        if isinstance(valor,(int,float)):
            if valor >= 0:

                self._valor = valor
            
            else:
                raise ValueError('O Valor não pode ser um número negativo')
        else:
            raise TypeError('O Valor tem que ser um número')
    
    def __str__(self):
        
        return f'-Peça: {self.modelo}\n valor: {self.valor} R$\n'
    
    def __add__(self, peca2):
        if isinstance(peca2, Peca):

            self.valor += peca2.valor

            return self


        
class Processador(Peca):
        def __init__(self, modelo='I7', valor=500.0, clock= 3.4):
            super().__init__(modelo, valor)

            self.clock = clock
        
        @property
        def clock(self):

            return self._clock
        
        @clock.setter
        def clock(self, clo):
            if isinstance(clo, float):

                self._clock = clo

            else:
                raise TypeError('O clock tem que ser um número flutuante')
        
        def __str__(self):
            return super().__str__() + f'Info- Clock: {self.clock} Ghz\n'

class PlacaMae(Peca):
    def __init__(self, modelo='AMD', valor=600, padrao= 'ATX'):
        super().__init__(modelo, valor)

        self.padrao = padrao

    @property
    def padrao(self):

        return self._padrao

    @padrao.setter
    def padrao(self, padrao):
        if isinstance(padrao, str):
            if len(padrao) > 0:

                self._padrao = padrao
        
            else:
                raise ValueError('O Padrão não pode ser uma string vazia')
        else:
            raise TypeError('O Padrão tem que ser uma string')
        
    def __str__(self):
        
        return super().__str__() + f'Info- Padrão: {self.padrao}\n'
    
class Memoria(Peca):
    def __init__(self, modelo='Kingstom', valor=1000, capacidade=16):
        super().__init__(modelo, valor)

        self.capacidade = capacidade

    @property
    def capacidade(self):

        return self._capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade):
        if isinstance(capacidade,int):
            if capacidade > 0:

                self._capacidade = capacidade
            
            else:
                raise ValueError('A Capacidade não pode ser menor que 0')
        else:
            raise TypeError('O Capacidade tem que ser um número inteiro')
        
    def __str__(self):
        
        return super().__str__() + f'Info- Capacidade: {self.capacidade} GB\n'
    
class Fonte(Peca):
    def __init__(self, modelo='Modular', valor=200, potencia= 650):
        super().__init__(modelo, valor)

        self.potencia = potencia

    @property
    def potencia(self):

        return self._potencia
    
    @potencia.setter
    def potencia(self, potencia):
        if isinstance(potencia,int):
            if potencia > 0:

                self._potencia = potencia
            
            else:
                raise ValueError('A Pontencia da fonte não pode ser menor que 0')
        else:
            raise TypeError('A potencia tem que ser um número inteiro')
        
    def __str__(self):
        
        return super().__str__() + f'Info- Potência: {self.potencia} W\n'
    
class Disco(Peca):
    def __init__(self, modelo='Não veio nada em mente', valor=400, capacidade = 1024):
        super().__init__(modelo, valor)

        self.capacidade = capacidade

    @property
    def capacidade(self):

        return self._capacidade
    
    @capacidade.setter
    def capacidade(self, capacidade):
        if isinstance(capacidade,int):
            if capacidade > 0:

                self._capacidade = capacidade
            
            else:
                raise ValueError('A Capacidade da fonte não pode ser menor que 0')
        else:
            raise TypeError('A Capacidade tem que ser um número inteiro')
        
    def __str__(self):
        
        return super().__str__() + f'Info- Capacidade: {self.capacidade} GB\n'
    
class Gabinete(Peca):
    def __init__(self, modelo='Pichau', valor=700, tipo= 'Tower'):
        super().__init__(modelo, valor)

        self.tipo = tipo

    @property
    def tipo(self):

        return self._tipo
    
    @tipo.setter
    def tipo(self, tipo):
        if isinstance(tipo, str):
            if len(tipo) > 0:

                self._tipo = tipo
            
            else:
                raise ValueError('O tipo do gabinete não pode ser uma string vazia')
        else:
            raise TypeError('O tipo deve ser uma string')
        
    def __str__(self):
        
        return super().__str__() + f'Info- Tipo de Gabinete: {self.tipo}\n'

if __name__ == '__main__':
    #Testes de sobrecarga de variavel
    p1 = Processador()
    print(p1)
    p2 = Processador('Ryzen 7', 200, 3.4)
    print(p2)
    pl1 = PlacaMae()
    print(pl1)
    pl2 = PlacaMae('Intel', 874, 'Micro ATX')
    print(pl2)
    m1 = Memoria()
    print(m1)
    m2 = Memoria('Pascal', 193, 32)
    print(m2)
    f1 = Fonte()
    print(f1)
    f2 = Fonte('semi-modular', 300, 900)
    d1 = Disco()
    print(d1)
    d2 = Disco('Ainda nãos sei', 100, 512)
    print(d2)
    g1 = Gabinete()
    print(g1)
    g2 = Gabinete('Acer', 400, 'Rack')
    print(g2)
    #teste do pedido
    Pedi = Pedido('Afonso',p1,pl1,m1,f1,d1, obs1= 'O gabinete vermelho', obs2= 'Disconto de 50%')
    print(Pedi)
    #teste de adiocionar peça e observação
    Pedi.adic_pecas(g1)
    #Pedi.adic_obs(Obs3= 'Se funcionar vai ser otimo')
    print(Pedi)
    #FIM dos TESTES