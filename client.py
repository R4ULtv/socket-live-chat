import socket as s

while True:
    socket = s.socket(s.AF_INET, s.SOCK_STREAM)
    socket.connect(("127.0.0.1", 1028))
    socket.send(str(input()).encode())
