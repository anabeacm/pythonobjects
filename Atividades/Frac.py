'''
Atividade Fracao.py

Todos os atributos da classe devem ser privados e acessíveis
via funções de acesso;

Método __str__ para print dos objetos da classe;

Validações falhas disparam ValueError com raise.

O construtor da classe Fracao:
    num int padrão 1
    den int padrão 1

A fração deve:
    - possuir numerador e denominador inteiros;
    - possuir denominador diferente de zero;
    - ser sempre irredutível;
    - possuir denominador positivo.

Operações:
    + Adição
    - Subtração
    * Multiplicação
    / Divisão
    < Menor que
    == Igualdade

Testes de todos os métodos na MAIN.
'''

from math import gcd


class Fracao:

    def __init__(self, num=1, den=1):

        if not isinstance(num, int):
            raise ValueError('Numerator must be an integer.')

        if not isinstance(den, int) or den == 0:
            raise ValueError('Denominator must be a non-zero integer.')

        divisor = gcd(num, den)

        num = num // divisor
        den = den // divisor

        # Mantém o denominador positivo
        if den < 0:
            num = -num
            den = -den

        self.num = num
        self.den = den

    # Get and Set num
    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num_):
        if isinstance(num_, int):
            self.__num = num_
        else:
            raise ValueError('Numerator must be an integer.')

    # Get and Set den
    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, den_):
        if isinstance(den_, int) and den_ != 0:
            self.__den = den_
        else:
            raise ValueError('Denominator must be a non-zero integer.')

    # Adição
    def __add__(self, other):
        if isinstance(other, Fracao):

            num = self.num * other.den + other.num * self.den
            den = self.den * other.den

            return Fracao(num, den)

        else:
            raise RuntimeError('Can only add Fracao objects.')

    # Subtração
    def __sub__(self, other):
        if isinstance(other, Fracao):

            num = self.num * other.den - other.num * self.den
            den = self.den * other.den

            return Fracao(num, den)

        else:
            raise RuntimeError('Can only subtract Fracao objects.')

    # Multiplicação
    def __mul__(self, other):
        if isinstance(other, Fracao):

            num = self.num * other.num
            den = self.den * other.den

            return Fracao(num, den)

        else:
            raise RuntimeError('Can only multiply Fracao objects.')

    # Divisão
    def __truediv__(self, other):
        if isinstance(other, Fracao):

            if other.num == 0:
                raise ValueError('Cannot divide by a zero fraction.')

            num = self.num * other.den
            den = self.den * other.num

            return Fracao(num, den)

        else:
            raise RuntimeError('Can only divide Fracao objects.')

    # Menor que
    def __lt__(self, other):
        if isinstance(other, Fracao):

            return self.num * other.den < other.num * self.den

        else:
            raise RuntimeError(
                'Fracao can only be compared to another Fracao.'
            )

    # Igualdade
    def __eq__(self, other):
        if isinstance(other, Fracao):

            return self.num == other.num and self.den == other.den

        else:
            raise RuntimeError(
                'Fracao can only be compared to another Fracao.'
            )

    # Print da fração
    def __str__(self):
        return f'{self.num}/{self.den}'


