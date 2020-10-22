import socket

host = "localhost"
port = 8131

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

s.connect((host,port))
msg = s.recv(1024)
print(msg.decode("utf-8"))

s.sendall(bytes("Client connect","utf-8"))



