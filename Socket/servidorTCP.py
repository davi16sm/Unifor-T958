import socket
porta = 12001
socketServidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socketServidor.bind(('',porta))
socketServidor.listen(1)
print 'Servidor escutando na porta '+str(porta)
while 1:
    conexao, enderecoCliente = socketServidor.accept()	
    mensagem = conexao.recv(2048)
    mensagemModificada = mensagem.upper()
    conexao.send(mensagemModificada)
    conexao.close();
