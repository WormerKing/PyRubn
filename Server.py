import socket

host = "localhost"
port = 8131

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(20)

while True:
	client,adress = s.accept()
	print(f"Connecting {adress}")

	with open("Yorum.txt","a") as dosya:
		msg = client.recv(1024)
		dosya.write(msg.decode("utf-8"))
	
	
	

