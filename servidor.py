import socket
from datetime import *

host = '192.168.3.10' # local host
porta = 8800 # porta de conexão

soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # TCP/IP AF_INET: para conexão entre endereços IP  e é a que vai determinar um valor para a porta e SOCK_STREAM: para usar o protocolo TCP
recebe = (host, porta) # variavel atribuida do host e da porta
soquete.bind(recebe) #variável soquete utiliza a função bind, para apanhar os valores da variável recebe (colocar um valor de IP e da porta no socket)
soquete.listen(3) # conexão atribuída a variável soquete aceita (ouve) até duas conexões cliente, podendo aumentar a capacidade

print('\nSERVIDOR INICIANDO... IP: ', host, 'PORTA: ', porta, ' EM: ', datetime.now().strftime('%d/%m%y - %H:%M:%S')) # imprime o endereço de IP do servidor e o numero da porta quando acessado

while True:
    conexao, enderecoIP = soquete.accept() # essa variavel recebe e aceita a conexão do cliente através da função accept()
    print('\nSERVIDOR ACESSADO PELO CLIENTE: ', enderecoIP, ' EM: ',datetime.now().strftime('%d/%m/%y - %H:%M:%S')) #imprime o endereço IP do cliente e um valor para a porta, gerada pela função AF_INET

    while True: # esse while True vai receber a mensgem do cliente, com a variavel mensagem que vai receber o valor da variavel conexao que o soquete aceitou e atraves da funcao recv(2048), recebe o texto da mensagemo valor 2048 significa que vai aceitar textos com até 2k Bytes de caracteres, podendo ser alterado
        mensagem = conexao.recv(2048)
        if not mensagem: # aqui se não receber mais nenhuma mensagem, o loop sera interrompido
            break
        print('\nIP CLIENTE:', enderecoIP) # aqui vai imprimir o numero de ip no servidor
        print('MENSAGEM RECEBIDA: ', mensagem.decode(), ' - ',datetime.now().strftime('%H:%M:%S'))# e aqui vai imprimir a mensagem recebida do cliente

    print('CONEXÃO COM O CLIENTE FINALIZADA...', enderecoIP, ' EM: ',datetime.now().strftime('%d/%m/%y - %H:%M:%S'))# aqui vai imprimir a mensagem caso o cliente interrompa a conexão
    conexao.close()

"""Nas linhas 12, 16, 23 e 25, foi acrescentada a função datetime.now()
que captura a data do sistema e com o print a data e a hora também são impressas, foi utilizada
junto à função strftime() para formatarmos a data e a hora do sistema, porque a data vem no
padrão britânico: ano/mês/dia e os segundos são mostrados em frações de até milissegundos.
Então, utilizamos os parâmetros: %d = dia, %m = mês, %Y = ano com 4 dígitos, %H = hora no padrão 24
(se quiser usar o padrão 12, utilize %I), %M = minutos e %S = segundos."""
