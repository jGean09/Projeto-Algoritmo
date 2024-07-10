import os
import pickle

funcionarios = {}
try:
  arq_funcionarios = open("Funcionarios.dat", "rb")
  funcionarios = pickle.load(arq_funcionarios)
except:
  arq_funcionarios = open("Funcionarios.dat", "wb")
  arq_funcionarios.close()


def carregarFuncionarios():
  global funcionarios
  try:
    with open("Funcionarios.dat", "rb") as arq_funcionarios:
      funcionarios = pickle.load(arq_funcionarios)
  except FileNotFoundError:
    funcionarios = {
    }  # Se o arquivo não existe, inicializa como um dicionário vazio
  except Exception as e:
    print(f"Erro ao carregar funcionários: {e}")


def salvarFuncionarios():
  try:
    with open("Funcionarios.dat", "wb") as arq_funcionarios:
      pickle.dump(funcionarios, arq_funcionarios)
  except Exception as e:
    print(f"Erro ao salvar funcionários: {e}")


def cadastrarFuncionario():
  print("############################################")
  print("##### Você está no Cadastro Funcionário ####")
  print("############################################")
  print()
  print("Cadastro de Funcionário")
  print("--------------------")

  while True:
    CPF = input("Digite o CPF do Funcionário: ").strip()
    if not CPF:
      print("CPF não pode ser vazio! Por favor, digite um CPF válido.")
    elif CPF in funcionarios:
      print(
          "Funcionário com este CPF já existe! Por favor, digite um novo CPF.")
    else:
      break

  while True:
    nome = input("Digite o nome do Funcionário: ").strip()
    if not nome:
      print("Nome não pode ser vazio! Por favor, digite um nome válido.")
    else:
      break

  while True:
    email = input("Digite o Email do Funcionário: ").strip()
    if not email:
      print("Email não pode ser vazio! Por favor, digite um email válido.")
    else:
      break

  funcionarios[CPF] = [nome, email]

  print("Funcionário cadastrado com sucesso!")
  print()
  print("##### CPF:", CPF)
  print("##### Nome: ", funcionarios[CPF][0])
  print("##### EMAIL: ", funcionarios[CPF][1])

  salvarFuncionarios()
  input("Pressione ENTER para continuar")


def BuscarFuncionario():
  print()
  print("############################################")
  print("##### Você está no Buscar Funcionário #####")
  print("############################################")
  print()
  print("Buscar Funcionário")
  print("--------------------")

  while True:
    CPF = input("Qual é o CPF do Funcionário? ")
    if CPF in funcionarios:
      print("CPF encontrado:")
      print("##### CPF:", CPF)
      print("##### Nome: ", funcionarios[CPF][0])
      print("##### Email: ", funcionarios[CPF][1])
      break
    else:
      print("CPF inexistente!")
      opcao = input("Deseja tentar novamente? (s/n): ").lower()
      if opcao != 's':
        break

  input("Tecle <ENTER> para continuar...")


def alterarFuncionario():
  print()
  print("############################################")
  print("##### Você está no Alterar Funcionário #####")
  print("############################################")
  print()
  print("Alterar Funcionário")
  print("--------------------")

  CPF = input("Qual é o CPF do Funcionário que deseja alterar? ")
  if CPF in funcionarios:
    print("Funcionário encontrado:")
    print("##### CPF:", CPF)
    print("##### Nome: ", funcionarios[CPF][0])
    print("##### Email: ", funcionarios[CPF][1])

    nome = input("Digite o novo nome do Funcionário: ")
    email = input("Digite o novo Email do Funcionário: ")
    funcionarios[CPF] = [nome, email]

    print("Funcionário alterado com sucesso!")
    salvarFuncionarios()
  else:
    print("Funcionário não encontrado.")

  input("Tecle <ENTER> para continuar...")


def excluirFuncionario():
  print()
  print("############################################")
  print("##### Você está no Excluir Funcionário #####")
  print("############################################")
  print()
  print("Excluir Funcionário")
  print("--------------------")

  CPF = input("Qual é o CPF do Funcionário que deseja excluir? ")

  if CPF in funcionarios:
    print("Funcionário encontrado:")
    print("##### CPF:", CPF)
    print("##### Nome:", funcionarios[CPF][0])
    print("##### Email:", funcionarios[CPF][1])
    print("--------------------")

    confirmacao = input(
        "Tem certeza que deseja excluir este funcionário? (s/n): ").lower()
    if confirmacao == 's':
      del funcionarios[CPF]
      print("Funcionário excluído com sucesso!")
      salvarFuncionarios()
    else:
      print("Exclusão cancelada.")
  else:
    print("Funcionário não encontrado.")

  input("Tecle <ENTER> para continuar...")


def relatorioFuncionarios():
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


# Se esse módulo for executado diretamente, carrega os funcionários

arq_funcionarios = open("Funcionarios.dat", "wb")
pickle.dump(funcionarios, arq_funcionarios)
arq_funcionarios.close()
