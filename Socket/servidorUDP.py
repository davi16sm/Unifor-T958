import socket
porta = 12000
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socketServidor.bind(('',porta))
print 'Servidor escutando na porta '+str(porta)
while 1:
    mensagem, enderecoCliente = socketServidor.recvfrom(2048)
    mensagemModificada = mensagem.upper()
    socketServidor.sendto(mensagemModificada, enderecoCliente)
