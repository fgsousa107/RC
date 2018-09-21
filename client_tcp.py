import socket

PORT = 58000
BUFF_SIZE = 80

# create TCP socket
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# get ip of this machine
server_ip = socket.gethostbyname('localhost')

# connect to the server's socket
client.connect((server_ip,PORT))

# send information
client.sendall(str.encode('Hello'))

# receive information back from the server
data = client.recv(BUFF_SIZE)

# print the information
print(data.decode("utf-8"))

# close the socket
client.close()
