import socket 

host = 'block115389-wtj.blueboxgrid.com'
port = 50002
size = 1024
s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port))
first = str(1)
second = str(2)
s.send(first)
s.send(second)
data = s.recv(size) 
s.close() 
print 'Received:', data

