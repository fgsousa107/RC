import socket

PORT = 58000
BUFF_SIZE = 80

# create a TCP socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# bind the address to the socket
server.bind(('',PORT))

# listen, enables the server to accept connections
server.listen(5)

# accept client connections, it returns a new socket and the client's address
client_connection, client_address = server.accept()

# receive information and print it
data = client_connection.recv(BUFF_SIZE)
print(data.decode("utf-8"))

# send something back
client_connection.sendall(str.encode('Hey, I\'m the server'))

# close everything
client_connection.close()
server.close()
