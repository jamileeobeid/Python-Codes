#client.py

import socket

host_name = socket.gethostname()
port = 12345

client_socket = socket.socket()
client_socket.connect((host_name,port))

msg = 'hello'
client_socket.send(msg.encode())
reply = client_socket.recv(1024)
print("reply is", reply.decode())

client_socket.close()
