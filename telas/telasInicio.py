####################Informações####################
import os


def telaGestao():
  os.system('clear')
  print("############################################")
  print("######       Projeto GESTAO-Estoque   ######")
  print("############################################")
  print("#####      1 - Módulo Funcionário      #####")
  print("#####      2 - Módulo Produto/estoque  #####")
  print("#####      3 - Módulo Movimentação     #####")
  print("#####      4 - Módulo Relatório        #####")
  print("#####      5 - Módulo Informações      #####")
  print("#####      0 - Sair                    #####")
  resp_inicial = input("##### Escolha sua opção: ")
  return resp_inicial


def informacoes():
  print("############################################")
  print("#####  Você está no Módulo Informações  ####")
  print("############################################")
  print()
  print("##### Projeto de Gestão de Estoque      ####")
  print("##### Equipe de desenvolvimento:        ####")
  print("##### José Gean De Macêdo Alves         ####")
  print("#####    EMAIL PARA CONTATO:            ####")
  print("#####   josegeantlc@gmail.com           ####")
  print()
  input("Tecle <ENTER> para continuar...")


def telarelatorios():
  os.system('clear')
  print("############################################")
  print("#####       Módulo Relatório          ######")
  print("############################################")
  print("### 1 - Relatório Geral de Funcionários  ###")
  print("### 2 - Relatório Geral de Produtos      ###")
  print("### 3 - Relatório Geral de Movimentação  ###")
  print("### 0 - Sair                             ###")
  resp_relatorio = input("### Escolha sua opção: ")
  return resp_relatorio
