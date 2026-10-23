# Tópicos

### O que é objeto?

É uma entidade (instância) que possui características (atributos) e comportamentos (métodos).

Pense em um carro.

| Atributos | Comportamentos |
|-----------|----------------|
| Cor | Ligar |
| Modelo | Frear |
| Ano | Acelerar |
| Velocidade | Desligar |

- Resumo: Reunir dados e ações em um único elemento.

Exemplo:

```python
meu_carro = Carro()

# meu_carro é um objeto.
```

---

### O que é classe?

Uma classe é um molde ou modelo utilizado para criar objetos.

Ela define:
- Quais atributos os objetos terão.
- Quais métodos os objetos poderão executar.

**Analogia:**

- Classe: Planta de uma casa.
- Objeto: Casa construída a partir da planta.

Uma única classe pode ser utilizada para criar diversos objetos.

Exemplo:

```python
class Carro:
    pass

# Nesse momento existe apenas o modelo.
# Nenhum objeto foi criado.
```

---

### O que é instanciamento?

Instanciar é o processo de criar um objeto a partir de uma classe.

Exemplo:

```python
class Carro:
    pass

carro1 = Carro()
carro2 = Carro()
```

Neste exemplo:

- `Carro` é uma **classe**.
- `carro1` é um **objeto**.
- `carro2` é outro **objeto**.

Ambos foram criados utilizando o mesmo molde (`Carro`).

---

### Estados dos objetos

O estado de um objeto corresponde aos valores atuais de seus atributos.

Exemplo:

```python
class Carro:
    def __init__(self, cor):
        self.cor = cor
        self.velocidade = 0
```

Criando um objeto:

```python
carro = Carro("Azul")
```

Estado inicial:

| Atributo | Valor |
|----------|-------|
| Cor | Azul |
| Velocidade | 0 km/h |

Após alterar um atributo:

```python
carro.velocidade = 80
```

Novo estado:

| Atributo | Valor |
|----------|-------|
| Cor | Azul |
| Velocidade | 80 km/h |

- Resumo: O estado de um objeto muda sempre que o valor de um de seus atributos é alterado.