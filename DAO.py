from Models import Pessoa, Fornecedor, Venda, Funcionario, Categoria, Estoque, Produto

class PessoaDAO:
    @classmethod
    def salvar(cls, pessoa: Pessoa):
        with open('pessoas.txt', 'a') as arq:
            arq.writelines(pessoa.nome + "|" + str(pessoa.idade) + "|" + pessoa.cpf)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('pessoas.txt', 'r') as arq:
            cls.pessoa = arq.readlines()
        
        cls.pessoa = list(map(lambda x: x.replace('\n', ''), cls.pessoa))
        cls.pessoa = list(map(lambda x: x.split('|'), cls.pessoa))
        print(cls.pessoa)
        clientes = []
        for i in cls.pessoa:
            clientes.append(Fornecedor(i[0], i[1], i[2], i[3], i[4]))
        return clientes

class FornecedorDAO:
    @classmethod
    def salvar(cls, fornecedor: Fornecedor):
        with open('fornecedor.txt', 'a') as arq:
            arq.writelines(fornecedor.nome + "|" + fornecedor.cnpj + "|" + fornecedor.telefone + "|" + fornecedor.categoria)
            arq.writelines('\n')
    
    def ler(cls):
        with open('fornecedor.txt',  'r') as arq:
            cls.fornecedor = arq.readlines()

        cls.fornecedor = list(map(lambda x: x.replace('\n', ''), cls.fornecedor))
        cls.fornecedor = list(map(lambda x: x.split('|'), cls.fornecedor))
        forn = []
        for i in cls.fornecedor:
            forn.append(Fornecedor(i[0], i[1], i[2], i[3]))
        return forn

class ProdutoDAO:
    @classmethod
    def salvar(cls, produto: Produto):
        with open('produto.txt', 'a') as arq:
            arq.writelines(produto.nome + "|" + produto.preco + "|" + produto.categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('produto.txt', 'r') as arq:
            cls.produto = arq.readlines()
            print(cls.produto)

        cls.produto = list(map(lambda x: x.replace('\n', ''), cls.produto))
        cls.produto = list(map(lambda x: x.split('|'), cls.produto)) 

class VendaDAO:
    @classmethod
    def salvar(cls, venda: Venda):
        with open('venda.txt', 'a') as arq:
            arq.writelines(venda.itensVendido.nome + "|" + venda.itensVendido.preco + "|" + venda.itensVendido.categoria + "|"
                           + venda.vendedor + "|" + venda.comprador + "|" + str(venda.quantidadeVendida) + "|" + venda.data)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('venda.txt', 'r') as arq:
            cls.venda = arq.readlines()
            print(cls.venda)

        cls.venda = list(map(lambda x: x.replace('\n', ''), cls.venda))
        cls.venda = list(map(lambda x: x.split('|'), cls.venda))
        print(cls.venda)
        vend = []
        for i in cls.venda:
            vend.append(Venda(Produto(i[0], i[1], i[2]), i[3], i[4], i[5]))
        return vend

class FuncionarioDAO:
    @classmethod
    def salvar(cls, funcionario: Funcionario):
        with open('funcionario.txt', 'a') as arq:
            arq.writelines(funcionario.clt + "|" + funcionario.nome + "|" + funcionario.idade + "|" + funcionario.cpf)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('funcionario.txt', 'r') as arq:
            cls.venda = arq.readlines()
            print(cls.funcionario)

        cls.funcionario = list(map(lambda x: x.replace('\n', ''), cls.funcionario))
        cls.funcionario = list(map(lambda x: x.split('|'), cls.funcionario))
        funcionario = []
        for i in cls.funcionario:
            funcionario.append(Funcionario(i[0], i[1], i[2], i[3], i[4], i[5]))

class CategoriaDAO:
    @classmethod
    def salvar(cls, categoria):
        with open('categoria.txt', 'a') as arq:
            arq.writelines(categoria)
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('categoria.txt', 'r') as arq:
            cls.categoria = arq.readlines()

        cls.categoria = list(map(lambda x: x.replace('\n', ''), cls.categoria))

        cat = []   
        for i in cls.categoria:
            cat.append(Categoria(i))
        return cat

class EstoqueDAO:
    @classmethod
    def salvar(cls, produto: Produto, quantidade):
        with open('estoque.txt', 'a') as arq:
            arq.writelines(produto.nome + "|" + produto.preco + "|" + produto.categoria + "|"
                           + str(quantidade))
            arq.writelines('\n')

    @classmethod
    def ler(cls):
        with open('estoque.txt', 'r') as arq:
            cls.estoque = arq.readlines()
            #print(cls.estoque)

        cls.estoque = list(map(lambda x: x.replace('\n', ''), cls.estoque))
        cls.estoque = list(map(lambda x: x.split('|'), cls.estoque))
        est = []
        if len(cls.estoque) > 0:
            for i in cls.estoque:
                est.append(Estoque(Produto(i[0], i[1], i[2]), i[3]))
        return est


#x = VendaDAO.ler()
#print(x)