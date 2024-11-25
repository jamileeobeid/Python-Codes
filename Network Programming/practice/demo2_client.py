#client.py

import socket

host_name = socket.gethostname()
port = 12345

client_socket = socket.socket()
client_socket.connect((host_name,port))

msg = open('story.txt').read().strip()
client_socket.send(msg.encode())

client_socket.close()
