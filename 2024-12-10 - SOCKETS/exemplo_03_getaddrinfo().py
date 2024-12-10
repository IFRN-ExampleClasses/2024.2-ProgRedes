import socket, sys

server = input('\nInforme o nome do HOST ou URL do site: ')

try:
   infos = socket.getaddrinfo(host=server, port=80)
except:
   sys.exit(f'\nERRO:Não foi possível resolver o nome do host.\n{sys.exc_info()}')
else:
   print(f'\nInformações sobre o HOST {server}:')
   for info in infos:
      print('\n----------------------------------------')
      print(f'Info ...................: {info}')
      print(f'Family .................: {info[0]}')
      print(f'Type ...................: {info[1]}')
      print(f'Proto ..................: {info[2]}')
      print(f'Canonical Name (CNAME) .: {info[3]}')   
      print(f'SOCKET Address .........: {info[4]}')
