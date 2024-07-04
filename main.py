#Sistema de Gestão de Estoque
#Cadastro, Listagem, Alteração, Exclusão e "Busca"
#Controle de Entrada e Saída de Produto

#trocar modulo listar pra buscar por produto
#Modulo buscar colocar relatorio

import os
import pickle

estoque = []
produtos = {
    '123': ["Agua", 5, 10],
    '456': ["Celular", 1000, 1],
    '789': ["Cerveja", 4, 12],
}
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
  codigo = input("Digite o Codigo do produto: ")
  nome = input("Digite o nome do produto: ")
  preco = float(input("Digite o preço do produto: "))
  quantidade = int(input("Digite a quantidade do produto: "))
  produtos[codigo] = [nome, preco, quantidade]
  estoque.append(produtos)
  print("Produto cadastrado com sucesso!")
  input("Pressione ENTER para continuar")


def BuscarProduto():
  print()
  print("############################################")
  print("#####   Você está no Módulo Buscar    ####")
  print("############################################")
  print()
  print("Buscar Produtos")
  print("--------------------")
  codtest = input("Qual é o Codigo do Produto?")
  #Qual é o melhor, listar todos os produtos ou somente 1?
  #melhor relatorio
  if codtest in produtos:
    print("##### Codigo:", codtest)
    print("##### Nome: ", produtos[codtest][0])
    print("##### Preço: ", produtos[codtest][1])
    print("##### Quantidade: ", produtos[codtest][2])
  else:
    print("Produto inexistente!")
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
  codtest = input("Qual é o Codigo do Produto?")
  if codtest in produtos:
    print("Informe os novos dados do Produto: ")
    nome = input("##### Nome: ")
    print()
    preco = input("##### Preço: ")
    print()
    Quantidade = input("##### Quantidade: ")
    print()
    produtos[codtest] = [nome, preco, Quantidade]
    print("Produto Alterado com Sucesso!!")

  else:
    print("Produto inexistente!")
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
  codtest = input("Qual é o Codigo do Produto?")
  if codtest in produtos:
    del produtos[codtest]
    print("Produto Excluído com Sucesso!!")
  else:
    print("Produto inexistente!")
    print()
  input("Tecle <ENTER> para continuar...")


def relatorioProduto():
  print()
  print("############################################")
  print("#####   Você está no Módulo Relatorio   ####")
  print("############################################")
  print()
  print("Relatorio de Produtos")
  print("--------------------")
  print()


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
  print("#####      1 - Módulo Usuario          #####")
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
      resp_estoque = telaUsuario()
      print("Módulo Usuario")
      #Modulo Usuario
      match resp_estoque:
        case '1':
          os.system('clear')
          #telaSaidaProduto()
          #Esse modulo é pra movimentação do estoque
          #Simular um saida de produto
          #saidaProduto()
        case '2':
          os.system('clear')
          #telaEntradaProduto()
          #Esse modulo é pra movimentação do estoque
          #Simular um entrada de produto
          #entradaProduto()
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
          #os.system('clear')
          print()

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
