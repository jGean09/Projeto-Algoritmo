#SISTEMA DE GESTÃO DE ESTOQUE DE UM ALMOXARIFADO
#TODA VEZ QUE UM PRODUTO/FERRAMENTA/EQUIPAMENTO FOR RETIRADO DO ALMOXARIFADO, O PRODUTO/FERRAMENTA/EQUIPAMENTO DEVE TER UM FUNCIONÁRIO QUE SERÁ RESPONSÁVEL. ONDE FICARÁ RESPONSÁVEL PRA DEVOLVER O PRODUTO/FERRAMENTA/EQUIPAMENTO AO ALMOXARIFADO.

# GESTÃO DO ALMOXARIFADO DO CERES
#

import os
import pickle
import funcionario

produtos = {}
try:
  arq_produtos = open("Produtos.dat", "rb")
  produtos = pickle.load(arq_produtos)
except:
  arq_produtos = open("Produtos.dat", "wb")
  arq_produtos.close()

fornecedores = {}
try:
  arq_fornecedores = open("Fornecedores.dat", "rb")
  fornecedores = pickle.load(arq_fornecedores)
except:
  arq_fornecedores = open("Fornecedores.dat", "wb")
  arq_fornecedores.close()

  #############################################################################################
  #################     PRODUTO      #########################


def cadastrarProduto():
  print("############################################")
  print("#####   Você está no Módulo Cadastro    ####")
  print("############################################")
  print()
  print("Cadastro de Produtos")
  print("--------------------")

  while True:
    try:
      codigo = int(input("Digite o Código do produto: ").strip())
      if codigo in produtos:
        print(
            "Produto com esse código já existe! Por favor, digite um novo código."
        )
      else:
        break
    except ValueError:
      print("Código inválido! Por favor, digite um número inteiro.")

  while True:
    nome = input("Digite o nome do produto: ").strip()
    if not nome:
      print(
          "Nome do produto não pode ser vazio! Por favor, digite um nome válido."
      )
    else:
      break

  while True:
    try:
      preco = float(input("Digite o preço do produto: ").strip())
      if preco <= 0:
        print(
            "O preço deve ser um valor positivo! Por favor, digite um preço válido."
        )
      else:
        break
    except ValueError:
      print("Preço inválido! Por favor, digite um número válido.")

  while True:
    try:
      quantidade = int(input("Digite a quantidade do produto: ").strip())
      if quantidade < 0:
        print(
            "A quantidade não pode ser negativa! Por favor, digite um valor válido."
        )
      else:
        break
    except ValueError:
      print("Quantidade inválida! Por favor, digite um número inteiro.")

  produtos[codigo] = [nome, preco, quantidade]

  print("Produto cadastrado com sucesso!")
  print()
  print("##### Código:", codigo)
  print("##### Nome: ", produtos[codigo][0])
  print("##### Preço: R$", produtos[codigo][1])
  print("##### Quantidade: ", produtos[codigo][2])

  input("Pressione ENTER para continuar")


def BuscarProduto():
  print()
  print("############################################")
  print("#####   Você está no Módulo Buscar    ####")
  print("############################################")
  print()
  print("Buscar Produtos")
  print("--------------------")

  while True:
    try:
      codtest = int(input("Qual é o Código do Produto? "))
      if codtest in produtos:
        print("Produto encontrado:")
        print("##### Código:", codtest)
        print("##### Nome: ", produtos[codtest][0])
        print("##### Preço: R$", produtos[codtest][1])
        print("##### Quantidade: ", produtos[codtest][2])
        break
      else:
        print("Produto inexistente!")
        input("Tecle <ENTER> para continuar...")
        os.system('clear')
    except ValueError:
      print("Código inválido! Por favor, digite um número inteiro.")

  print()
  input("Tecle <ENTER> para continuar...")


