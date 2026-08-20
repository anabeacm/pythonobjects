'''
Questão — Sistema de Gerenciamento de Biblioteca

Desenvolva, em Python, um sistema orientado a objetos para gerenciamento de uma biblioteca. 
O sistema deverá demonstrar abstração, encapsulamento, herança, polimorfismo, composição, métodos especiais, tratamento de erros e diferentes tipos de membros de classe.

1. Classe abstrata - `ItemBiblioteca` utilizando `ABC`. Ela deverá possuir:

- Um identificador único;
- Uma propriedade `titulo`;
- Uma propriedade `ano_publicacao`;
- Um método abstrato `calcular_multa(dias_atraso)`;
- Um método abstrato `tipo_item()`.

2. Classes derivadas: `Livro`; `Revista`; `DVD`.

Todas deverão herdar de `ItemBiblioteca` e implementar os métodos abstratos adequadamente.

Cada tipo deverá possuir pelo menos um atributo específico:

- `Livro`: `autor` e `numero_paginas`;
- `Revista`: `edicao`;
- `DVD`: `duracao_minutos`.

3. Encapsulamento: Utilize encapsulamento nos atributos internos.

Informações como título, ano de publicação, número de páginas, edição e duração não poderão ser alteradas diretamente sem validação.

4. Utilize `@property` e `@setter` para controlar o acesso aos atributos.

Valores inválidos deverão gerar `ValueError`.

Considere, por exemplo:

- Título não pode ser vazio;
- Ano de publicação não pode ser negativo;
- Número de páginas deve ser maior que zero;
- Edição deve ser maior que zero;
- Duração deve ser maior que zero.

5. Crie uma classe `Biblioteca`, responsável por armazenar vários objetos `ItemBiblioteca`.

A classe deverá utilizar composição, mantendo internamente uma coleção de objetos `ItemBiblioteca`.

6. A classe `Biblioteca` deverá possuir métodos para:

- Adicionar um item;
- Remover um item pelo identificador;
- Buscar um item pelo identificador;
- Buscar itens pelo título;
- Calcular a soma das multas de todos os itens para uma determinada quantidade de dias de atraso;
- Retornar o item que possui a maior multa;
- Retornar todos os itens ordenados pelo ano de publicação.

7. Atributo de classe `Biblioteca`: Responsável por contabilizar quantas bibliotecas foram criadas.

Crie também um `@classmethod` que permita consultar essa quantidade.

8. Implemente `__str__` em todas as classes de itens.

Ao utilizar:

```python
print(item)
```
deverá ser exibida uma representação adequada do objeto.

A representação deverá ser diferente para cada tipo de item.

9. Implemente `__eq__` para comparar dois itens da biblioteca.

Dois itens deverão ser considerados iguais quando possuírem o mesmo identificador.

10. Implemente `__lt__` para permitir a comparação entre itens.

A comparação deverá considerar o ano de publicação.

Assim, deverá ser possível fazer:

```python
item1 < item2
```
e ordenar uma coleção de itens utilizando:

```python
sorted(itens)
```

11. Implemente `__len__` na classe `Biblioteca`.

Assim:

```python
len(biblioteca)
```
deverá retornar a quantidade de itens armazenados.

12. Implemente `__contains__` para permitir verificar se um item está presente na biblioteca utilizando o operador:

```python
item in biblioteca
```

A verificação deverá utilizar a igualdade definida em `__eq__`.

13. Polimorfismo e duck typing

Crie uma função:

```python
def calcular_multa_item(objeto, dias):
```

A função deverá receber qualquer objeto que possua o método:

```python
calcular_multa()
```
Ela não deverá verificar explicitamente se o objeto é `Livro`, `Revista` ou `DVD`. O objetivo é demonstrar duck typing.

14. Crie uma classe `LivroDigital` que herde de `Livro`.

Ela deverá acrescentar uma propriedade:

```python
formato
```
que poderá receber valores como `"PDF"`, `"EPUB"` ou `"MOBI"`.

A classe deverá sobrescrever `__str__` para incluir o formato do livro digital.

15. Utilize `super()` corretamente em `LivroDigital`, reutilizando o construtor ou algum comportamento da classe `Livro`.

16. Cada tipo de item deverá possuir uma regra diferente para cálculo de multa:

- `Livro`: R$ 2,00 por dia de atraso;
- `Revista`: R$ 1,00 por dia de atraso;
- `DVD`: R$ 4,00 por dia de atraso;
- `LivroDigital`: não possui multa.

O método `calcular_multa()` deverá ser implementado individualmente nas classes, demonstrando polimorfismo.

17. Utilize tratamento de exceções para situações como:

- Tentativa de criar um item com dados inválidos;
- Tentativa de adicionar à biblioteca algo que não seja um `ItemBiblioteca`;
- Busca de item inexistente;
- Remoção de item inexistente;
- Tentativa de utilizar quantidade negativa de dias de atraso.

Utilize exceções apropriadas, como `ValueError`, `TypeError` ou `KeyError`, quando necessário.

18. Utilize pelo menos uma asserção (`assert`) para verificar uma pré-condição ou invariante relevante do sistema.

Por exemplo, uma condição relacionada à quantidade de itens ou aos dias de atraso.

19. Crie uma função ou método de classe capaz de construir diferentes tipos de itens a partir de um dicionário.

Por exemplo:
```python
{
    "tipo": "livro",
    "titulo": "Dom Casmurro",
    "ano": 1899,
    "autor": "Machado de Assis",
    "paginas": 256
}
```

Outro exemplo:
```python
{
    "tipo": "dvd",
    "titulo": "Interestelar",
    "ano": 2014,
    "duracao": 169
}
```

O sistema deverá identificar o tipo e criar o objeto correspondente.

20. No programa principal, deverá ser demonstrado o funcionamento completo do sistema.

O programa deverá:

- Criar diferentes tipos de itens;
- Criar pelo menos um `Livro`, `Revista`, `DVD` e `LivroDigital`;
- Alterar propriedades utilizando setters;
- Demonstrar a validação de valores inválidos;
- Armazenar os objetos em uma `Biblioteca`;
- Exibir os objetos utilizando `print()`;
- Demonstrar `len()`;
- Demonstrar o operador `in`;
- Demonstrar `==`;
- Demonstrar `<`;
- Ordenar os itens;
- Calcular multas para diferentes quantidades de dias;
- Identificar o item com maior multa;
- Demonstrar o polimorfismo;
- Demonstrar o duck typing;
- Demonstrar o tratamento das exceções;
- Demonstrar a criação de objetos a partir de dicionários;
- Consultar a quantidade de bibliotecas criadas utilizando o `@classmethod`.

Restrição

Não utilize bibliotecas externas.

Objetivo: desenvolver um sistema completo em POO, evitando soluções puramente procedurais e fazendo com que cada classe tenha responsabilidades bem definidas.

'''


