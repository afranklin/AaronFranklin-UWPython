import socket 

host = 'block115389-wtj.blueboxgrid.com'
port = 50000 
size = 1024
s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port)) 
s.send(2)
s.send(3)
data = s.recv(size) 
s.close() 
print 'Received:', data

