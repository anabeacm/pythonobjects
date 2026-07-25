'''
Questão 14 — Sistema de Hotel:

Implemente as classes Quarto e Hotel para simular um sistema simples de reservas.

1. Atributos das Classes

Quarto:
    numero (int): Número do quarto.
    capacidade (int): Quantidade máxima de hóspedes.
    ocupado (bool): Indica se o quarto está ocupado (inicia como False).

Hotel:
    nome (string): Nome do hotel.
    quartos (list): Lista de objetos da classe Quarto (deve iniciar vazia).

2. Métodos

Classe Quarto:
    reservar(): Marca o quarto como ocupado caso esteja livre. Caso contrário, exibe uma mensagem informando que o quarto já está ocupado.
    liberar(): Marca o quarto como disponível.
    exibir_dados(): Exibe o número do quarto, sua capacidade e sua situação (Livre ou Ocupado).

Classe Hotel:
    adicionar_quarto(quarto): Adiciona um objeto Quarto ao hotel.
    listar_quartos(): Exibe os dados de todos os quartos.
    procurar_quarto(numero): Busca um quarto pelo número e retorna o objeto encontrado (ou exibe uma mensagem caso não exista).
    listar_disponiveis(): Exibe apenas os quartos que estão livres.
    listar_ocupados(): Exibe apenas os quartos que estão ocupados.

3. Execução

    Crie um hotel.
    Instancie pelo menos cinco quartos.
    Adicione todos ao hotel.
    Reserve dois quartos.
    Tente reservar novamente um dos quartos já ocupados.
    Libere um dos quartos ocupados.
    Liste todos os quartos.
    Liste apenas os quartos disponíveis.
'''

'''
Retorno do terminal:

'''