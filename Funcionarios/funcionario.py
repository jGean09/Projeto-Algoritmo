import os
from biblioteca.ValidarCPF import validaCPF
from biblioteca.ValidarNome import ler_nome
from biblioteca.ValidarEmail import ler_email
from biblioteca.dados import carregarDados, salvarDados
from telas.telasFuncionarios import telacadastroFuncionario, telabuscarFuncionario, telaalterarFuncionario, telaexcluirFuncionario

funcionarios = carregarDados("Funcionarios.dat")


def exibirFuncionario(funcionarios, CPF):
  print("Funcionário cadastrado com sucesso!")
  print()
  print("##### CPF:", CPF)
  print("##### Nome: ", funcionarios[CPF][0])
  print("##### EMAIL: ", funcionarios[CPF][1])
  input("Pressione ENTER para continuar")


def cadastrarFuncionario():
  telacadastroFuncionario()
  while True:
    CPF = input("Digite o CPF do Funcionário: ").strip()
    if validaCPF(CPF) == True:
      break
    else:
      print("CPF inválido. Digite novamente.")
      continue

  nome = ler_nome()
  email = ler_email()
  funcionarios[CPF] = [nome, email]
  exibirFuncionario(funcionarios, CPF)
  salvarDados("Funcionarios.dat", funcionarios)


def buscarFuncionarioPorCPF(CPF):
  funcionarios = carregarDados("Funcionarios.dat")

  while True:
    if CPF in funcionarios:
      return funcionarios
    else:
      print("Funcionario não encontrado.")
      resposta = input("Deseja tentar buscar novamente? (s/n): ").lower()
      if resposta != 's':
        return None
      CPF = int(input("Digite o CPF do Funcionario: "))


def BuscarFuncionario():
  funcionarios = carregarDados("Funcionarios.dat")
  telabuscarFuncionario()
  while True:
    relatorioFuncionarios()
    CPF = input("Qual é o CPF do Funcionário? ")
    if CPF in funcionarios:
      exibirFuncionario(funcionarios, CPF)
      break
    else:
      print("CPF inexistente!")
      opcao = input("Deseja tentar novamente? (s/n): ").lower()
      if opcao != 's':
        break

  input("Tecle <ENTER> para continuar...")


def alterarFuncionario():
  telaalterarFuncionario()
  relatorioFuncionarios()
  CPF = input("Qual é o CPF do Funcionário que deseja alterar? ")
  if CPF in funcionarios:
    exibirFuncionario(funcionarios, CPF)
    print("Digite o novo nome:")
    nome = ler_nome()
    print("Digite o novo Email:")
    email = ler_email()
    funcionarios[CPF] = [nome, email]
    print("Funcionário alterado com sucesso!")
    salvarDados("Funcionarios.dat", funcionarios)
  else:
    print("Funcionário não encontrado.")

  input("Tecle <ENTER> para continuar...")


def excluirFuncionario():
  telaexcluirFuncionario()
  relatorioFuncionarios()
  CPF = input("Qual é o CPF do Funcionário que deseja excluir? ")
  if CPF in funcionarios:
    exibirFuncionario(funcionarios, CPF)
    confirmacao = input(
        "Tem certeza que deseja excluir este funcionário? (s/n): ").lower()
    if confirmacao == 's':
      del funcionarios[CPF]
      print("Funcionário excluído com sucesso!")
      salvarDados("Funcionarios.dat", funcionarios)
    else:
      print("Exclusão cancelada.")
  else:
    print("Funcionário não encontrado.")
  input("Tecle <ENTER> para continuar...")


def relatorioFuncionarios():
  funcionarios = carregarDados("Funcionarios.dat")
  linha_sep = "##################################################################################"
  cabecalho = "#######################        Relatório Geral de Funcionários       #######################"
  linha_tabela_sep = "|--------------|--------------------------------------|----------------------------------------|"
  cabecalho_tabela = "|     CPF      |           Nome do Funcionário        |              Email                     |"

  print()
  print(linha_sep)
  print(cabecalho)
  print(linha_sep)
  print(linha_tabela_sep)
  print(cabecalho_tabela)
  print(linha_tabela_sep)

  if not funcionarios:
    print("| %-14s | %-36s | %-38s |" % ("N/A", "N/A", "N/A"))
    print(linha_tabela_sep)
  else:
    for cpf, dados in funcionarios.items():
      nome = dados[0]
      email = dados[1]
      print("| %-12s | %-36s | %-38s |" % (cpf, nome, email))
      print(linha_tabela_sep)

  print()
  input("Tecle <ENTER> para continuar...")


def telaFuncionario():
  os.system('clear')
  print("############################################")
  print("#####   Módulo Produto Estoque   ######")
  print("############################################")
  print("##### 1 - Cadastrar Funcionário          #####")
  print("##### 2 - Buscar Funcionário             #####")
  print("##### 3 - Alterar Funcionário            #####")
  print("##### 4 - Excluir Funcionário            #####")
  print("##### 5 - Relatorio Funcionário          #####")
  print("##### 0 - Sair                           #####")
  print("############################################")
  resp_funcionario = input("##### Escolha sua opção: ")
  return resp_funcionario
