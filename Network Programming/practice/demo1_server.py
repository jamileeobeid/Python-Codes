#server.py
import socket

host_name = socket.gethostname()
port = 12345

server_socket = socket.socket()
server_socket.bind((host_name,port))
server_socket.listen()

conn, addr = server_socket.accept()
print("connection from", str(addr))

while True:
  data = conn.recv(1024)
  if not data:
    break
    
  print("received data:", data.decode())
  msg = 'hello’
  conn.send(msg.encode())
conn.close()
