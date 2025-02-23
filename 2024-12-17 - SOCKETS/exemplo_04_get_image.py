import socket

# --------------------------------------------------
# Documentação Protocolo HTTP
#
# https://datatracker.ietf.org/doc/html/rfc2616
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview
# https://www.ibm.com/docs/pt-br/power10/7063-CR2?topic=apis-http-protocol
# --------------------------------------------------

url_host    = 'httpbin.org'
url_image   = '/image/png'
url_request = f'GET {url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 

HOST_PORT   = 80
BUFFER_SIZE = 512

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, HOST_PORT))
sock_img.sendall(url_request.encode())

print('-'*50)

while True:
   dados = sock_img.recv(BUFFER_SIZE)
   if not dados: break
   print(dados)

print('-'*50)

sock_img.close()