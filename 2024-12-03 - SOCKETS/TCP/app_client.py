import socket

HOST_IP   = 'localhost'    # Definindo o IP do servidor   
HOST_PORT = 50000          # Definindo a porta do servidor  
PAGE_CODE = 'utf-8'        # Definindo o código da página

# Criando o socket TCP
socketCliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Endereço e porta do servidor
addressServer = (HOST_IP, HOST_PORT)

# Conectando ao servidor
socketCliente.connect(addressServer)

# Digitando a mensagem a ser enviada
mensagem = input('Digite uma mensagem: ')

# Enviando a mensagem para o servidor
socketCliente.send(mensagem.encode(PAGE_CODE))

# Fechando o socket
socketCliente.close()
