import socket

host = '192.168.0.66'
port = 4356

s = socket.socket()
s.connect((host, port))
filename = input("Filename? -> ")
file = open(filename, 'rb')
file_data = file.read(1024)
# send file name
s.send(filename.encode("utf-8"))

s.send(file_data)

print("File has been uploaded.")

s.close()
