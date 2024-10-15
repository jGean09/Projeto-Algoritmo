import os
from biblioteca.dados import carregarDados, salvarDados
from biblioteca.geradorId import gerarNovoID
from telas.telasProdutos import telacadasstraproduto, telabuscarproduto, telaexcluirproduto, telaalterarproduto

produtos = carregarDados("Produtos.dat")


def lernomeProduto():
    while True:
        nome = input("Digite o nome do produto: ").strip()
        if nome:
            break
        else:
            print(
                "Nome do produto não pode ser vazio! Por favor, digite um nome válido."
            )
    return nome


def lerprecoProduto():
    while True:
        preco = input("Digite o preço do produto: ").strip()
        try:
            preco = float(preco)
            if preco > 0:
                break
            else:
                print(
                    "O preço deve ser um valor positivo! Por favor, digite um preço válido."
                )
        except ValueError:
            print("Preço inválido! Por favor, digite um número válido.")
    return preco


def lerquantidadeProduto():
    while True:
        quantidade = input("Digite a quantidade do produto: ").strip()
        if quantidade.isdigit():
            quantidade = int(quantidade)
            if quantidade >= 0:
                break
            else:
                print(
                    "A quantidade não pode ser negativa! Por favor, digite um valor válido."
                )
        else:
            print("Quantidade inválida! Por favor, digite um número inteiro.")
    return quantidade


def exibirproduto(produtos, codigo):
    print("Produto cadastrado com sucesso!")
    print()
    print("##### Código:", codigo)
    print("##### Nome: ", produtos[codigo][0])
    print("##### Preço: R$", produtos[codigo][1])
    print("##### Quantidade: ", produtos[codigo][2])
    input("Pressione ENTER para continuar")


def retorna_nome_produto(produtos, codigo):
    if codigo in produtos:
        return produtos[codigo][0]
    else:
        return None


def retorna_quantidade_produto(produtos, codigo):
    if codigo in produtos:
        return produtos[codigo][2]
    else:
        return None


def cadastrarProduto():
    telacadasstraproduto()
    codigo = gerarNovoID("id_produto.dat")
    nome = lernomeProduto()
    preco = lerprecoProduto()
    quantidade = lerquantidadeProduto()
    produtos[codigo] = [nome, preco, quantidade]
    salvarDados("Produtos.dat", produtos)
    print("Produto cadastrado com sucesso!")
    exibirproduto(produtos, codigo)


def buscarProdutoPorCodigo(codigo):
    produtos = carregarDados("Produtos.dat")
    while True:
        if codigo in produtos:
            return {
                'codigo': codigo,
                'nome': produtos[codigo][0],
                'preco': produtos[codigo][1],
                'quantidade': produtos[codigo][2]
            }
        else:
            print("Produto não encontrado.")
            resposta = input("Deseja tentar buscar novamente? (s/n): ").lower()
            if resposta != 's':
                return None
            codigo = int(input("Digite o Código do Produto: "))


def buscarProduto():
    telabuscarproduto()
    while True:
        try:
            codtest = int(input("Qual é o Código do Produto? "))
            if codtest in produtos:
                exibirproduto(produtos, codtest)
                break
            else:
                print("Produto inexistente!")
                input("Tecle <ENTER> para continuar...")
                os.system('clear')
        except ValueError:
            print("Código inválido! Por favor, digite um número inteiro.")
    print()
    input("Tecle <ENTER> para continuar...")


def alterarQuantidadeProduto(codigo, nova_quantidade):
    if codigo in produtos:
        produtos[codigo][2] = nova_quantidade
        salvarDados("Produtos.dat", produtos)
        print(
            f"Quantidade do produto {codigo} alterada para {nova_quantidade}.")

    else:
        print(f"Produto com código {codigo} não encontrado.")


def alterarProduto():
    telaalterarproduto()
    while True:
        try:
            codtest = int(input("Qual é o Código do Produto? "))
            if codtest in produtos:
                exibirproduto(produtos, codtest)
                confirmacao = input(
                    "Deseja alterar este produto? (s/n): ").lower()
                if confirmacao == 's':
                    nome = input("Informe o novo nome: ")
                    preco = float(input("Informe o novo preço: "))
                    quantidade = int(input("Informe a nova quantidade: "))
                    produtos[codtest] = [nome, preco, quantidade]
                    salvarDados("Produtos.dat", produtos)
                    print("Produto alterado com sucesso!")
                else:
                    print("Alteração cancelada.")
                break
            else:
                print("Produto inexistente!")
        except ValueError:
            print("Código inválido! Por favor, digite um número inteiro.")
    print()
    input("Tecle <ENTER> para continuar...")


def excluirProduto():
    telaexcluirproduto()
    while True:
        try:
            codtest = int(input("Qual é o Código do Produto? "))
            break
        except ValueError:
            print("Código inválido! Por favor, digite um número inteiro.")

    if codtest in produtos:
        nome, preco, quantidade = produtos[codtest]
        print("Produto encontrado:")
        exibirproduto(produtos, codtest)
        confirm = input(
            "Tem certeza que deseja remover este produto? (s/n): ").lower()
        if confirm == 's':
            del produtos[codtest]
            salvarDados("Produtos.dat", produtos)
            print("Produto Excluído com Sucesso!!")
        else:
            print("Exclusão de produto cancelada.")
    else:
        print("Produto inexistente!")
    print()
    input("Tecle <ENTER> para continuar...")


def relatorioGeralProdutos():
    os.system('clear')
    linha_sep = "##################################################################################"
    cabecalho = "#######################        Relatório Geral de Produtos       #######################"
    linha_tabela_sep = "|-----------|-----------------------------|--------------------|-----------------|"
    cabecalho_tabela = "|  Código   |        Nome do Produto      |       Preço        |   Quantidade    |"

    print(linha_sep)
    print(cabecalho)
    print(linha_sep)
    print(linha_tabela_sep)
    print(cabecalho_tabela)
    print(linha_tabela_sep)
    #Ordenar os códigos dos produtos em ordem crescente.
    for codigo in sorted(produtos.keys(), key=int):
        nome, preco, quantidade = produtos[codigo]
        print("| %-9s " % (codigo), end='')
        print("| %-27s " % (nome), end='')
        print("| R$ %-15.2f " % (preco), end='')
        print("| %-15d |" % (quantidade))
        print(linha_tabela_sep)
    print()
    input("Tecle <ENTER> para continuar...")


def telaProduto():
    os.system('clear')
    print("############################################")
    print("#####   Módulo Produto Estoque   ######")
    print("############################################")
    print("##### 1 - Cadastrar Produto          #####")
    print("##### 2 - Buscar Produto             #####")
    print("##### 3 - Alterar Produto            #####")
    print("##### 4 - Excluir Produto            #####")
    print("##### 5 - Relatorio Produto          #####")
    print("##### 0 - Sair                       #####")
    resp_produto = input("##### Escolha sua opção: ")
    return resp_produto
