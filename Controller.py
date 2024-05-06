from DAO import PessoaDAO, FornecedorDAO, CategoriaDAO, EstoqueDAO, VendaDAO,FuncionarioDAO
from Models import Pessoa, Fornecedor, Categoria, Estoque, Produto, Venda, Funcionario
from datetime import datetime

class FornecedorController:
    def cadastrarFornecedor(self, nome, cnpj, telefone, categoria):
        x = FornecedorDAO.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.cnpj == cnpj, x))
        if len(listaCnpj) > 0:
            print("O cnpj já existe")
        elif len(listaTelefone) > 0:
            print('O telefone já existe')
        else:
            if len(cnpj)  == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                FornecedorDAO.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print("Digite um cnpj ou telefone válido")

    def alterarFornecedor(self, nomeAlterar, novoNome, novoCnpj, novoTelefone, novoCategoria):
        x = FornecedorDAO.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            est = list(filter(lambda x: x.cnpj == novoCnpj, x))
            if len(est) == 0:
                x = list(map(lambda x: Fornecedor(novoNome, novoCnpj, novoTelefone, novoCategoria) if(x.nome == nomeAlterar) else(x),x))
            else:
                print('Cnpj já existe')
        else:
            print('O fornecedor que deseja alterar nao existe')

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines('\n')
            print('fornecedor alterado com sucesso')

    def removerFornecedor(self, nome):
        x = FornecedorDAO.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('O fornecedor que deseja remover não existe')
            return None

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines('\n')
            print('Fornecedor removido com sucesso')

    def mostrarFornecedores(self):
        fornecedores = FornecedorDAO.ler()
        if len(fornecedores) == 0:
            print("Lista de fornecedores vazia")

        for i in fornecedores:
            print("=========Fornecedores==========")
            print(f"Categoria fornecida: {i.categoria}\n"
                  f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Cnpj: {i.cnpj}")

class CategoriaController:
    def cadastrarCategoria(self, novaCategoria):
        existe = False
        x = CategoriaDAO.ler()
        for i in x:
            if i.categoria == novaCategoria:
                 existe = True
        if not existe:
            CategoriaDAO.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso!')
        else:
            print('Categoria ja existente')

    
    def removerCategoria(self, deleteCategoria):

        x = CategoriaDAO.ler()
        cat = list(filter(lambda x: x.categoria == deleteCategoria, x))
        
        if len(cat) <= 0:
            print('Categoria não existente')
        else:
            for i in range(len(x)):
                if x[i].categoria == deleteCategoria:
                    del x[i]
                    break            
            print('Categoria removida com sucesso!')
        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

        estoque = EstoqueDAO.ler()

        estoque = list(map(lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, "sem categoria"), x.quantidade)
                                             if (x.produto.categoria == deleteCategoria) else (x), estoque))
        
        with open('estoque','w') as arq:
            for i in estoque:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(i.quantidade))
                arq.writelines("\n")

            
    def alterarCategoria(self, categoriaAlterar, categoriaAlterada):
        x = CategoriaDAO.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x) ,x))
                print('A altereção foi efetuada com sucesso')

                estoque = EstoqueDAO.ler()

                estoque = list(map(
                    lambda x: Estoque(Produto(x.produto.nome, x.produto.preco, categoriaAlterada), x.quantidade) if (
                                x.produto.categoria == categoriaAlterar) else (x), estoque))
                with open('estoque.txt', 'w') as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(
                            i.quantidade))
                        arq.writelines("\n")

            else:
                print("A categoria para qual deseja alterar já existe")

        else:
            print('A categoria que deseja alterar não existe')

        with open('categoria.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')
    
    def monstrarCategoria(self):
        categorias = CategoriaDAO.ler()
        if len(categorias) == 0:
            print('Nao existe categorias cadastradas')
        else:
            print('Categorias Cadastradas\n')
            for i in categorias:
                print(f'Categoria: {i.categoria}')