'''
1. Classe abstrata - `ItemBiblioteca` utilizando `ABC`. Ela deverá possuir:

- Um identificador único;
- Uma propriedade `titulo`;
- Uma propriedade `ano_publicacao`;
- Um método abstrato `calcular_multa(dias_atraso)`;
- Um método abstrato `tipo_item()`.

'''

# Informações como título, ano de publicação, número de páginas, edição e duração não poderão ser alteradas diretamente sem validação.

class ItemBiblioteca:
    def __init__(self, titulo, ano_publicacao):
        self.__titulo = titulo
        self.__ano_publicacao = ano_publicacao

    def calcular_multa(self, dias_atraso):
        pass

    def tipo_item(self):
        pass

'''
2. Classes derivadas: `Livro`; `Revista`; `DVD`.

Todas deverão herdar de `ItemBiblioteca` e implementar os métodos abstratos adequadamente.

Cada tipo deverá possuir pelo menos um atributo específico:

- `Livro`: `autor` e `numero_paginas`;
- `Revista`: `edicao`;
- `DVD`: `duracao_minutos`.
'''

class Livro:
    def __init__(self, autor, numero_paginas):
        self._autor = autor
        self.__numero_paginas = numero_paginas

class Revista:
    def __init__(self, edicao):
        self.__edicao = edicao

class DVD:
    def __init__(self, duracao_minutos):
        self.__duracao = duracao_minutos

'''
4. Utilize `@property` e `@setter` para controlar o acesso aos atributos.

Valores inválidos deverão gerar `ValueError`.

Considere, por exemplo:

- Título não pode ser vazio;
- Ano de publicação não pode ser negativo;
- Número de páginas deve ser maior que zero;
- Edição deve ser maior que zero;
- Duração deve ser maior que zero.

'''

