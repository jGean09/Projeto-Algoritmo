#Sistema de Gestão de Estoque
#Cadastro, Listagem, Alteração, Exclusão e "Busca"
#Controle de Entrada e Saída de Produto

#trocar modulo listar pra buscar por produto
#Modulo buscar colocar relatorio

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
      codigo = int(input("Digite o Código do produto: "))
      if codigo in produtos:
        print(
            "Produto com esse código já existe! Por favor, digite um novo código."
        )
      else:
        break
    except ValueError:
      print("Código inválido! Por favor, digite um número inteiro.")

  nome = input("Digite o nome do produto: ")
  preco = float(input("Digite o preço do produto: "))
  quantidade = int(input("Digite a quantidade do produto: "))
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
  print("#####      3 - Módulo Relatório        #####")
  print("#####      4 - Módulo Informações      #####")
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
  resp_produto = input("##### Escolha sua opção: ")
  return resp_produto


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

        case 0:
          os.system('clear')
          print()
          print("############################################")
        case _:
          #Qualquer Número invalido
          os.system('clear')
          print("Opção inválida")
          input("Tecle <ENTER> para continuar...")
    case '3':
      #modulo informações
      os.system('clear')
      print()
      print("Relatorio")
      input("Tecle <ENTER> para continuar...")
      os.system('clear')
    case '4':
      informacoes()
      os.system('clear')
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
