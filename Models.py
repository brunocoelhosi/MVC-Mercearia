#caracteristicas dos dados (classes)
from datetime import datetime
class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.categoria = categoria

class Pessoa:
    def __init__(self, nome: str, idade: int, cpf: str):
        self.nome = nome
        self.idade = idade
        self.cpf = cpf

class Funcionario(Pessoa):
    def __init__(self, clt, nome, idade, cpf):
        self.clt = clt
        super(Funcionario, self).__init__(nome,idade,cpf)

class Categoria:
    def __init__(self, categoria):
        self.categoria = categoria

class Produto:
    def __init__(self, nome, preco, categoria):
        self.nome = nome
        self.preco = preco
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produto, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itensVendido: Produto, vendedor, comprador, quantidadeVendida, data = datetime.now().strftime("%d/%m/%Y")):
        self.itensVendido = itensVendido
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data



