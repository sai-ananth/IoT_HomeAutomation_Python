import socket 
s = socket.socket()          
print ("Socket successfully created")
port = 12345
productId = "3"
s.bind(('', port))         
print ("socket binded to %s" %(port))
s.listen(5)      
print ("socket is listening")
while True:
    c, addr = s.accept() 
    output = productId
    c.send(output.encode('utf-8'))
    status =c.recv(1024).decode()
    if status == "on" or status == "off":
        output = 'Updated the status Successfully'
        print(output)
    c.send(output.encode('utf-8'))
    c.close() 
