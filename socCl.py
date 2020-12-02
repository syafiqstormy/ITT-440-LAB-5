import socket

HOST = '192.168.0.66'
PORT = 8888

s = socket.socket()

s.connect((HOST, PORT))
data = s.recv(1024)

s.send(b'Hi, saya client, Terima Kasih!')

print(data)

s.close()
