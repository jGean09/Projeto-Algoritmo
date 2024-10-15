
# AUTHOR Flavius Gorgonio
#https://replit.com/@flaviusgorgonio/Projeto-Escola-V12?v=1#main.py
def ler_nome():
  print()
  nome = input("##### Nome: ")
  while not (validar_nome(nome)):
    print("##### Ops! O nome informado é inválido!")
    print("##### Tente novamente...")
    print()
    nome = input("##### Nome: ")
  return nome



# AUTHOR Flavius Gorgonio
#https://replit.com/@flaviusgorgonio/Projeto-Escola-V12?v=1#main.py
def validar_nome(nome):
  nome = nome.replace(' ', '')
  return bool(nome.isalpha())
