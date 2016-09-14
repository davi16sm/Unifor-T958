import socket
ip = '192.168.0.102'
porta = 12000
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
mensagem = raw_input("Digite uma mensagem: ")
socketCliente.sendto(mensagem, (ip,porta))
resposta, enderecoServidor = socketCliente.recvfrom(2048)
print resposta
socketCliente.close()
