import pickle
import os
from biblioteca.dados import carregarDados, salvarDados

#
# AUTHOR CHATGPT
#gerar um novo ID sequencial


#erro de sobrescrever o id foi resolvido
def gerarNovoID(nome_arquivo):
    ids = carregarDados(nome_arquivo)

    # Verifica se a lista de IDs foi carregada corretamente
    if not isinstance(ids, list):
        ids = []

    if not ids:
        novo_id = 1
    else:
        novo_id = max(ids) + 1

    ids.append(novo_id)
    salvarDados(nome_arquivo, ids)
    return novo_id
