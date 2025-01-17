import socket, sys

# ----------------------------------------------------------------------
# Documentação Protocolo HTTP
# https://datatracker.ietf.org/doc/html/rfc2616
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview
#
# Status Code (Códigos de Resposta HTTP)
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status
#
# Headers (Cabeçalhos HTTP)
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers
# ----------------------------------------------------------------------

# ----------------------------------------------------------------------
PORT        = 80
CODE_PAGE   = 'utf-8'
BUFFER_SIZE = 2048
# ----------------------------------------------------------------------

host = input('\nInforme o nome do HOST ou URL do site: ')

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.settimeout(5)

try:
    tcp_socket.connect((host, PORT))
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')
else:
    requisicao = f'GET / HTTP/1.1\r\nHost: {host}\r\nAccept: text/html\r\n\r\n'
    try:
        tcp_socket.sendall(requisicao.encode(CODE_PAGE))
    except:
        print(f'\nERRO.... {sys.exc_info()[0]}')
    else:
        print('-'*50)
        while True:
            resposta = tcp_socket.recv(BUFFER_SIZE).decode(CODE_PAGE)
            if not resposta: break
            print(resposta)
        print('-'*50)
    tcp_socket.close()