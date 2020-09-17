import socket


TCP_IP = '192.168.1.67'
TCP_PORT = 5005
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"

PACKAGE = MESSAGE.encode('utf-8')

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
s.send(PACKAGE)
data = s.recv(BUFFER_SIZE)
s.close()

print("received data: {}".format(data))