
import socket
import os


port = 4356

s = socket.socket()

s.bind(('',port))
print("Socket is binded to"+str(port))

s.listen(5)
print("socket is listening")

print ("Server Started.")
while True:
        conn, addr = s.accept()
        print ("client connedted ip:<" + str(addr) + ">")
        filename = conn.recv(1024)
        file = open(filename,'wb')
        file_data = conn.recv(1024)
        file.write(file_data)
        file.close()
        print("File has been stored.")

s.close()

