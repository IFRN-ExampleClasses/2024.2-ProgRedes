import socket, sys

host = input('\nInforme o nome do HOST ou URL do site: ')

# https://pt.wikipedia.org/wiki/Lista_de_portas_dos_protocolos_TCP_e_UDP
lstPorts = [22, 23, 25, 80, 443, 5432, 8080]

try:
    ip_host = socket.gethostbyname(host)
except:
    sys.exit(f'\nERRO: Não foi possível resolver o nome do host.\n{sys.exc_info()}')
else:
    print(f'\nIP do HOST: {ip_host}\n')
    for port in lstPorts:
        socketTeste = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socketTeste.settimeout(5)
        print(f'\nTestando a porta {port:>4}... ', end='')
        try:
            socketTeste.connect((ip_host, port))
        except KeyboardInterrupt:
            sys.exit('\n\nSaindo...\n')
        except:
            print(f'ERRO... {sys.exc_info()}')
        else:
            print(f'OK...')
        finally:
            socketTeste.close()