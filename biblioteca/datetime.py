
# AUTHOR CHATGPT
import datetime
def obter_data_atual():
    # Obter a data atual
    data_atual = datetime.datetime.now()

    # Formatando a data como string no formato desejado
    data_formatada = data_atual.strftime("%d/%m/%Y %H:%M:%S")

    return data_formatada