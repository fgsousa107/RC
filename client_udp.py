import socket

PORT = 58000
BUFF_SIZE = 80

# create the socket
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

# get the server's ip address
server_ip = socket.gethostbyname('localhost')

# send a message
client.sendto(str.encode("Hello! I'm the client, are you ther server?"),(server_ip,PORT))

# receive a message and print it
data = client.recv(BUFF_SIZE)
print(data.decode("utf-8"))

# close the socket
client.close()
