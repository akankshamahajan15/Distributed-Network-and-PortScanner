import socket

HOST = '127.0.0.1'
PORT = 65432

s = socket.socket()
print("Socket created")

s.bind(('', PORT))
print("Socket binded to %s" %(PORT))

s.listen(5)
