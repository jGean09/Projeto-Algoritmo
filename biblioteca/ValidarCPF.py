from biblioteca.dados import carregarDados, salvarDados


# AUTHOR Flavius Gorgonio
def validaCPF(cpf):
    funcionario = carregarDados("Funcionarios.dat")

    if cpf in funcionario:
        print("CPF já cadastrado!")
        print("Digite um novo CPF!")
        return False  # CPF já existente é considerado válido, mas quero que volte pra a pra digitar u mque não exxiste

    tam = len(cpf)
    if tam != 11:
        return False

    for i in range(11):
        if (cpf[i] < '0') or (cpf[i] > '9'):
            return False

    soma = 0
    for i in range(9):
        soma += (int(cpf[i]) * (10 - i))
    d1 = 11 - (soma % 11)
    if (d1 == 10 or d1 == 11):
        d1 = 0
    if d1 != int(cpf[9]):
        return False

    soma = 0
    for i in range(10):
        soma += (int(cpf[i]) * (11 - i))
    d2 = 11 - (soma % 11)
    if (d2 == 10 or d2 == 11):
        d2 = 0
    if d2 != int(cpf[10]):
        return False

    return True
