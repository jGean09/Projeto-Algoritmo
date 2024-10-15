import os
from biblioteca.dados import carregarDados, salvarDados
from biblioteca.datetime import obter_data_atual
from biblioteca.geradorId import gerarNovoID
from Estoque.produtos import alterarQuantidadeProduto, buscarProdutoPorCodigo, carregarDados, exibirproduto, relatorioGeralProdutos, retorna_nome_produto, retorna_quantidade_produto
from Funcionarios.funcionario import buscarFuncionarioPorCPF, exibirFuncionario, relatorioFuncionarios
from telas.telasMovimentacao import telaCadastroMovimentacao, telaMovimentacao

NomeDadosMovimentacao = "movimentacao.dat"
movimentacao = carregarDados(NomeDadosMovimentacao)
produto = carregarDados("Produtos.dat")


def cadastrarmivmentacaoDevolver():
    validar_movimentacao = False
    validar_quantidade = False
    validar_produto = False

    relatoriomovimentacao()
    while True:
        try:
            codigo = int(
                input("Qual é o código da movimentação que deseja devolver? "))
            if codigo in movimentacao:
                exibirmv(movimentacao, codigo)
                validar_movimentacao = True
                break
            else:
                print("Movimentação não encontrada.")
                input("Tecle <ENTER> para continuar...")
                os.system('clear')
        except ValueError:
            print("Código inválido! Por favor, digite um número inteiro.")
    print()
    quantidade_retirada = movimentacao[codigo][1]
    quantidade_devolvida = movimentacao[codigo][4]
    while True:
        try:
            qta_devolver = int(
                input("Informe a quantidade que deseja devolver: "))
            if qta_devolver >= 0 and qta_devolver <= quantidade_retirada - quantidade_devolvida:
                validar_quantidade = True
                break
            else:
                if qta_devolver > quantidade_retirada - quantidade_devolvida:
                    print(
                        "Quantidade inválida! Não pode devolver mais do que foi retirado."
                    )
                else:
                    print(
                        "Quantidade inválida. Por favor, insira um número inteiro válido."
                    )
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    # Busca o código do produto
    for prod_codigo, prod_dados in produto.items():
        if prod_dados[0] == movimentacao[codigo][0]:
            codigo_produto = prod_codigo
            validar_produto = True
            break
    else:
        print("Produto não encontrado no estoque.")

    # Se todas validares
    if validar_movimentacao and validar_quantidade and validar_produto:
        movimentacao[codigo][4] += qta_devolver
        salvarDados(NomeDadosMovimentacao, movimentacao)
        alterarQuantidadeProduto(codigo_produto, qta_devolver)

        if qta_devolver < quantidade_retirada:
            print(
                f"Devolução realizada com sucesso! Faltam {quantidade_retirada - qta_devolver - quantidade_devolvida} produtos para serem devolvidos."
            )
        else:
            print(
                "Devolução realizada com sucesso! Todos os produtos foram devolvidos."
            )
    else:
        print("Erro na devolução. Verifique as informações e tente novamente.")

    input("Tecle <ENTER> para continuar...")


def cadastrarmovimentacaoRetirada():
    validarproduto = False
    validarquantidade = False
    validarfuncionario = False

    telaCadastroMovimentacao()
    codmov = gerarNovoID("IDs.dat")
    data = obter_data_atual()
    relatorioGeralProdutos()
    print()

    produto = carregarDados("Produtos.dat")

    while True:
        try:
            codigo_retirar = int(
                input(
                    "Qual Código do Produto que Deseja retirar do estoque? "))
            print("Código do produto fornecido:", codigo_retirar)
            if codigo_retirar in produto:
                exibirproduto(produto, codigo_retirar)
                validarproduto = True
                break
            else:
                print(
                    "Código inválido! Por favor, digite um número inteiro válido."
                )
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    nome_produto_retirado = retorna_nome_produto(produto, codigo_retirar)
    quantidade_antiga = retorna_quantidade_produto(produto, codigo_retirar)

    while True:
        try:
            qta_retirar = int(
                input("Informe a quantidade que deseja retirar: "))
            if validarproduto and qta_retirar <= quantidade_antiga:
                validarquantidade = True
                break
            else:
                print("Quantidade insuficiente no estoque.")
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    relatorioFuncionarios()
    while True:
        CPF = input("Informe o CPF do Funcionário Responsável: ")
        funcionarios = buscarFuncionarioPorCPF(CPF)
        if funcionarios:
            exibirFuncionario(funcionarios, CPF)
            Nome_funcionario_responsavel = funcionarios[CPF][0]
            validarfuncionario = True
            break
        else:
            print("Funcionário não encontrado.")

    if validarproduto and validarquantidade and validarfuncionario:
        quantidade_nova = quantidade_antiga - qta_retirar

        quantidade_devolvida = 0  
        movimentacao[codmov] = [
            nome_produto_retirado, qta_retirar, data,
            Nome_funcionario_responsavel, quantidade_devolvida
        ]
        salvarDados(NomeDadosMovimentacao, movimentacao)

        alterarQuantidadeProduto(codigo_retirar, quantidade_nova)

        print("Movimentação cadastrada com sucesso!")
        input("Tecle <ENTER> para continuar...")
    else:
        print("Algo deu errado, volte ao menu principal")
        input("Tecle <ENTER> para continuar...")


