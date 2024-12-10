import socket

HOST_IP   = 'localhost'    # Definindo o IP do servidor   
HOST_PORT = 50000          # Definindo a porta do servidor  
PAGE_CODE = 'utf-8'        # Definindo o código da página

# Criando o socket UDP
socketCliente = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Endereço e porta do servidor
addressServer = (HOST_IP, HOST_PORT)

print('\nCliente UDP aguardando mensagens...\nPressione CTRL+C para interromper...\n')

while True:
   try:
      # Digitando a mensagem a ser enviada
      mensagem = input('Digite uma mensagem: ')
   except KeyboardInterrupt:
      break
   else:
      # Enviando uma mensagem para o servidor
      socketCliente.sendto(mensagem.encode(PAGE_CODE), addressServer)
      # Recebendo echo do servidor
      dado_retorno, ip_retorno = socketCliente.recvfrom(1024)
      mensagem_volta = dado_retorno.decode(PAGE_CODE)
      print (f'Echo recebido {ip_retorno}: {mensagem_volta} ')

# Fechando o socket
socketCliente.close()