class EstoqueController:
    def CadastraEstoque(self, nome, preco, categoria, quantidade):
        x = EstoqueDAO.ler()
        y = CategoriaDAO.ler()
        h = list(filter(lambda y: y.categoria == categoria, y))            
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produto = Produto(nome,preco,categoria)
                EstoqueDAO.salvar(produto, quantidade)
                print('produto cadastrado com sucesso')
            else:
                print('produto ja exite em estoque')
        else:
            print('categoria inexistente')

    def RemoverProduto(self, nome):

        x = EstoqueDAO.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        
        if len(est) <= 0:
            print('Produto não existente')
        else:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break            
            print('Produto removido com sucesso!')
        with open('estoque.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(
                            i.quantidade))
                arq.writelines('\n')

    def AlterarProduto(self, produtoAlterar, novoProduto, novoPreco, novaCategoria, novaQuantidade):

        x = EstoqueDAO.ler()
        y = CategoriaDAO.ler()

        h = list(filter(lambda x: x.categoria == novaCategoria, y))

        if len(h)>0:
            est = list(filter(lambda x: x.produto.nome == produtoAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoProduto, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produto(novoProduto, novoPreco, novaCategoria),novaQuantidade)
                                 if (x.produto.nome == produtoAlterar) else (x), x))
                    print('produto alterado com sucesso')
                else:
                    print('produto ja cadastrado')
            else:
                print('o produto que deseja alterar nao existe')

            with open('estoque.txt', 'w') as arq:
                for i in x:
                    arq.writelines(i.produto.nome + "|" + i.produto.preco + "|" + i.produto.categoria + "|" + str(
                                i.quantidade))
                    arq.writelines('\n')

        else:
            print('categoria nao existe')

    def mostrarEstoque(self):
        estoque = EstoqueDAO.ler()
        if len(estoque) == 0:
            print('Nao existe produtos no estoque')
        else:
            print("-------- Produto --------")
            for i in estoque:
                
                print(f'Estoque: {i.produto.nome}')
                print(f'Preco: {i.produto.preco}')
                print(f'Categoria: {i.produto.categoria}')
                print(f'Quantidade: {i.quantidade}\n')

class VendaController:
    def CadastraVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = EstoqueDAO.ler()
        temp = []
        existe = False
        quantidade = False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if int(i.quantidade) >= int(quantidadeVendida):
                        quantidade = True
                        i.quantidade = int(i.quantidade) - int(quantidadeVendida)

                        vendido = Venda(Produto(i.produto.nome, i.produto.preco, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                        valorCompra = int(quantidadeVendida) * int(i.produto.preco)

                        VendaDAO.salvar(vendido)
            
            temp.append([Produto(i.produto.nome, i.produto.preco, i.produto.categoria),i.quantidade])
        
        arq = open('estoque.txt','w')
        arq.write("")

        for i in temp:
            with open('estoque.txt','a') as arq:
                arq.writelines(i[0].nome + "|" + i[0].preco + "|" + i[0].categoria + "|" + int(i[1]))
                arq.writelines('\n')

        if existe == False:
            print('produto nao existe')
            return None
        elif not quantidade:
            print('quantidade insuficiente')
        else: 
            print(f'Venda realizada com sucesso - Valor total da compra:{valorCompra}')
            return valorCompra

    def relatorioProdutos(self):
        vendas = VendaDAO.ler()
        produtos = []
        for i in vendas:
            nome = i.itensVendido.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho)>0:
                produtos = list(map(lambda x: {'produto': nome, 'quantidade': int(x['quantidade']) + int(quantidade)}
                if (x['produto'] == nome) else(x), produtos))
            else:
                produtos.append({'produto': nome, 'quantidade': int(quantidade)})

        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

        print('Esses são os produtos mais vendidos')
        a = 1
        for i in ordenado:
            print(f"==========Produto [{a}]==========")
            print(f"Produto: {i['produto']}\n"
                  f"Quantidade: {i['quantidade']}\n")
            a += 1

    def mostrarTodasVendas(self):

        vendas = VendaDAO.ler()
        if len(vendas) == 0:
            print("nenhum venda foi realizada")

        for i in vendas:
            print(f'Produto: {i.itensVendido.nome}')
            print(f'Data venda: {i.data}\n')

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = VendaDAO.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1 and datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))

        cont = 1
        total = 0
        for i in vendasSelecionadas:
            print(f"==========Venda [{cont}]==========")
            print(f"Nome: {i.itensVendido.nome}\n"
                f"Categoria: {i.itensVendido.categoria}\n"
                f"Data: {i.data}\n"
                f"Quantidade: {i.quantidadeVendida}\n"
                f"Cliente: {i.comprador}\n"
                f"Vendedor: {i.vendedor}\n")
            total += int(i.itensVendido.preco) * int(i.quantidadeVendida)
            cont += 1

        print(f"Total vendido: {total}")

