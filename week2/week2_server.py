import socket 
import time

host = '' 
port = 50002
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
while True: 
    client, address = s.accept()
    data1 = client.recv(size)
    data2 = client.recv(size)
    solution = int(data1) + int(data2)
    client.send(data1int+data2int)
    client.close()
