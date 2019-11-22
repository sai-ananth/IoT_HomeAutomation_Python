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
    status =c.recv(1024).decode().lower()
    print(status == "on")
    print(status == "off")
    if status == "on" or status == "off":
        output = 'Updated the status Successfully'
    else:
        output = 'Update failed'
    print(output)
    c.send(output.encode('utf-8'))
    c.close() 
