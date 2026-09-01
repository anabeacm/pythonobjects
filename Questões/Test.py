class EndDevice:

    '''
A Classe EndDevice é uma forma que cria objetos EndDevice
    '''
    def __init__(self, name='localhost', address='127.0.0.1'):
        """
        Este é um método padrão construtor.

        Parâmetros:
            name (str): nome do dispositivo - padrão caso seja criado sem nome é localhost.
            address (str): endereço IP do dispositivo - padrão caso seja criado sem address é 127.0.0.1.
        """

        # Aqui você protege os atributos pós serem criados pelo método construtor, nesse caso são atributos privados com __
            # também podem ser protegidos com _
                # ou públicos sem underscore.
        self.name = name
        self.address = address

    # FUNÇÃO DE ACESSO AO ATRIBUTO __name
        # Ainda dentro da class, mas fora do método construtor, programam-se os gets e sets de maneira organizada.
            # Utiliza-se @property para get
            # Utiliza-se @coisa.setter para set

    @property
    def name(self):
        """
        Getter do atributo privado __name.
        """
        return self.__name

    @name.setter
    def name(self, name_):
        """
        Setter do atributo privado __name.
        """
        if isinstance(name_, str) and len(name_) > 0:
            self.__name = name_
        else:
            raise RuntimeError('Device name must be a non-empty string')

    # FUNÇÃO DE ACESSO AO ATRIBUTO __address

    @property
    def address(self):
        """
        Getter do atributo privado __address.
        """
        return self.__address

    @address.setter
    def address(self, address_):
        """
        Setter do atributo privado __address.
        """
        if isinstance(address_, str) and len(address_) > 0:
            self.__address = address_
        else:
            raise RuntimeError('Device address must be a non-empty string')

    # MÉTODO ESPECIAL __str__ (print())
        # Como citado em sala, existem métodos especiais dunder, nesse caso o método __str__, __eq__ etc
    
    def __str__(self):
        """
        Define como o objeto será representado quando
        utilizado com print().
        """
        return f'EndDevice(name={self.__name}, address={self.__address})'

    # MÉTODO ESPECIAL __eq__ (==)

    def __eq__(self, other):
        """
        Compara dois EndDevice.

        Dois dispositivos finais são considerados iguais
        quando possuem o mesmo endereço IP.
        """

        if not isinstance(other, EndDevice):
            return False

        return self.__address == other.__address


class NetworkDevice:

    '''
A Classe NetworkDevice é uma forma que cria objetos NetworkDevice
    '''

    def __init__(self, name='device', address='192.168.0.1'):
        """
        Construtor da classe NetworkDevice.

        Parâmetros:
            name (str): nome do dispositivo.
            address (str): endereço IP do dispositivo.
        """

        self.name = name
        self.address = address

        # Lista privada de dispositivos finais com __
        self.__endDevices = []

    # FUNÇÃO DE ACESSO AO ATRIBUTO __name

    @property
    def name(self):
        """
        Getter do atributo privado __name.
        """
        return self.__name

    @name.setter
    def name(self, name_):
        """
        Setter do atributo privado __name.
        """
        if isinstance(name_, str) and len(name_) > 0:
            self.__name = name_
        else:
            raise RuntimeError('Device name must be a non-empty string')

    # FUNÇÃO DE ACESSO AO ATRIBUTO __address

    @property
    def address(self):
        """
        Getter do atributo privado __address.
        """
        return self.__address

    @address.setter
    def address(self, address_):
        """
        Setter do atributo privado __address.
        """
        if isinstance(address_, str) and len(address_) > 0:
            self.__address = address_
        else:
            raise RuntimeError('Device address must be a non-empty string')

    # MÉTODO add()

    def add(self, endDevice: EndDevice):
        """
        Adiciona um dispositivo final à rede.

        Não permite dois dispositivos com o mesmo endereço IP.
        """

        # Verifica se o argumento realmente é um EndDevice
        if not isinstance(endDevice, EndDevice):
            raise RuntimeError(
                'O dispositivo deve ser uma instância de EndDevice.'
            )

        # Verifica se já existe um dispositivo com o mesmo endereço
        if endDevice in self.__endDevices:
            raise RuntimeError(
                'Já existe um dispositivo com esse endereço IP.'
            )

        # Adiciona o dispositivo à lista
        self.__endDevices.append(endDevice)

    # MÉTODO remove()

    def remove(self, endDevice: EndDevice):
        """
        Remove um dispositivo final da rede.

        Só permite remover um dispositivo que esteja
        conectado à rede.
        """

        # Verifica se o argumento realmente é um EndDevice
        if not isinstance(endDevice, EndDevice):
            raise RuntimeError(
                'O dispositivo deve ser uma instância de EndDevice.'
            )

        # Verifica se o dispositivo está na lista
        if endDevice not in self.__endDevices:
            raise RuntimeError(
                'O dispositivo não está conectado à rede.'
            )

        # Remove o dispositivo
        self.__endDevices.remove(endDevice)

    # MÉTODO ESPECIAL __len__ (len())

    def __len__(self):
        """
        Retorna a quantidade de dispositivos finais
        conectados ao NetworkDevice.

        Permite utilizar:

            len(network)
        """
        return len(self.__endDevices)

    # MÉTODO ESPECIAL __str__

    def __str__(self):
        """
        Define como o NetworkDevice será representado
        quando utilizado com print().
        """
        return f'NetworkDevice(name={self.__name}, address={self.__address})'


