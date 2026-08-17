'''
## Questão — Sistema de Gerenciamento de Formas Geométricas

Desenvolva, em Python, um sistema orientado a objetos para gerenciamento de formas geométricas. O sistema deverá demonstrar **abstração, encapsulamento, herança, polimorfismo, composição, métodos especiais, tratamento de erros e diferentes tipos de membros de classe**.

### Requisitos

1. Crie uma classe abstrata `FormaGeometrica` utilizando `ABC`. Ela deverá possuir:

   * um identificador único;
   * uma propriedade `nome`;
   * um método abstrato `area()`;
   * um método abstrato `perimetro()`.

2. O sistema deverá possuir as classes:

   * `Retangulo`;
   * `Circulo`;
   * `Triangulo`.

   Todas deverão herdar de `FormaGeometrica` e implementar os métodos abstratos adequadamente.

3. Utilize **encapsulamento** nos atributos internos. Dimensões como largura, altura, raio e lados não poderão ser alteradas diretamente sem validação.

4. Utilize `@property` e `@setter` para controlar o acesso às dimensões. Valores inválidos deverão gerar `ValueError`.

5. Crie uma classe `CatalogoFormas`, responsável por armazenar várias formas geométricas. Essa classe deverá utilizar **composição**, mantendo internamente uma coleção de objetos `FormaGeometrica`.

6. O catálogo deverá possuir métodos para:

   * adicionar uma forma;
   * remover uma forma pelo identificador;
   * buscar uma forma;
   * calcular a soma das áreas de todas as formas;
   * retornar a forma de maior área.

7. O `CatalogoFormas` deverá possuir um **atributo de classe** responsável por contabilizar quantos catálogos foram criados e um `@classmethod` para consultar essa quantidade.

8. Implemente `__str__` em todas as classes de formas, permitindo que objetos sejam exibidos diretamente com `print()`.

9. Implemente `__eq__` para comparar duas formas geométricas considerando suas áreas.

10. Implemente `__lt__` para permitir a ordenação das formas pela área. O catálogo deverá possuir um método que retorne suas formas ordenadas.

11. Implemente `__len__` em `CatalogoFormas`, de modo que `len(catalogo)` retorne a quantidade de formas armazenadas.

12. Implemente `__contains__` para permitir verificar se uma forma está presente no catálogo utilizando o operador `in`.

13. Crie uma função `exibir_area(objeto)` que receba qualquer objeto capaz de fornecer uma operação `area()`, **sem verificar explicitamente o tipo do objeto**, demonstrando o conceito de **duck typing**.

14. Crie uma classe `RetanguloColorido` que herde de `Retangulo` e acrescente uma propriedade `cor`. A classe deverá demonstrar **especialização por herança** e deverá sobrescrever `__str__`.

15. Crie pelo menos uma situação em que o método `super()` seja utilizado corretamente para inicializar ou reutilizar o comportamento da classe-pai.

16. Utilize tratamento de exceções para situações como:

* dimensões inválidas;
* tentativa de adicionar ao catálogo algo que não seja uma `FormaGeometrica`;
* busca de uma forma inexistente;
* remoção de uma forma inexistente.

17. Utilize pelo menos uma **asserção (`assert`)** para verificar uma pré-condição ou invariante relevante do sistema.

18. Crie uma função ou método de **classe** capaz de construir uma forma a partir de um dicionário de dados, por exemplo:

```python
{"tipo": "circulo", "raio": 5}
```

19. O programa principal deverá:

* criar diferentes formas;
* alterar algumas propriedades;
* demonstrar a validação de valores inválidos;
* armazená-las em um catálogo;
* exibir as formas;
* demonstrar `len()`, `in`, `==` e `<`;
* ordenar as formas;
* calcular a área total;
* identificar a maior forma;
* demonstrar o funcionamento do duck typing;
* demonstrar o tratamento das exceções;
* demonstrar a criação de uma forma a partir de um dicionário.

Restrição: Não utilize bibliotecas externas. O objetivo é que a solução demonstre claramente os conceitos de abstração, encapsulamento, herança, composição, polimorfismo, sobrecarga/sobrescrita de operadores, propriedades, atributos e métodos de classe, métodos abstratos, exceções e duck typing.

'''

from abc import ABC, abstractmethod
from math import pi
from typing import Any


class FormaGeometrica(ABC):
    _quantidade_formas = 0

    def __init__(self, nome: str):
        if not isinstance(nome, str) or not nome.strip():
            raise ValueError("O nome deve ser uma string não vazia.")

        self.__id = FormaGeometrica._quantidade_formas + 1
        self.nome = nome

        FormaGeometrica._quantidade_formas += 1

    @property
    def id(self):
        return self.__id

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("O nome deve ser uma string não vazia.")

        self.__nome = valor

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimetro(self):
        pass

    @classmethod
    def quantidade_formas(cls):
        return cls._quantidade_formas

    def __eq__(self, other):
        if not isinstance(other, FormaGeometrica):
            return NotImplemented

        return self.area() == other.area()

    def __lt__(self, other):
        if not isinstance(other, FormaGeometrica):
            return NotImplemented

        return self.area() < other.area()

    def __str__(self):
        return f"{self.nome} (ID: {self.id})"


