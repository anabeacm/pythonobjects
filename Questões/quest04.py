'''
Questão 4 — Produto
Crie uma classe Produto contendo:
    Nome
    Preço
    Quantidade

Depois:
    Cadastre cinco produtos.
    Crie um método para atualizar o preço.
    Crie outro para mostrar os dados do produto.
    Atualize o preço de dois produtos.
'''

class Produto:
    def __init__(self, nome, preco, qtd):

        self.nome = nome
        self.preco = preco
        self.qtd = qtd

    def atPreco(self, preco):
        self.preco = preco

    def dados(self):
        return f"O produto {self.nome}, custa {self.preco} reais e temos {self.qtd} unidades em estoque"
    

arroz = Produto("Arroz", 30, 45)
feijao = Produto("Feijão", 40, 46)
macarrao = Produto("Macarrão", 50, 47)
bandOvo = Produto("Bandeja de ovo", 60, 48)
cebola = Produto("Cebola", 25.00, 49)

print("\nDados atuais do estoque:")
print(arroz.dados())
print(feijao.dados())
print(macarrao.dados())
print(bandOvo.dados())
print(cebola.dados())

arroz.atPreco(50)
macarrao.atPreco(80)

print("\nDados atuais do estoque:")
print(arroz.dados())
print(feijao.dados())
print(macarrao.dados())
print(bandOvo.dados())
print(cebola.dados())


'''
Retorno do terminal:

Dados atuais do estoque:
O produto Arroz, custa 30 reais e temos 45 unidades em estoque
O produto Feijão, custa 40 reais e temos 46 unidades em estoque
O produto Macarrão, custa 50 reais e temos 47 unidades em estoque
O produto Bandeja de ovo, custa 60 reais e temos 48 unidades em estoque
O produto Cebola, custa 25.0 reais e temos 49 unidades em estoque

Dados atuais do estoque:
O produto Arroz, custa 50 reais e temos 45 unidades em estoque
O produto Feijão, custa 40 reais e temos 46 unidades em estoque
O produto Macarrão, custa 80 reais e temos 47 unidades em estoque
O produto Bandeja de ovo, custa 60 reais e temos 48 unidades em estoque
O produto Cebola, custa 25.0 reais e temos 49 unidades em estoque
'''