def alterarProdutos():
  print()
  print("############################################")
  print("#####   Você está no Módulo Alteração   ####")
  print("############################################")
  print()
  print("Alterar Produtos")
  print("--------------------")

  while True:
    try:
      codtest = int(input("Qual é o Código do Produto? "))
      if codtest in produtos:
        print("Produto encontrado:")
        print("##### Código:", codtest)
        print("##### Nome: ", produtos[codtest][0])
        print("##### Preço: R$", produtos[codtest][1])
        print("##### Quantidade: ", produtos[codtest][2])

        confirmacao = input("Deseja alterar este produto? (s/n): ").lower()
        if confirmacao == 's':
          nome = input("Informe o novo nome: ")
          preco = float(input("Informe o novo preço: "))
          quantidade = int(input("Informe a nova quantidade: "))

          produtos[codtest] = [nome, preco, quantidade]
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


def excluirProdutos():
  print()
  print("############################################")
  print("#####   Você está no Módulo Exclusão   ####")
  print("############################################")
  print()
  print("Excluir Produtos")
  print("--------------------")

  while True:
    try:
      codtest = int(input("Qual é o Código do Produto? "))
      break
    except ValueError:
      print("Código inválido! Por favor, digite um número inteiro.")

  if codtest in produtos:
    nome, preco, quantidade = produtos[codtest]
    print("Produto encontrado:")
    print("##### Código:", codtest)
    print("##### Nome: ", nome)
    print("##### Preço: R$", preco)
    print("##### Quantidade: ", quantidade)

    confirm = input(
        "Tem certeza que deseja remover este produto? (s/n): ").lower()

    if confirm == 's':
      del produtos[codtest]
      print("Produto Excluído com Sucesso!!")
    else:
      print("Exclusão de produto cancelada.")
  else:
    print("Produto inexistente!")

  print()
  input("Tecle <ENTER> para continuar...")


def relatorioGeralProdutos():

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
  for codigo in sorted(produtos.keys(), key=int):
    # Ordenando os códigos numericamente
    nome, preco, quantidade = produtos[codigo]
    print("| %-9s " % (codigo), end='')
    print("| %-27s " % (nome), end='')
    print("| R$ %-15.2f " % (preco), end='')
    print("| %-15d |" % (quantidade))
    print(linha_tabela_sep)
  print()
  input("Tecle <ENTER> para continuar...")


#
def informacoes():
  print("############################################")
  print("#####  Você está no Módulo Informações  ####")
  print("############################################")
  print()
  print("##### Projeto de Gestão de Estoque      ####")
  print("##### Equipe de desenvolvimento:        ####")
  print("##### José Gean De Macêdo Alves         ####")
  print()
  input("Tecle <ENTER> para continuar...")


def telaGestao():
  os.system('clear')
  print("############################################")
  print("######       Projeto GESTAO-Estoque   ######")
  print("############################################")
  print("#####      1 - Módulo Funcionário      #####")
  print("#####      2 - Módulo Produto/estoque  #####")
  print("#####      3 - Módulo Fornecedores     #####")
  print("#####      4 - Módulo Movimentação     #####")
  print("#####      5 - Módulo Relatório        #####")
  print("#####      6 - Módulo Informações      #####")
  print("#####      0 - Sair                    #####")
  resp_inicial = input("##### Escolha sua opção: ")
  return resp_inicial


def telaUsuario():
  os.system('clear')
  print("############################################")
  print("#####   Módulo Movimentação Estoque   ######")
  print("############################################")
  print("##### 1 - Retirar Produto do Estoque   #####")
  print("##### 2 - Adicionar Produto do Estoque #####")
  print("############################################")
  resp_estoque = input("##### Escolha sua opção: ")
  return resp_estoque


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


####################FORNECEEDORES####################


def telafornecedor():
  os.system('clear')
  print("############################################")
  print("#####   Módulo Fornecedores   ######")
  print("############################################")
  print("##### 1 - Cadastrar Fornecedor      #####")
  print("##### 2 - Buscar Fornecedor         #####")
  print("##### 3 - Alterar Fornecedor        #####")
  print("##### 4 - Excluir Fornecedor        #####")
  print("##### 5 - Relatorio Fornecedor      #####")
  resp_fornecedor = input("##### Escolha sua opção: ")
  return resp_fornecedor


