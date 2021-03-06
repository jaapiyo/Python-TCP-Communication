import socket


TCP_IP = '0.0.0.0'
TCP_PORT = 5005
BUFFER_SIZE = 20  # Normally 1024, but we want fast response

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print('\nConnection address: {}'.format(addr))
while 1:
    data = conn.recv(BUFFER_SIZE)
    if not data: break
    message = data.decode('utf-8')
    print("received data: {}".format(data))
    conn.send(data)  # echo
    for i in range(100):
        conn.send(i.to_bytes(1, byteorder='big'))

conn.close()