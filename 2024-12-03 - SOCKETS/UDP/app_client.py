import socket

HOST_IP   = 'localhost'    # Definindo o IP do servidor   
HOST_PORT = 50000          # Definindo a porta do servidor  
PAGE_CODE = 'utf-8'        # Definindo o código da página

# Criando o socket UDP
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Endereço e porta do servidor
addressServer = (HOST_IP, HOST_PORT)

# Digitando a mensagem a ser enviada
mensagem = input('Digite uma mensagem: ')

# Enviando uma mensagem para o servidor
socketCliente.sendto(mensagem.encode(PAGE_CODE), addressServer)

# Fechando o socket
socketCliente.close()