def cadastrarFornecedor():
  os.system('clear')
  print("############################################")
  print("#####   Você está no Módulo Cadastro    ####")
  print("############################################")
  print()
  print("Cadastro de Fornecedores")
  print("--------------------")

  while True:
    try:
      codigo = int(input("Digite o Código do fornecedor: ").strip())
      if codigo in fornecedores:
        print(
            "Fornecedor com esse código já existe! Por favor, digite um novo código."
        )
      else:
        break
    except ValueError:
      print("Código inválido! Por favor, digite um número inteiro.")

  while True:
    nome = input("Digite o nome do fornecedor: ").strip()
    if not nome:
      print(
          "Nome do fornecedor não pode ser vazio! Por favor, digite um nome válido."
      )
    else:
      break

  fornecedores[codigo] = [nome]

  print("Fornecedor cadastrado com sucesso!")
  print()
  print("##### Código:", codigo)
  print("##### Nome: ", fornecedores[codigo][0])

  input("Pressione ENTER para continuar")


def buscarFornecedor():
  os.system('clear')
  print()
  print("############################################")
  print("#####   Você está no Módulo Buscar      ####")
  print("############################################")
  print()
  print("Buscar Fornecedores")
  print("--------------------")
  while True:
    try:
      codtest = int(input("Qual é o Código do Fornecedor? "))
      if codtest in fornecedores:
        print("Fornecedor encontrado:")
        print("##### Código:", codtest)
        print("##### Nome: ", fornecedores[codtest][0])
        break
      else:
        print("Fornecedor inexistente!")
        input("Tecle <ENTER> para continuar...")
        os.system('clear')
    except ValueError:
      print("Código inválido! Por favor, digite um número inteiro.")
  print()
  input("Tecle <ENTER> para continuar...")


def alterarfornecedor():
  os.system('clear')
  print()
  print("############################################")
  print("#####   Você está no Módulo Alteração   ####")
  print("############################################")
  print()
  print("Alterar Fornecedores")
  print("--------------------")
  while True:
    try:
      codtest = int(input("Qual é o Código do Fornecedor? "))
      if codtest in fornecedores:
        print("Fornecedor encontrado:")
        print("##### Código:", codtest)
        print("##### Nome: ", fornecedores[codtest][0])
        confirmacao = input("Deseja alterar este fornecedor? (s/n): ").lower()
        if confirmacao == 's':
          nome = input("Informe o novo nome: ")
          fornecedores[codtest] = [nome]
          print("Fornecedor alterado com sucesso!")
        else:
          print("Alteração cancelada.")
        break
      else:
        print("Fornecedor inexistente!")
    except ValueError:
      print("Código inválido! Por favor, digite um número inteiro.")
  print()
  input("Tecle <ENTER> para continuar...")


def excluirfornecedor():
  print()
  print("############################################")
  print("#####   Você está no Módulo Exclusão   ####")
  print("############################################")
  print()
  print("Excluir Fornecedores")
  print("--------------------")
  while True:
    try:
      codtest = int(input("Qual é o Código do Fornecedor? "))
      if codtest in fornecedores:
        nome, fornecedores[codtest] = fornecedores[codtest]
        print("Fornecedor encontrado:")
        print("##### Código:", codtest)
        print("##### Nome: ", nome)
        confirm = input(
            "Tem certeza que deseja remover este fornecedor? (s/n): ").lower()
        if confirm == 's':
          del fornecedores[codtest]
          print("Fornecedor Excluído com Sucesso!!")
        else:
          print("Exclusão de fornecedor cancelada.")
        break
      else:
        print("Fornecedor inexistente!")
    except ValueError:
      print("Código inválido! Por favor, digite um número inteiro.")
  print()
  input("Tecle <ENTER> para continuar...")


