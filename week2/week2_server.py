import socket 
import time

host = '' 
port = 50004
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
    solution = str(int(data1) + int(data2))
    client.send(solution)
    client.close()
