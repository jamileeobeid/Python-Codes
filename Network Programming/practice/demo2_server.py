#server.py
import socket

host_name = socket.gethostname()
port = 12345

server_socket = socket.socket()
server_socket.bind((host_name,port))
server_socket.listen()

conn, addr = server_socket.accept()
print("connection from", str(addr))

data = conn.recv(1024)
print(data.decode())

conn.close()