# TESTES COMPLETOS SOLICITADOS

if __name__ == '__main__':

    print('\nTESTANDO EndDevice\n')

    # Instancia utilizando os valores padrão
    host1 = EndDevice()

    # Instancia utilizando valores diferentes
    host2 = EndDevice('notebook', '192.168.0.2')
    host3 = EndDevice('printer', '192.168.0.3')

    # Testando print() -> __str__()
    print(host1)
    print(host2)
    print(host3)

    # Testando propriedades
    print('\nNome:', host2.name)
    print('Endereço:', host2.address)

    # Instancia EndDevice idêntico a um já pré-existente
    host4 = EndDevice('outro_nome', '192.168.0.2')

    # Testando igualdade -> __eq__
    print('\nhost2 == host4:', host2 == host4)
    print('host2 == host3:', host2 == host3)

    print('\nTESTANDO NetworkDevice\n')

    # Instancia de um dispositivo intermediário
    network = NetworkDevice('switch', '192.168.0.1')

    # Testando print()
    print(network)

    # Inicialmente a rede não possui hosts -> __len__ -> 0
    print('\nTamanho inicial da rede:', len(network))

    # Adicionando dispositivos
    network.add(host2)
    network.add(host3)

    print('Tamanho após adicionar dois dispositivos:', len(network))

    # Removendo um dispositivo
    network.remove(host2)

    print('Tamanho após remover um dispositivo:', len(network))

    print('\nTESTANDO EXCEÇÕES\n')

    # Nome vazio
    try:
        EndDevice('', '192.168.0.2')
    except RuntimeError as error:
        print('Erro:', error)

    # Endereço vazio
    try:
        EndDevice('notebook', '')
    except RuntimeError as error:
        print('Erro:', error)

    # Tipo incorreto para nome
    try:
        EndDevice(123, '192.168.0.2')
    except RuntimeError as error:
        print('Erro:', error)

    # Tipo incorreto para endereço
    try:
        EndDevice('notebook', 123)
    except RuntimeError as error:
        print('Erro:', error)

    # Tentando adicionar o mesmo endereço
    try:
        network.add(host3)
    except RuntimeError as error:
        print('Erro:', error)

    # Tentando remover dispositivo que não está conectado
    try:
        network.remove(host2)
    except RuntimeError as error:
        print('Erro:', error)

    # Tentando adicionar algo que não é EndDevice
    try:
        network.add('not a device')
    except RuntimeError as error:
        print('Erro:', error)

'''
Retorno do terminal para o código:

TESTANDO EndDevice

EndDevice(name=localhost, address=127.0.0.1)
EndDevice(name=notebook, address=192.168.0.2)
EndDevice(name=printer, address=192.168.0.3)

Nome: notebook
Endereço: 192.168.0.2

host2 == host4: True
host2 == host3: False

TESTANDO NetworkDevice

NetworkDevice(name=switch, address=192.168.0.1)

Tamanho inicial da rede: 0
Tamanho após adicionar dois dispositivos: 2
Tamanho após remover um dispositivo: 1

TESTANDO EXCEÇÕES

Erro: Device name must be a non-empty string
Erro: Device address must be a non-empty string
Erro: Device name must be a non-empty string
Erro: Device address must be a non-empty string
Erro: Já existe um dispositivo com esse endereço IP.
Erro: O dispositivo não está conectado à rede.
Erro: O dispositivo deve ser uma instância de EndDevice.

'''