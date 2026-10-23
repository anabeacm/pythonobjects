from math import gcd


class MinhaClasse:

    def __init__(self, atributo1=0, atributo2=1):
        self.atributo1 = atributo1
        self.atributo2 = atributo2

    # =========================
    # PROPERTY + SETTER
    # =========================

    @property
    def atributo1(self):
        return self.__atributo1

    @atributo1.setter
    def atributo1(self, atributo1_):
        if isinstance(atributo1_, int):
            self.__atributo1 = atributo1_
        else:
            raise ValueError('Atributo deve ser inteiro.')

    # =========================
    # MÉTODO NORMAL
    # =========================

    def metodo(self):
        return self.atributo1

    # =========================
    # MÉTODO PROTEGIDO
    # =========================
    # Um "_" indica que é protegido por convenção.
    # Ainda pode ser acessado de fora.

    def _metodo_protegido(self):
        return 'Método protegido'

    # =========================
    # MÉTODO PRIVADO
    # =========================
    # Dois "__" indicam que é privado.
    # É usado internamente pela classe.

    def __metodo_privado(self):
        return 'Método privado'

    # Um método da própria classe pode chamá-lo:
    def usar_privado(self):
        return self.__metodo_privado()

    # =========================
    # __STR__
    # =========================
    # print(objeto)
    # Deve retornar uma STRING.

    def __str__(self):
        return f'{self.atributo1}/{self.atributo2}'

    # =========================
    # __LEN__
    # =========================
    # len(objeto)
    # Deve retornar um INTEIRO.

    def __len__(self):
        return self.atributo1

    # =========================
    # COMPARAÇÕES
    # =========================

    # objeto1 == objeto2
    # Retorna True ou False

    def __eq__(self, other):
        return self.atributo1 == other.atributo1

    # objeto1 != objeto2

    def __ne__(self, other):
        return self.atributo1 != other.atributo1

    # objeto1 < objeto2

    def __lt__(self, other):
        return self.atributo1 < other.atributo1

    # objeto1 <= objeto2

    def __le__(self, other):
        return self.atributo1 <= other.atributo1

    # objeto1 > objeto2

    def __gt__(self, other):
        return self.atributo1 > other.atributo1

    # objeto1 >= objeto2

    def __ge__(self, other):
        return self.atributo1 >= other.atributo1

    # =========================
    # OPERAÇÕES MATEMÁTICAS
    # =========================

    # objeto1 + objeto2
    # Retorna o resultado da soma

    def __add__(self, other):
        return self.atributo1 + other.atributo1

    # objeto1 - objeto2

    def __sub__(self, other):
        return self.atributo1 - other.atributo1

    # objeto1 * objeto2

    def __mul__(self, other):
        return self.atributo1 * other.atributo1

    # objeto1 / objeto2

    def __truediv__(self, other):
        return self.atributo1 / other.atributo1

    # objeto1 // objeto2

    def __floordiv__(self, other):
        return self.atributo1 // other.atributo1

    # objeto1 % objeto2

    def __mod__(self, other):
        return self.atributo1 % other.atributo1

    # objeto1 ** objeto2

    def __pow__(self, other):
        return self.atributo1 ** other.atributo1


# =====================================================
# TESTES
# =====================================================

if __name__ == '__main__':

    objeto1 = MinhaClasse(10, 2)
    objeto2 = MinhaClasse(5, 1)

    # ---------------------------------
    # PRINT
    # ---------------------------------

    print(objeto1)
    # chama automaticamente:
    # objeto1.__str__()

    # ---------------------------------
    # LEN
    # ---------------------------------

    print(len(objeto1))
    # chama:
    # objeto1.__len__()

    # ---------------------------------
    # MÉTODO NORMAL
    # ---------------------------------

    print(objeto1.metodo())

    # ---------------------------------
    # MÉTODO PROTEGIDO
    # ---------------------------------

    print(objeto1._metodo_protegido())

    # ---------------------------------
    # MÉTODO PRIVADO
    # ---------------------------------

    print(objeto1.usar_privado())

    # ---------------------------------
    # COMPARAÇÕES
    # ---------------------------------

    print(objeto1 == objeto2)   # __eq__
    print(objeto1 != objeto2)   # __ne__
    print(objeto1 < objeto2)    # __lt__
    print(objeto1 <= objeto2)   # __le__
    print(objeto1 > objeto2)    # __gt__
    print(objeto1 >= objeto2)   # __ge__

    # ---------------------------------
    # MATEMÁTICA
    # ---------------------------------

    print(objeto1 + objeto2)    # __add__
    print(objeto1 - objeto2)    # __sub__
    print(objeto1 * objeto2)    # __mul__
    print(objeto1 / objeto2)    # __truediv__
    print(objeto1 // objeto2)   # __floordiv__
    print(objeto1 % objeto2)    # __mod__
    print(objeto1 ** objeto2)   # __pow__

   # =====================================================
    # TRY / EXCEPT
    # =====================================================

    # -----------------------------------------------------
    # ValueError
    # -----------------------------------------------------
    # Valor possui tipo correto, mas é inválido.

    try:
        objeto1.atributo1 = 'abc'
    except ValueError as e:
        print(e)


    # -----------------------------------------------------
    # TypeError
    # -----------------------------------------------------
    # Tipo incompatível com a operação.

    try:
        resultado = 10 + 'abc'
    except TypeError as e:
        print(e)


    # -----------------------------------------------------
    # ZeroDivisionError
    # -----------------------------------------------------
    # Divisão por zero.

    try:
        resultado = 10 / 0
    except ZeroDivisionError as e:
        print(e)


    # -----------------------------------------------------
    # IndexError
    # -----------------------------------------------------
    # Índice que não existe em uma lista.

    try:
        lista = [10, 20, 30]
        print(lista[10])
    except IndexError as e:
        print(e)


    # -----------------------------------------------------
    # KeyError
    # -----------------------------------------------------
    # Chave que não existe em um dicionário.

    try:
        pessoa = {'nome': 'Bia'}
        print(pessoa['idade'])
    except KeyError as e:
        print(e)


    # -----------------------------------------------------
    # AttributeError
    # -----------------------------------------------------
    # Tentativa de acessar atributo que não existe.

    try:
        print(objeto1.nome)
    except AttributeError as e:
        print(e)


    # -----------------------------------------------------
    # RuntimeError
    # -----------------------------------------------------
    # Erro definido pelo próprio programador.

    try:
        raise RuntimeError('Erro definido pelo programador.')
    except RuntimeError as e:
        print(e)


    # -----------------------------------------------------
    # ValueError criado pelo programador
    # -----------------------------------------------------

    try:
        raise ValueError('Valor inválido.')
    except ValueError as e:
        print(e)


    # =====================================================
    # TRY / EXCEPT COM MAIS DE UM ERRO
    # =====================================================

    try:
        numero = int('abc')
        resultado = 10 / numero

    except ValueError as e:
        print('Erro de valor:', e)

    except ZeroDivisionError as e:
        print('Erro de divisão:', e)

    except TypeError as e:
        print('Erro de tipo:', e)


    # =====================================================
    # EXCEPTION
    # =====================================================
    # Captura praticamente qualquer erro.
    # Deve ser usado com cuidado.

    try:
        resultado = 10 / 0

    except Exception as e:
        print('Algum erro aconteceu:', e)