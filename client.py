from socket import *

client_socket = socket(AF_INET, SOCK_STREAM)
client_socket.connect(("127.0.0.1", 9999))
# print("client side:", client_socket)
# print("connected to server")
data = "I am client"
client_socket.send(data.encode())
client_socket.close()
