# bibliotecas a serem importadas
import pywhatkit
import keyboard
import time
from datetime import datetime

# definir lista de contatos
lista_contatos = []

# solicitar inserção dos contatos
outro_contato = 1
contato = str(input('Informe o primeiro contato (Ex: +5585922334455): \n'))

# verifica se há a intenção do usuario em adicionar mais contatos a lista
while outro_contato == 1:
    lista_contatos.append(contato)
    outro_contato = int(input("Deseja informar outro contato? [1 - SIM / 2 - NÃO]\n"))
    # caso não queira adicionar mais contatos o loop é imterrompido
    if outro_contato != 1:
        break
    contato = str(input('Informe outro contato (Ex: +5585922334455): '))

saudacao = '' # variavel para iniciar o texto da mensagem a ser enviada

# verificação de horário para alterar a saudacao conforme a hora do dia
if datetime.now().hour >= 6 and datetime.now().hour <= 12:
    saudacao = "Bom dia!"
elif datetime.now().hour >= 12 and datetime.now().hour <= 18:
    saudacao = "Boa tarde!"

# texto que será enviado para os contatos presentes na lista
texto_msg = str(input('Informe a mensagem: \n'))

# string que contem o texto completo da mensagem para envio
mensagem = f'{saudacao} {texto_msg}'

# função de envio de mensagem, definindo um intervalo de tempo para envio
def enviarMsg(list, mensagem):
    while len(lista_contatos) >= 1:
        pywhatkit.sendwhatmsg(
            list[0], mensagem, 
            datetime.now().hour, 
            datetime.now().minute + 1
        )
        del lista_contatos[0]
        time.sleep(30)

# bloco para confirmar o envio da mensagem
enviar = str(input("Confirma envio da mensagem? [S - SIM / N - NÃO]\n").upper())

if enviar == "S":
    enviarMsg(lista_contatos, mensagem)
else:
    print("Envio cancelado...")

print("Concluído!")
