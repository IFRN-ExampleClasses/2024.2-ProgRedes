import socket

HOST_IP   = ''        # Definindo o IP do servidor   
HOST_PORT = 50000     # Definindo a porta do servidor
PAGE_CODE = 'utf-8'   # Definindo o código da página

# Criando o socket TCP
socketServer = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

# Ligando o servidor ao IP e porta que será "escutado"
socketServer.bind((HOST_IP, HOST_PORT))

# Tornando o socket capaz de escutar conexões
socketServer.listen(5)

print('\nServidor TCP aguardando conexões...\nPressione Ctrl+C para interromper...\n')

while True:
    try:
        # Aceitando uma conexão de cliente
        conexao, endereco_cliente = socketServer.accept()
        print(f'Conexão estabelecida com {endereco_cliente}')
        
        # Recebendo dados do cliente
        dados = conexao.recv(1024)
        print(f'Recebido: {dados.decode(PAGE_CODE)} de {endereco_cliente}')
        
        # Fechando a conexão com o cliente após receber os dados
        conexao.close()        
    except KeyboardInterrupt:
        print('\nServidor encerrado pelo usuário...')
        break

# Fechando o socket do servidor
socketServer.close()