def relatoriofornecedores():
  linha_sep = "#######################################################################"
  cabecalho = "##############      Relatório Geral de Fornecedores       #############"
  linha_tabela_sep = "____|-----------|-----------------------------|____"
  cabecalho_tabela = "____|  Código   |        Nome do Fornecedor   |____"

  print(linha_sep)
  print(cabecalho)
  print(linha_sep)
  print(linha_tabela_sep)
  print(cabecalho_tabela)
  print(linha_tabela_sep)

  for codigo in sorted(fornecedores.keys(), key=int):
    nome = fornecedores[codigo]
    print("____| %-9s | %-27s |____" % (codigo, nome))
    print(linha_tabela_sep)
  print()
  input("Tacle <ENTER> para continuar...")


####################################################
# MODULO RELATORIO


def telarelatorios():
  os.system('clear')
  print("############################################")
  print("#####       Módulo Relatório          ######")
  print("############################################")
  print("### 1 - Relatório Geral de Funcionários  ###")
  print("### 2 - Relatório Geral de Produtos      ###")
  print("### 3 - Relatório Geral de Fornecedores  ###")
  print("### 4 - Relatório Geral de Movimentação  ###")
  print("### 0 - Sair                             ###")
  resp_relatorio = input("### Escolha sua opção: ")
  return resp_relatorio


### MOVIMETÇÃO ###
def telamovimentacao():
  os.system('clear')
  print("############################################")
  print("#####   Módulo Movimentação Estoque   ######")
  print("############################################")
  print("##### 1 - Retirar Produto do Estoque   #####")
  print("##### 2 - Adicionar Produto do Estoque #####")
  print("##### 0- Sair                          #####")
  print("############################################")
  resp_movimentacao = input("##### Escolha sua opção: ")
  return resp_movimentacao


def retirarprodutoestoque():
  os.system('clear')
  print("############################################")
  print("#####   Você está no Módulo Retirar     ####")
  print("############################################")
  print()
  print("Retirar Produto do Estoque")
  print("--------------------")
  while True:
    try:
      codtest = int(input("Qual é o Código do Produto? "))
      if codtest in produtos:
        print("Produto encontrado:")
        print("##### Código:", codtest)
        print("##### Nome: ", produtos[codtest][0])
        print("##### Preço: ", produtos[codtest][1])
        print("##### Quantidade: ", produtos[codtest][2])

        confirmacao = input("Deseja retirar este produto? (s/n): ").lower()
        if confirmacao == 's':
          quantidade = int(input("Informe a quantidade a ser retirada: "))
          if quantidade <= produtos[codtest][2]:
            produtos[codtest][2] -= quantidade
            print("Produto retirado com sucesso!")
            input("Tecle <ENTER> para continuar...")
          else:
            print("Quantidade insuficiente em estoque.")
            input("Tecle <ENTER> para continuar...")
        else:
          print("Retirada cancelada.")
          input("Tecle <ENTER> para continuar...")
        break
      else:
        print("Produto inexistente!")
        input("Tecle <ENTER> para continuar...")
    except ValueError:
      print("Código inválido! Por favor, digite um número inteiro.")


def adicionarprodutoestoque():
  os.system('clear')
  print("############################################")
  print("#####   Você está no Módulo Adicionar   ####")
  print("############################################")
  print()
  print("Adicionar Produto do Estoque")
  print("--------------------")
  while True:
    try:
      codtest = int(input("Qual é o Código do Produto? "))
      if codtest in produtos:
        print("Produto encontrado:")
        print("##### Código:", codtest)
        print("##### Nome: ", produtos[codtest][0])
        confirmacao = input("Deseja adicionar este produto? (s/n): ").lower()
        if confirmacao == 's':
          quantidade = int(input("Informe a quantidade a ser adicionada: "))
          produtos[codtest][2] += quantidade
          print("Produto adicionado com sucesso!")
        else:
          print("Adicionação cancelada.")
        break
      else:
        print("Produto inexistente!")
    except ValueError:
      print("Código inválido! Por favor, digite um número inteiro.")


