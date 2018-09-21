import socket

PORT = 58000
BUFF_SIZE = 80

# create a UDP socket
server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# bind the adress to the socket
server.bind(('',PORT))

# receive and print the message
data, client = server.recvfrom(BUFF_SIZE)
print(data.decode("utf-8"))

# send a message
server.sendto(str.encode("I am the server! I have received your message"), client)

# close the socket
server.close()
