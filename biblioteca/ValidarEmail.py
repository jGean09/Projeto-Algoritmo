

# AUTHOR Flavius Gorgonio
def ler_email():
  email = input("##### E-mail: ")
  while not (validar_email(email)):
    print("##### Ops! O e-mail informado é inválido!")
    print("##### Tente novamente...")
    print()
    email = input("##### E-mail: ")
  return email


# AUTHOR Flaviu Gorgonio
def validar_email(email):
  if email.count('@') != 1:
    return False
  if email.count('.') == 0:
    return False
  tam = len(email)
  if email[0] == '@' or email[tam - 1] == '@':
    return False
  if email[0] == '.' or email[tam - 1] == '.':
    return False
  pos = email.find('@')
  dominio = email[pos:]
  if dominio.count('.') == 0:
    return False
  return True
