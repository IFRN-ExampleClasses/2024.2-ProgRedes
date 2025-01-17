import socket, sys

# ------------------------------------------------------------
# Documentação Protocolo HTTP
# https://datatracker.ietf.org/doc/html/rfc2616
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Status
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Headers
# ------------------------------------------------------------

# ----------------------------------------------------------------------
PORT        = 80
CODE_PAGE   = 'utf-8'
BUFFER_SIZE = 2048
# ----------------------------------------------------------------------

url_host    = 'www.httpbin.org'
url_image   = '/image/png'

#url_host    = 'ead.ifrn.edu.br'
#url_image   = 'portal/wp-content/uploads/2019/03/4Iwakb0M_400x400.png'

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.settimeout(5)

try:
    tcp_socket.connect((url_host, PORT))
except:
    print(f'\nERRO.... {sys.exc_info()[0]}')
else:
    requisicao = f'GET /{url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n'
    try:
        tcp_socket.sendall(requisicao.encode(CODE_PAGE))
    except:
        print(f'\nERRO.... {sys.exc_info()[0]}')
    else:
        print('-'*50)
        while True:
            resposta = tcp_socket.recv(BUFFER_SIZE)
            if not resposta: break
            print(resposta)
        print('-'*50)
    tcp_socket.close()