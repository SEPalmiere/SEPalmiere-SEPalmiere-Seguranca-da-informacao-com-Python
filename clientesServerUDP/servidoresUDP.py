import socket

s =  socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket Criado com suceso!!!")

host = 'localhost'
porta = 5432

s.bind((host, porta))
mensagem = '\n Servidor: Olá, mensagem recebida!!!'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('Servidor enviando mensagem...')
        s.sendto(dados + (mensagem.encode()), end)