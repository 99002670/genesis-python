import socket
from socket import *

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind(("127.0.0.1", 9999))
server_socket.listen(10)
print("waiting for connections...")
connection, addr = server_socket.accept()
# print("server side:", connection)
# print("connection received...")
data = connection.recv(1024)
print("message from client is:", data.decode())
server_socket.close()
