import socket

HOST_IP   = 'localhost'    # Definindo o IP do servidor   
HOST_PORT = 50000          # Definindo a porta do servidor  
PAGE_CODE = 'utf-8'        # Definindo o código da página

# Criando o socket TCP
socketCliente = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Endereço e porta do servidor
addressServer = (HOST_IP, HOST_PORT)

# Conectando ao servidor
socketCliente.connect(addressServer)

print('\nServidor TCP aguardando conexões...\nPressione Ctrl+C para interromper...\n')

while True:
   try:
      # Digitando a mensagem a ser enviada
      mensagem = input('Digite uma mensagem: ')
   except KeyboardInterrupt:
      socketCliente.send('SAIR'.encode(PAGE_CODE))
      print('\nCliente encerrado pelo usuário...')
      break
   else:
      # Enviando a mensagem para o servidor
      socketCliente.send(mensagem.encode(PAGE_CODE))
      # Recebendo echo do servidor
      dados = socketCliente.recv(1024)   
      mensagem_volta = dados.decode(PAGE_CODE)
      print (f'Echo recebido: {mensagem_volta} ')

# Fechando o socket
socketCliente.close()
