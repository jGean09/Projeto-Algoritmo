import os


def telaCadastroMovimentacao():
  os.system('clear')
  print()
  print("############################################")
  print("#####   Você está no Módulo Adicionar   ####")
  print("############################################")
  print()
  print("Adicionar Movimentação")
  print("--------------------")
  print()


def telaMovimentacao():
  os.system('clear')
  print("######################################################")
  print("##########   Módulo Movimentação Estoque   ###########")
  print("######################################################")
  print("##### 1 - Cadastrar Retirar Produto do Estoque   #####")
  print("##### 2 - Cadastrar Devolução Produto ao Estoque  #####")
  print("##### 3 - Buscar Movimentação do Estoque         #####")
  print("##### 4 - Alterar Movimentação do Estoque        #####")
  print("##### 5 - Excluir Movimentação do Estoque        #####")
  print("##### 6 - Relatorio Movimentação do Estoque      #####")
  print("############################################")
  resp_estoque = input("##### Escolha sua opção: ")
  return resp_estoque