def exibirmv(movimentacao, codigo):
    print("Código da movimentação:", codigo)
    print("Nome do produto:", movimentacao[codigo][0])
    print("Quantidade retirada:", movimentacao[codigo][1])
    print("Data da movimentação:", movimentacao[codigo][2])
    print("Nome do funcionário responsável:", movimentacao[codigo][3])
    print("Quantidade devolvida:", movimentacao[codigo][4])
    print()


def buscarmovimentacao():
    relatoriomovimentacao()
    while True:
        try:
            codigo = int(
                input("Qual é o código da movimentação que deseja buscar? "))
            if codigo in movimentacao:
                exibirmv(movimentacao, codigo)
                break
            else:
                print("Movimentação não encontrada.")
                input("Tecle <ENTER> para continuar...")
                os.system('clear')

        except ValueError:
            print("Código inválido! Por favor, digite um número inteiro.")
    print()
    input("Tecle <ENTER> para continuar...")


def alterarmoovimentacao():
    relatoriomovimentacao()
    while True:
        try:
            codigo = int(
                input("Qual é o código da movimentação que deseja alterar? "))
            if codigo in movimentacao:
                exibirmv(movimentacao, codigo)
                break
            else:
                print("Movimentação não encontrada.")
                input("Tecle <ENTER> para continuar...")
                os.system('clear')

        except ValueError:
            print("Código inválido! Por favor, digite um número inteiro.")
    print()

    while True:
        try:
            qta_retirar = int(
                input("Informe a nova quantidade que deseja retirar: "))
            if qta_retirar >= 0:
                break
            else:
                print(
                    "Quantidade inválida. Por favor, insira um número inteiro válido."
                )
        except ValueError:
            print("Por favor, insira um número inteiro válido.")

    movimentacao[codigo][1] = qta_retirar
    salvarDados(NomeDadosMovimentacao, movimentacao)
    print("Movimentação alterada com sucesso!")
    input("Tecle <ENTER> para continuar...")


def excluirmovimentacao():
    relatoriomovimentacao()
    while True:
        try:
            codigo = int(
                input("Qual é o código da movimentação que deseja excluir? "))
            if codigo in movimentacao:
                exibirmv(movimentacao, codigo)
                break
            else:
                print("Movimentação não encontrada.")
                input("Tecle <ENTER> para continuar...")
                os.system('clear')

        except ValueError:
            print("Código inválido! Por favor, digite um número inteiro.")
    print()
    while True:
        confirmacao = input("Deseja excluir esta movimentação? (S/N): ")
        if confirmacao.upper() == "S":
            del movimentacao[codigo]
            salvarDados(NomeDadosMovimentacao, movimentacao)
            print("Movimentação excluída com sucesso!")
            input("Tecle <ENTER> para continuar...")
            break
        elif confirmacao.upper() == "N":
            print("Exclusão cancelada.")
            input("Tecle <ENTER> para continuar...")
            break
        else:
            print(
                "Opção inválida. Por favor, digite 'S' para sim ou 'N' para não."
            )


def relatoriomovimentacao():
    os.system('clear')
    linha_sep = "##################################################################################"
    cabecalho = "###########################        Relatório de Movimentação       #############################"
    linha_tabela_sep = "|--------------|---------------------|--------------|--------------|------------------|------------------|"
    cabecalho_tabela = "|     ID       |     Código Produto  |  Quantidade  |    Data      |    Funcionário   | Quantidade Devolvida|"

    print()
    print(linha_sep)
    print(cabecalho)
    print(linha_sep)
    print(linha_tabela_sep)
    print(cabecalho_tabela)
    print(linha_tabela_sep)

    if not movimentacao:
        print("| %-12s | %-19s | %-12s | %-12s | %-16s | %-16s |" %
              ("N/A", "N/A", "N/A", "N/A", "N/A", "N/A"))
        print(linha_tabela_sep)
    else:
        for codmov, mov in movimentacao.items():
            cod_prod = mov[0]
            quantidade = mov[1]
            data = mov[2]
            funcionario = mov[3] if len(mov) > 3 else "N/A"
            quantidade_devolvida = mov[4] if len(mov) > 4 else "N/A"
            print("| %-12s | %-19s | -%-12s | %-12s | %-16s | %-16s |" %
                  (codmov, cod_prod, quantidade, data, funcionario,
                   quantidade_devolvida))
            print(linha_tabela_sep)

    print()
    input("Tecle <ENTER> para continuar...")
