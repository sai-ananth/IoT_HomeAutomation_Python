import socket
import sys
s = socket.socket()
port = 12345

s.connect((sys.argv[1], port))
print (s.recv(1024).decode())
msg = sys.argv[2]
s.send(msg.encode('utf-8'))
print (s.recv(1024).decode())
s.close()