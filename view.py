import Controller
import os.path

def criaArquivos(*args):
    for i in args:
        if not os.path.exists(i):
            with open(i, "w") as arq:
                arq.write("")

criaArquivos("categoria.txt","estoque.txt","fornecedor.txt","funcionarios.txt","venda.txt","clientes.txt")

if __name__ == "__main__":

    while True:
        print('\n 1 - Categoria \n2 - Fornecedor \n3 - Produto \n4 - Cliente \n5 - Funcionario')

        menu = int(input())
        
        if menu == 1:

            print('\n1 - Cadastrar Categoria \n2 - Alterar Categproa \n3 - Excluir Categoria\n4 - mostrarCategoria')
            cat = Controller.CategoriaController()
            submenu = int(input())
            if submenu == 1:
                nome = input('Digite o nome da categoria\n')
                cat.cadastrarCategoria(nome)

            elif submenu == 2:
                nomeAntigo = input('Digite o nome da categoria que deseja alterar\n')
                nomeNovo = input('Digite o novo nome para a categoria\n')
                cat.cadastrarCategoria(nomeAntigo,nomeNovo)

            elif submenu == 3:
                nome = input('Digite o nome da categoria\n')
                cat.removerCategoria(nome)

            elif submenu == 4:
                cat.monstrarCategoria()

        elif menu == 2:
            print('\n1 - Cadastrar Fornecedor \n2 - Alterar Fornecedor \n3 - Excluir Fornecedor')

            submenu = int(input())
            if submenu == 1:
                nome = input('Digite o nome\n')
                cnpj = input('Digite o cnpj\n')
                telefone = input('Digite o telefone\n')
                categoria = input('Digite a categoria\n')
                FornecedorController.cadastrarFornecedor(nome, cnpj, telefone, categoria)

            elif submenu == 2:
                print('alt')
            elif submenu == 3:
                print('exc')

        elif menu == 3:
            print('\n1 - Cadastrar Fornecedor \n2 - Alterar Fornecedor \n3 - Excluir Fornecedor')
            submenu = int(input())
            if submenu == 1:
                nome = input('Digite o nome\n')
                cnpj = input('Digite o cnpj\n')
                telefone = input('Digite o telefone\n')
                categoria = input('Digite a categoria\n')
                FornecedorController.Cadastrar(nome, cnpj, telefone, categoria)

            elif submenu == 2:
                print('alt')
            elif submenu == 3:
                print('exc')

        elif menu == 4:
            cat = Controller.FuncionarioController()
            print('\n1 - Cadastrar Funcionario \n2 - Alterar Funcionario \n3 - Excluir Funcionario')
            submenu = int(input())
            if submenu == 1:
                nome = input('Digite o nome\n')
                idade = input('Digite a idade\n')
                cpf = input('Digite o cpf\n')
                cat.cadastrarFuncionario(nome, idade,cpf)

            elif submenu == 2:
                print('exc')
            elif submenu == 3:
                print('exc')

        else:
            0