class ClienteController:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = PessoaDAO.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print('CPF já existente')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                PessoaDAO.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente Cadastrado com sucesso')
            else:
                print('digite um cpf ou telefone válido')

    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = PessoaDAO.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if (
                        x.nome == nomeAlterar) else (x), x))
        else:
            print('O cliente que deseja alterar nao existe')

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('cliente alterado com sucesso')

    def removerCliente(self, nome):
        x = PessoaDAO.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('O cliente que deseja remover não existe')
            return None

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('Cliente removido com sucesso')

    def mostrarClientes(self):
        clientes = PessoaDAO.ler()

        if len(clientes) == 0:
            print("Lista de clientes vazia")

        for i in clientes:
            print("=========Cliente=========")
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Endereço: {i.endereco}\n"
                  f"Email: {i.email}\n"
                  f"CPF: {i.cpf}")

class FuncionarioController:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = FuncionarioDAO.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))
        if len(listaCpf) > 0:
            print('CPF já existente')
        elif len(listaClt) > 0:
            print('Já existe um funcionario com essa clt')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                FuncionarioDAO.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionario Cadastrado com sucesso')
            else:
                print('digite um cpf ou telefone válido')

    def alterarFuncionario(self, nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = FuncionarioDAO.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novoClt,novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if (
                    x.nome == nomeAlterar) else (x), x))
        else:
            print('O funcionario que deseja alterar nao existe')

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email
                               + "|" + i.endereco)
                arq.writelines('\n')
            print('funcionario alterado com sucesso')

    def removerFuncionario(self, nome):
        x = FuncionarioDAO.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('O funcionario que deseja remover não existe')
            return None

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('Funcionarios removido com sucesso')

    def mostrarFuncionarios(self):
        funcionario = FuncionarioDAO.ler()

        if len(funcionario) == 0:
            print("Lista de funcionarios vazia")

        for i in funcionario:
            print("========Funcionario==========")
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Email: {i.email}\n"
                  f"Endereço: {i.endereco}\n"
                  f"CPF: {i.cpf}\n"
                  f"CLT: {i.clt}\n")
#a = CategoriaController()
#a.cadastraCategoria('Pao')
#a.removerCategoria('Pao')
#a.alterarCategoria('Fruta','Bolo')
#a.monstrarCategoria()
            
#b = EstoqueController()
#b.CadastraEstoque('Pao de queijo', '1', 'Pao', '10')
#b.mostrarEstoque()
#b.CadastraEstoque('Pao de doce', '1', 'Pao', '10')
#b.RemoverProduto('Pao de queijo')
#b.AlterarProduto('Pao de doce', 'Pao sovado','10','Pao','10')
#c = VendaController()
#c.CadastraVenda('Pao de queijo','mariana','bruno',1)
#c.relatorioProdutos()
#c.mostrarVenda("01/03/2024","19/03/2024")


