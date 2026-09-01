class EndDevice:
    def __init__(self, name='localhost', address='127.0.01'):
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
            raise RuntimeError('name deve ser uma string não vazia')

    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address_):
        if isinstance(address_, str) and len(address_) > 0 :
            self.__address = address_

        else:
            raise RuntimeError('adress deve ser uma string não vazia')

# metodo eq

    def __eq__(self, other):
        if not isinstance(other,EndDevice):
            return False
        return self.__address == other.__address

    def __str__(self):
            return f'EndDevice(name: {self.__name}), (address: {self.__address})'
    
class NetworkDevice:
    def __init__(self, name='device', address='192.168.0.1'):
        self.name = name
        self.address = address

        self.__endDevices = []
    # funções de acesso
    
    @property
    def name(self):
        return self.__name 

    @name.setter
    def name(self, name_):
        if isinstance(name_, str) and len(name_)>0:
            self.__name = name_

        else:
            raise RuntimeError('name deve ser uma string não vazia') 


    @property
    def address(self):
        return self.__address

    @address.setter
    def address(self, address_):
        if isinstance(address_,str) and len(address_)>0 :
            self.__address = address_

        else:
            raise RuntimeError('Address deve ser uma string não vazia')

    # metodo add()
    def add(self, endDevice: EndDevice):
        if not isinstance(endDevice, EndDevice):
            raise RuntimeError('endDevice deve ser do tipo EndDevice')
        if endDevice in self.__endDevices: 
            raise RuntimeError('endDevice já está em endDevices')
        self.__endDevices.append(endDevice)

    def remove(self, endDevice: EndDevice):
        if not isinstance(endDevice, EndDevice):
            raise RuntimeError('endDevice deve ser do tipo EndDevice')
        if endDevice not in self.__endDevices :
            raise RuntimeError('Despositivo não conectado')
        self.__endDevices.remove(endDevice)

    # retorno do tamanho da rede
    def __len__(self):
        return len(self.__endDevices)

    def __str__(self):
        return f'NetworkDevice(name: {self.__name}), (address: {self.__address})'

if __name__ == '__main__':

    host1 = EndDevice()

    print(host1)

    host2 = EndDevice('notebook', '192.168.0.2')
    host3 = EndDevice('impressora', '192.168.0.3')

    print(host2)
    print(host3)

    print('nome:', host2.name, host2.address)

    host4 = EndDevice()

    print(host1 == host4)
    print(host2 == host4)

    net1 = NetworkDevice()
    print(net1)
    net2 = NetworkDevice('switch', '192.168.0.2')
    print(net2)
    print('tamanho inicial da rede:', len(net1))
    net1.add(host1)
    net1.add(host2)
    net1.add(host3)
    print(len(net1))
    net1.remove(host2)
    print(len(net1))

    try: 
        EndDevice('','192.168.0.2')
    except RuntimeError as error:
        print('erro: ', error )

    try:
        EndDevice('name', '')
    except RuntimeError as error:
        print('erro: ', error)
    try:
        EndDevice(4,'1.92.168.0.2')
    except RuntimeError as error:
        print('erro: ', error)
    try:
        EndDevice('name',4)
    except RuntimeError as error:
        print('erro: ', error)

    try: 
        NetworkDevice('','192.168.0.2')
    except RuntimeError as error:
        print('erro: ', error )

    try:
        NetworkDevice('name', '')
    except RuntimeError as error:
        print('erro: ', error)
    try:
        NetworkDevice(4,'1.92.168.0.2')
    except RuntimeError as error:
        print('erro: ', error)
    try:
        NetworkDevice('name',4)
    except RuntimeError as error:
        print('erro: ', error)
    try:
        net1.add(host4)
    except RuntimeError as error:
        print('erro: ', error)
    try:
        net1.remove(host2)
    except RuntimeError as error:
        print('erro: ', error)
    try:
        net1.add('str')
    except RuntimeError as error:
        print('erro: ', error)