class Retangulo(FormaGeometrica):

    def __init__(self, largura: float, altura: float, nome="Retângulo"):
        super().__init__(nome)

        self.largura = largura
        self.altura = altura

    @property
    def largura(self):
        return self.__largura

    @largura.setter
    def largura(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("A largura deve ser numérica.")

        if valor <= 0:
            raise ValueError("A largura deve ser positiva.")

        self.__largura = valor

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("A altura deve ser numérica.")

        if valor <= 0:
            raise ValueError("A altura deve ser positiva.")

        self.__altura = valor

    def area(self):
        return self.largura * self.altura

    def perimetro(self):
        return 2 * (self.largura + self.altura)

    def __str__(self):
        return (
            f"Retângulo {self.id}: "
            f"{self.largura} x {self.altura}, "
            f"área = {self.area():.2f}, "
            f"perímetro = {self.perimetro():.2f}"
        )


class Circulo(FormaGeometrica):

    def __init__(self, raio: float, nome="Círculo"):
        super().__init__(nome)

        self.raio = raio

    @property
    def raio(self):
        return self.__raio

    @raio.setter
    def raio(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O raio deve ser numérico.")

        if valor <= 0:
            raise ValueError("O raio deve ser positivo.")

        self.__raio = valor

    def area(self):
        return pi * self.raio ** 2

    def perimetro(self):
        return 2 * pi * self.raio

    def __str__(self):
        return (
            f"Círculo {self.id}: "
            f"raio = {self.raio}, "
            f"área = {self.area():.2f}, "
            f"perímetro = {self.perimetro():.2f}"
        )

    @classmethod
    def from_dict(cls, dados):
        if not isinstance(dados, dict):
            raise TypeError("Os dados devem estar em um dicionário.")

        if dados.get("tipo") != "circulo":
            raise ValueError("O tipo informado não é círculo.")

        return cls(
            raio=dados["raio"],
            nome=dados.get("nome", "Círculo")
        )


class Triangulo(FormaGeometrica):

    def __init__(
        self,
        lado_a: float,
        lado_b: float,
        lado_c: float,
        nome="Triângulo"
    ):
        super().__init__(nome)

        self.lado_a = lado_a
        self.lado_b = lado_b
        self.lado_c = lado_c

        assert self._eh_triangulo(), "Os lados não formam um triângulo."

    def _validar_lado(self, valor):
        if not isinstance(valor, (int, float)):
            raise ValueError("O lado deve ser numérico.")

        if valor <= 0:
            raise ValueError("O lado deve ser positivo.")

        return valor

    @property
    def lado_a(self):
        return self.__lado_a

    @lado_a.setter
    def lado_a(self, valor):
        self.__lado_a = self._validar_lado(valor)

    @property
    def lado_b(self):
        return self.__lado_b

    @lado_b.setter
    def lado_b(self, valor):
        self.__lado_b = self._validar_lado(valor)

    @property
    def lado_c(self):
        return self.__lado_c

    @lado_c.setter
    def lado_c(self, valor):
        self.__lado_c = self._validar_lado(valor)

    def _eh_triangulo(self):
        return (
            self.lado_a + self.lado_b > self.lado_c
            and self.lado_a + self.lado_c > self.lado_b
            and self.lado_b + self.lado_c > self.lado_a
        )

    def area(self):
        # Fórmula de Heron
        s = self.perimetro() / 2

        return (
            s
            * (s - self.lado_a)
            * (s - self.lado_b)
            * (s - self.lado_c)
        ) ** 0.5

    def perimetro(self):
        return self.lado_a + self.lado_b + self.lado_c

    def __str__(self):
        return (
            f"Triângulo {self.id}: "
            f"lados = ({self.lado_a}, {self.lado_b}, {self.lado_c}), "
            f"área = {self.area():.2f}, "
            f"perímetro = {self.perimetro():.2f}"
        )


class RetanguloColorido(Retangulo):

    def __init__(
        self,
        largura: float,
        altura: float,
        cor: str,
        nome="Retângulo Colorido"
    ):
        super().__init__(largura, altura, nome)

        self.cor = cor

    @property
    def cor(self):
        return self.__cor

    @cor.setter
    def cor(self, valor):
        if not isinstance(valor, str) or not valor.strip():
            raise ValueError("A cor deve ser uma string não vazia.")

        self.__cor = valor

    def __str__(self):
        return (
            f"Retângulo Colorido {self.id}: "
            f"{self.largura} x {self.altura}, "
            f"cor = {self.cor}, "
            f"área = {self.area():.2f}"
        )


class CatalogoFormas:

    _quantidade_catalogos = 0

    def __init__(self):
        self.__formas = []

        CatalogoFormas._quantidade_catalogos += 1

    @property
    def formas(self):
        return self.__formas.copy()

    def adicionar(self, forma):
        if not isinstance(forma, FormaGeometrica):
            raise TypeError(
                "Somente objetos de FormaGeometrica "
                "podem ser adicionados."
            )

        self.__formas.append(forma)

    def remover(self, id_forma):
        for forma in self.__formas:
            if forma.id == id_forma:
                self.__formas.remove(forma)
                return

        raise ValueError("Forma não encontrada.")

    def buscar(self, id_forma):
        for forma in self.__formas:
            if forma.id == id_forma:
                return forma

        raise ValueError("Forma não encontrada.")

    def area_total(self):
        return sum(forma.area() for forma in self.__formas)

    def maior_forma(self):
        if not self.__formas:
            raise ValueError("O catálogo está vazio.")

        return max(self.__formas)

    def formas_ordenadas(self):
        return sorted(self.__formas)

    @classmethod
    def quantidade_catalogos(cls):
        return cls._quantidade_catalogos

    def __len__(self):
        return len(self.__formas)

    def __contains__(self, forma):
        return forma in self.__formas

    def __str__(self):
        if not self.__formas:
            return "Catálogo vazio."

        resultado = "=== CATÁLOGO DE FORMAS ===\n"

        for forma in self.__formas:
            resultado += str(forma) + "\n"

        return resultado


def exibir_area(objeto):
    """
    Demonstra duck typing.

    Não verificamos se o objeto é uma FormaGeometrica.
    Apenas assumimos que ele possui o método area().
    """

    try:
        print(f"Área: {objeto.area():.2f}")

    except AttributeError:
        print("O objeto não possui o método area().")


class ObjetoComArea:

    def __init__(self, valor):
        self.valor = valor

    def area(self):
        return self.valor ** 2


if __name__ == "__main__":

    print("===== CRIAÇÃO DAS FORMAS =====")

    retangulo = Retangulo(
        largura=5,
        altura=3
    )

    circulo = Circulo(
        raio=4
    )

    triangulo = Triangulo(
        lado_a=3,
        lado_b=4,
        lado_c=5
    )

    colorido = RetanguloColorido(
        largura=10,
        altura=2,
        cor="azul"
    )

    print(retangulo)
    print(circulo)
    print(triangulo)
    print(colorido)


    print("\n===== PROPRIEDADES =====")

    print("Raio original:", circulo.raio)

    circulo.raio = 5

    print("Raio alterado:", circulo.raio)
    print("Nova área:", circulo.area())


    print("\n===== TESTE DE VALIDAÇÃO =====")

    try:
        circulo.raio = -10

    except ValueError as erro:
        print("Erro capturado:", erro)


    print("\n===== CATÁLOGO =====")

    catalogo = CatalogoFormas()

    catalogo.adicionar(retangulo)
    catalogo.adicionar(circulo)
    catalogo.adicionar(triangulo)
    catalogo.adicionar(colorido)

    print(catalogo)

    print("Quantidade de formas:", len(catalogo))


    print("\n===== ÁREA TOTAL =====")

    print(
        f"Área total: "
        f"{catalogo.area_total():.2f}"
    )


    print("\n===== MAIOR FORMA =====")

    maior = catalogo.maior_forma()

    print(maior)


    print("\n===== ORDENAÇÃO =====")

    formas_ordenadas = catalogo.formas_ordenadas()

    for forma in formas_ordenadas:
        print(
            f"{forma.nome} -> "
            f"{forma.area():.2f}"
        )


    print("\n===== COMPARAÇÃO =====")

    print(
        "Retângulo == círculo:",
        retangulo == circulo
    )

    print(
        "Retângulo < círculo:",
        retangulo < circulo
    )


    print("\n===== OPERADOR IN =====")

    print(
        "Círculo está no catálogo?",
        circulo in catalogo
    )


    print("\n===== BUSCA =====")

    encontrado = catalogo.buscar(circulo.id)

    print("Forma encontrada:", encontrado)


    print("\n===== REMOÇÃO =====")

    catalogo.remover(triangulo.id)

    print(catalogo)


    print("\n===== TRATAMENTO DE ERRO =====")

    try:
        catalogo.remover(999)

    except ValueError as erro:
        print("Erro capturado:", erro)


    print("\n===== DUCK TYPING =====")

    exibir_area(retangulo)
    exibir_area(circulo)
    exibir_area(ObjetoComArea(7))


    print("\n===== CRIAÇÃO POR DICIONÁRIO =====")

    dados = {
        "tipo": "circulo",
        "raio": 6,
        "nome": "Círculo criado por dicionário"
    }

    circulo_dict = Circulo.from_dict(dados)

    print(circulo_dict)


    print("\n===== ATRIBUTOS DE CLASSE =====")

    print(
        "Quantidade de formas criadas:",
        FormaGeometrica.quantidade_formas()
    )

    print(
        "Quantidade de catálogos criados:",
        CatalogoFormas.quantidade_catalogos()
    )
    

'''
Retorno do terminal:

'''