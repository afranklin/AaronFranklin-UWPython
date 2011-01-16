import socket 
import time

host = '' 
port = 50000
backlog = 5 
size = 1024 
s = socket.socket(socket.AF_INET,
                  socket.SOCK_STREAM) 
s.bind((host,port)) 
s.listen(backlog) 
while True: 
    client, address = s.accept()
    print "first number"
    data1 = client.recv(size)
    print "second number"
    data2 = client.recv(size)
    client.send(data1+data2)
    client.close()