end = ''
while end != '0':
  resp_Geral = telaGestao()

  #Gestão de Estoque
  match resp_Geral:
    case '1':
      resp_funcionario = funcionario.telaFuncionario()
      #Modulo Usuario
      match resp_funcionario:
        case '1':
          os.system('clear')
          funcionario.cadastrarFuncionario()
        case '2':
          os.system('clear')
          funcionario.BuscarFuncionario()
        case '3':
          os.system('clear')
          funcionario.alterarFuncionario()
        case '4':
          os.system('clear')
          funcionario.excluirFuncionario()
        case '5':
          os.system('clear')
          funcionario.relatorioFuncionarios()
        case '0':
          os.system('clear')
          print("Saindo do módulo de Funcionário...")
          input("Tecle <ENTER> para continuar...")

        case _:
          #Qualquer Número invalido
          os.system('clear')
          print("Opção inválida")
          input("Tecle <ENTER> para continuar...")
    case '2':
      #Modulo Produto
      os.system('clear')

      #telaProduto()
      resp_produto = telaProduto()
      match resp_produto:
        case '1':
          os.system('clear')
          cadastrarProduto()

        case '2':
          os.system('clear')
          BuscarProduto()
        case '3':
          os.system('clear')
          alterarProdutos()

        case '4':
          os.system('clear')
          excluirProdutos()
        case '5':
          os.system('clear')
          print()
          relatorioGeralProdutos()

        case '0':
          os.system('clear')
          print()
          print("Saindo do Módulo Produto...")
          input("Tecle <ENTER> para continuar...")
        case _:
          #Qualquer Número invalido
          os.system('clear')
          print("Opção inválida")
          input("Tecle <ENTER> para continuar...")
    case '3':
      #modulo Fornecedores
      os.system('clear')
      resp_fornecedor = telafornecedor()
      match resp_fornecedor:
        case '1':
          cadastrarFornecedor()
        case '2':
          buscarFornecedor()
        case '3':
          alterarfornecedor()
        case '4':
          excluirfornecedor()
        case '5':
          relatoriofornecedores()
        case '0':
          print("Saindo do Módulo Fornecedores...")
          input("Tecle <ENTER> para continuar...")
        case _:
          print("Resposta inválida")
          input("Tecle <ENTER> para continuar...")
      os.system('clear')
    case '4':
      resp_movimentacao = telamovimentacao()
      match resp_movimentacao:
        case '1':
          retirarprodutoestoque()
        case '2':
          adicionarprodutoestoque()
        case '0':
          print("Saindo do Módulo Movimentação...")
          input("Tecle <ENTER> para continuar...")
        case _:
          print("Resposta inválida")
          input("Tecle <ENTER> para continuar...")

      os.system('clear')
    case '5':
      resp_relatorios = telarelatorios()
      match resp_relatorios:
        case '1':
          print("Relatório de Funcionários")
          funcionario.relatorioFuncionarios()
        case '2':
          print("Relatório de Produtos")
          relatorioGeralProdutos()
        case '3':
          print("Relatório de Fornecedores")
          relatoriofornecedores()
        case '4':
          print("Relatório de Movimentação")
          #relatorioMovimentacao()
        case '0':
          print("Saindo do módulo de Relatórios...")
          input("Tecle <ENTER> para continuar...")
        case _:
          print("Resposta inválida")
          input("Tecle <ENTER> para continuar...")
    case '6':
      informacoes()
    case '0':
      #sair do programa geral
      end = '0'

      os.system('clear')
    case _:
      #Qualquer Número invalido
      os.system('clear')
      print("Opção inválida")
      input("Tecle <ENTER> para continuar...")

arq_produtos = open("Produtos.dat", "wb")
pickle.dump(produtos, arq_produtos)
arq_produtos.close()

arq_fornecedores = open("Fornecedores.dat", "wb")
pickle.dump(fornecedores, arq_fornecedores)
arq_fornecedores.close()
