import socket 
import time

host = '' 
port = 50001
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
    data1int = int(data1)
    print "second number"
    data2 = client.recv(size)
    data2int = int(data2)
    client.send(data1int+data2int)
    client.close()
