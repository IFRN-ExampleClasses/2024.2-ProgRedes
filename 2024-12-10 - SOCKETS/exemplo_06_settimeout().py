import socket, sys

host = input('\nInforme o nome do HOST ou URL do site: ')
port = 443

try:
   ip_host = socket.gethostbyname(host)
except:
   sys.exit(f'\nERRO: Não foi possível resolver o nome do host.\n{sys.exc_info()}')
else:
   server_conn = (ip_host, port)
   socketTeste = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   socketTeste.settimeout(5)
   try:
      socketTeste.connect(server_conn)
   except:
      print(f'\nERRO: {sys.exc_info()}')
   else:
      print('\nConexão OK')
      socketTeste.close()
