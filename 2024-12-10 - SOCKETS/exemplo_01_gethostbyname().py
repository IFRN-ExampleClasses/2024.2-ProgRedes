import socket, sys

host  = input('\nInforme o nome do HOST ou URL do site: ')

try:
   ip_host = socket.gethostbyname(host)
except:
   sys.exit(f'\nERRO: Não foi possível resolver o nome do host.\n{sys.exc_info()}')
else:
   print(ip_host)