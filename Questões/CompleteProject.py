'''
Atividade Device.py

Todos os atributos das classes devem ser privados e acessíveis via funções de acesso;
Método __ para print dos objetos de cada classe;
Validações falhas que falharem dispara 'RuntimeError' com raise.
O contrutor da classe NetworkDevice:
    name str não vazia padrão device
    address str não vazia padrão 192.168.0.1

O contrutor da classe NetworkDevice:
    name str não vazia padrão device
    address str não vazia padrão 127.0.0.1


Relações de composição e Herança

Composição 1 para 1
Composição N para N
Composição 1 para N - Lista []

NetworkDevice:
    add(endDevice: EndDevice)
    remove(endDevice: EndDevice)

    lista __endDevices não vazia

    dois dispositivos endDevice iguais não podem ser adicionados à lista

    somente podem ser removidos da lista quem está na lista


Testes de métodos na MAIN
'''

class NetworkDevice:
    def __init__(self, name='device', address='192.168.0.1'): # Método construtor Net - Com parâmetros - Parametrizado - Se parametro não informado, recebe 'device' - Função polimórfica
        self.name = name # Chama a função e depois ele recebe
        self.address = address

        self.__endDevices = []

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name_):
        if isinstance(name_, str) and len(name_) > 0:
            self.__name = name_
        else:
            raise RuntimeError('Device name must be a non-empty string')

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address_):
        if isinstance(address_, str) and len(address_) > 0:
            self.__address = address_
        else:
            raise RuntimeError('Device address must be a non-empty string')
        
    '''
    def __init__(self): - Sem parâmetros - Construtor padrão
            pass
    '''

    # Teste de igualdade de EndDevice e dispara RuntimeError - Validação de tipo =/ Validação de método!
    def __eq__(self, other):
        if isinstance(other, EndDevice):
            return self.address == other.address
        else:
            raise RuntimeError('EndDevice can only be compared to other EndDevice')

    def add(self, endDevice):
        if isinstance(endDevice, EndDevice):
            if endDevice not in self.__endDevices:
                self.__endDevices.append(endDevice)
            else:
                raise RuntimeError('Can only add an EndDevice once')
        else:
            raise RuntimeError('Can only add EndDevices')
        
    def remove(self, endDevice):
        if isinstance(endDevice, EndDevice):
            if endDevice in self.__endDevices:
                self.__endDevices.remove(endDevice)
            else:
                raise RuntimeError('EndDevice does not belong to NetworkDevice.')
        else:
            raise RuntimeError('Can only remove EndDevices')
    
    def __str__(self): # Dunder String return String
        res = f'{self.__class__.__name__} -> [name: {self.name}, address: {self.address}]\n'
        for ed in self.__endDevices:
            res += str(ed) + '\n'
        return res

    '''
    def __repr__(self): # Dunder Representation - Só retorna string - Serve como print
            pass
    '''
        
class EndDevice:
    def __init__(self, name='localhost', address='127.0.0.1'):
        self.name = name
        self.address = address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name_):
        if isinstance(name_, str) and len(name_) > 0:
            self.__name = name_
        else:
            raise RuntimeError('Device name must be a non-empty string')

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address_):
        if isinstance(address_, str) and len(address_) > 0:
            self.__address = address_
        else:
            raise RuntimeError('Device address must be a non-empty string')

    def __str__(self):
        return f'EndDevice -> [name: {self.name}, address: {self.address}]'
    

if __name__ == '__main__':
    # Ver tipos de erro - RuntimeError / Exception / ValueError etc
    
    # Na prova é obrigado fazer os try exceptions de todos os erros
    
    '''NETWORKDEVICES'''
    nd = NetworkDevice(address='192.168.0.1')
    print(f'\n{nd}')
    nd1 = NetworkDevice(name='Switch1')
    print(f'{nd1}\n')

    ''' TESTES NETWORKDEVICE'''
    # Erro name string vazia e Erro string int
    try:
        nd = NetworkDevice(name='')
    except RuntimeError as e:
        print({e})
    try:
        nd2 = NetworkDevice(name=1)
    except RuntimeError as e:
        print({e})

    # Erro address string vazia e Erro string int
    try:
        nd1 = NetworkDevice(address='')
    except RuntimeError as e:
        print({e})

    try:
        nd3 = NetworkDevice(address=1)
    except RuntimeError as e:
        print({e})


    ''' ENDDEVICES'''
    end = EndDevice(address='192.168.0.1')
    print(f'\n{end}')
    end1 = EndDevice(name='Switch1')
    print(f'{end1}\n')

    ''' TESTES ENDDEVICE'''
    # Erro name string vazia e Erro string int
    try:
        end = EndDevice(name='')
    except RuntimeError as e:
        print({e})
    try:
        end2 = EndDevice(name=1)
    except RuntimeError as e:
        print({e})

    # Erro address string vazia e Erro string int
    try:
        end1 = EndDevice(address='')
    except RuntimeError as e:
        print({e})

    try:
        end3 = EndDevice(address=1)
    except RuntimeError as e:
        print({e})

    nd.add(end)
    nd.add(end1)
    print(f'\n{nd}')

    nd.remove(end)
    print(nd)