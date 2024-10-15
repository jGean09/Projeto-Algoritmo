'''
Sistema de Gestão de Estoque
Baseado no sistema de gestão de estoque de um almoxarifado

Consiste em um sistema de gestão de estoque, onde o usuário pode cadastrar, buscar, alterar e excluir produtos e funcionarios. Pra fazer movimentação no estoque o usuario utilizar um modulo chamado de movimentação, pois não é uma venda e sim um retirada do estoque. Após isso, o sistema tem que gerar relatorio do estoque para saber  o que o funcionario retirou (quais produtos e a quantidade de produtos).
'''
import os
from biblioteca.geradorId import gerarNovoID

from Estoque.produtos import telaProduto, cadastrarProduto, buscarProduto, alterarProduto, excluirProduto, relatorioGeralProdutos

from Funcionarios.funcionario import telaFuncionario, cadastrarFuncionario, BuscarFuncionario, alterarFuncionario, excluirFuncionario, relatorioFuncionarios

from movimentacao.movimentacao import buscarmovimentacao, cadastrarmovimentacaoRetirada, relatoriomovimentacao, telaMovimentacao, cadastrarmovimentacaoAdicionar, relatoriomovimentacao, alterarmoovimentacao, excluirmovimentacao

from telas.telasInicio import telaGestao, informacoes, telarelatorios

resp_Geral = ''
while resp_Geral != '0':
  resp_Geral = telaGestao()
  match resp_Geral:
    case '1':
      resp_funcionario = telaFuncionario()
      match resp_funcionario:
        case '1':
          os.system('clear')
          cadastrarFuncionario()
        case '2':
          os.system('clear')
          BuscarFuncionario()
        case '3':
          os.system('clear')
          alterarFuncionario()
        case '4':
          os.system('clear')
          excluirFuncionario()
        case '5':
          os.system('clear')
          relatorioFuncionarios()
        case '0':
          os.system('clear')
          print("Saindo do módulo de Funcionário...")
          input("Tecle <ENTER> para continuar...")
        case _:
          os.system('clear')
          print("Opção inválida")
          input("Tecle <ENTER> para continuar...")
    case '2':
      os.system('clear')
      resp_produto = telaProduto()
      match resp_produto:
        case '1':
          os.system('clear')
          cadastrarProduto()
        case '2':
          os.system('clear')
          buscarProduto()
        case '3':
          os.system('clear')
          alterarProduto()
        case '4':
          os.system('clear')
          excluirProduto()
        case '5':
          os.system('clear')
          relatorioGeralProdutos()
        case '0':
          os.system('clear')
          print("Saindo do Módulo Produto...")
          input("Tecle <ENTER> para continuar...")
        case _:
          os.system('clear')
          print("Opção inválida")
          input("Tecle <ENTER> para continuar...")
    case '3':
      resp_movimentacao = telaMovimentacao()
      match resp_movimentacao:
        case '1':
          cadastrarmovimentacaoRetirada()
        case '2':
          cadastrarmivmentacaoDevolver()
        case '3':
          buscarmovimentacao()
        case '4':
          alterarmoovimentacao()
        case '5':
          excluirmovimentacao()
        case '6':
          relatoriomovimentacao()
        case '0':
          print("Saindo do Módulo Movimentação...")
          input("Tecle <ENTER> para continuar...")
        case _:
          print("Resposta inválida")
          input("Tecle <ENTER> para continuar...")

      os.system('clear')
    case '4':
      resp_relatorios = telarelatorios()
      match resp_relatorios:
        case '1':
          relatorioFuncionarios()
        case '2':
          relatorioGeralProdutos()
        case '3':
          relatoriomovimentacao()
        case '0':
          print("Saindo do módulo de Relatórios...")
          input("Tecle <ENTER> para continuar...")
        case _:
          print("Resposta inválida")
          input("Tecle <ENTER> para continuar...")
    case '5':
      informacoes()
    case '0':
      os.system('clear')
    case _:
      os.system('clear')
      print("Opção inválida")
      input("Tecle <ENTER> para continuar...")
