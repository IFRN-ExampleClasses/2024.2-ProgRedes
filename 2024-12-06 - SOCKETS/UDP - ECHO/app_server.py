import socket

HOST_IP   = ''       # Definindo o IP do servidor   
HOST_PORT = 50000    # Definindo a porta do servidor
PAGE_CODE = 'utf-8'  # Definindo o código da página

# Criando o socket UDP
socketServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Ligando o servidor ao IP e Porta que será "escutado"
socketServer.bind((HOST_IP, HOST_PORT))

print('\nServidor UDP aguardando mensagens...\nPressione Ctrl+C para interromper...\n')

while True:
   try:
      # Recebendo dados do cliente
      dados, endereco_cliente = socketServer.recvfrom(1024)
      print(f'Recebido: {dados.decode(PAGE_CODE)} de {endereco_cliente}')
      mensagem_retorno = f'DEVOLVENDO: {dados.decode(PAGE_CODE)}'
      # Enviando mensagem de retorno ao cliente
      socketServer.sendto(mensagem_retorno.encode(PAGE_CODE), endereco_cliente)
   except KeyboardInterrupt:
      print('\nServidor encerrado pelo usuário...')
      break
      
# Fechando o socket antes de terminar
socketServer.close()
