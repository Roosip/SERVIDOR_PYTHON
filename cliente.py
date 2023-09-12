# criando um cliente para conexão com o servidor Python
import socket
 
host = '192.168.3.10'  # mesmo local do servidor
porta = 8800      # mesma porta do servidor
 
soquete = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
envio = (host,porta)
soquete.connect(envio)
 
print('Digite: S e pressione ENTER para encerrar...') 
print('DIGITE A MENSAGEM: ')
mensagem = input()
 
while mensagem not in ('s','S'):
    soquete.send(str(mensagem).encode())
    mensagem = input()
 
soquete.close()