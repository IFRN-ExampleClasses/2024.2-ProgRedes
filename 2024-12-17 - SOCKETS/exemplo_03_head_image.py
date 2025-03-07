import socket

# --------------------------------------------------
# Documentação Protocolo HTTP
#
# https://datatracker.ietf.org/doc/html/rfc2616
# https://developer.mozilla.org/pt-BR/docs/Web/HTTP/Overview
# https://www.ibm.com/docs/pt-br/power10/7063-CR2?topic=apis-http-protocol
# --------------------------------------------------

url_host    = 'www.httpbin.org'
url_image   = '/image/png'

#url_host    = 'ead.ifrn.edu.br'
#url_image   = 'portal/wp-content/uploads/2019/03/4Iwakb0M_400x400.png'

url_host = 'www.youtube.com'
url_image = 'watch?v=iMXaH0s_8W4'
#https://youtu.be/iMXaH0s_8W4

url_request = f'HEAD /{url_image} HTTP/1.1\r\nHOST: {url_host}\r\n\r\n' 

HOST_PORT   = 80
BUFFER_SIZE = 1024

sock_img = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock_img.connect((url_host, HOST_PORT))
sock_img.sendall(url_request.encode())

print('-'*50)
dados = sock_img.recv(BUFFER_SIZE)
print(str(dados, 'utf-8'))
print('-'*50)

sock_img.close()