if __name__ == '__main__':

    ''' TESTES DO CONSTRUTOR '''

    print('\n--- TESTES DO CONSTRUTOR ---')

    # Fração padrão
    try:
        f1 = Fracao()
        print(f'Fração padrão: {f1}')

    except ValueError as e:
        print({e})

    # Fração normal
    try:
        f2 = Fracao(3, 5)
        print(f'Fração: {f2}')

    except ValueError as e:
        print({e})

    # Fração que precisa ser simplificada
    try:
        f3 = Fracao(6, 8)
        print(f'Fracao(6, 8) = {f3}')

    except ValueError as e:
        print({e})

    # Fração com denominador negativo
    try:
        f4 = Fracao(2, -4)
        print(f'Fracao(2, -4) = {f4}')

    except ValueError as e:
        print({e})


    ''' TESTES DOS ACESSORES '''

    print('\n--- TESTES DOS ACESSORES ---')

    try:
        f = Fracao(3, 5)

        print(f'Numerador: {f.num}')
        print(f'Denominador: {f.den}')

    except ValueError as e:
        print({e})


    ''' TESTES DE ERRO DO CONSTRUTOR '''

    print('\n--- TESTES DE ERRO DO CONSTRUTOR ---')

    # Numerador não inteiro
    try:
        f = Fracao(2.5, 3)

    except ValueError as e:
        print({e})

    # Denominador não inteiro
    try:
        f = Fracao(2, 3.5)

    except ValueError as e:
        print({e})

    # Denominador zero
    try:
        f = Fracao(3, 0)

    except ValueError as e:
        print({e})


    ''' TESTE DE ADIÇÃO '''

    print('\n--- TESTE DE ADIÇÃO ---')

    try:
        f1 = Fracao(1, 2)
        f2 = Fracao(1, 3)

        resultado = f1 + f2

        print(f'{f1} + {f2} = {resultado}')

    except RuntimeError as e:
        print({e})


    # Erro: objeto não é Fracao
    try:
        f1 = Fracao(1, 2)

        resultado = f1 + 2

    except RuntimeError as e:
        print({e})


    ''' TESTE DE SUBTRAÇÃO '''

    print('\n--- TESTE DE SUBTRAÇÃO ---')

    try:
        f1 = Fracao(3, 4)
        f2 = Fracao(1, 4)

        resultado = f1 - f2

        print(f'{f1} - {f2} = {resultado}')

    except RuntimeError as e:
        print({e})


    # Erro: objeto não é Fracao
    try:
        f1 = Fracao(3, 4)

        resultado = f1 - 2

    except RuntimeError as e:
        print({e})


    ''' TESTE DE MULTIPLICAÇÃO '''

    print('\n--- TESTE DE MULTIPLICAÇÃO ---')

    try:
        f1 = Fracao(2, 3)
        f2 = Fracao(3, 4)

        resultado = f1 * f2

        print(f'{f1} * {f2} = {resultado}')

    except RuntimeError as e:
        print({e})


    # Erro: objeto não é Fracao
    try:
        f1 = Fracao(2, 3)

        resultado = f1 * 2

    except RuntimeError as e:
        print({e})


    ''' TESTE DE DIVISÃO '''

    print('\n--- TESTE DE DIVISÃO ---')

    try:
        f1 = Fracao(2, 3)
        f2 = Fracao(4, 5)

        resultado = f1 / f2

        print(f'{f1} / {f2} = {resultado}')

    except (RuntimeError, ValueError) as e:
        print({e})


    # Erro: divisão por zero
    try:
        f1 = Fracao(1, 2)
        f2 = Fracao(0, 1)

        resultado = f1 / f2

    except ValueError as e:
        print({e})


    # Erro: objeto não é Fracao
    try:
        f1 = Fracao(1, 2)

        resultado = f1 / 2

    except RuntimeError as e:
        print({e})


    ''' TESTE DE MENORIDADE '''

    print('\n--- TESTE DE MENORIDADE ---')

    # Resultado True
    try:
        f1 = Fracao(1, 3)
        f2 = Fracao(1, 2)

        resultado = f1 < f2

        print(f'{f1} < {f2} = {resultado}')

    except RuntimeError as e:
        print({e})


    # Resultado False
    try:
        f1 = Fracao(3, 4)
        f2 = Fracao(1, 2)

        resultado = f1 < f2

        print(f'{f1} < {f2} = {resultado}')

    except RuntimeError as e:
        print({e})


    # Erro: objeto não é Fracao
    try:
        f1 = Fracao(1, 2)

        resultado = f1 < 2

    except RuntimeError as e:
        print({e})


    ''' TESTE DE IGUALDADE '''

    print('\n--- TESTE DE IGUALDADE ---')

    # Frações iguais
    try:
        f1 = Fracao(1, 2)
        f2 = Fracao(2, 4)

        print(f'{f1} == {f2} = {f1 == f2}')

    except RuntimeError as e:
        print({e})


    # Frações diferentes
    try:
        f1 = Fracao(1, 2)
        f2 = Fracao(2, 3)

        print(f'{f1} == {f2} = {f1 == f2}')

    except RuntimeError as e:
        print({e})


    # Erro: objeto não é Fracao
    try:
        f1 = Fracao(1, 2)

        resultado = f1.__eq__(2)

    except RuntimeError as e:
        print({e})


    ''' TESTE DE IMPRESSÃO '''

    print('\n--- TESTE DE IMPRESSÃO ---')

    try:
        f = Fracao(3, 5)

        print(f)

    except ValueError as e:
        print({e})


    print('\n--- FIM DOS TESTES ---')