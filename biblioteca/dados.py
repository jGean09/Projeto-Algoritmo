import os
import pickle


# AUTHOR CHATGPT
def carregarDados(nome_arquivo):
  try:
    with open(nome_arquivo, "rb") as arquivo:
      return pickle.load(arquivo)
  except (FileNotFoundError, EOFError):
    return {}


def salvarDados(nome_arquivo, dados):
  with open(nome_arquivo, "wb") as arquivo:
    pickle.dump(dados, arquivo)
