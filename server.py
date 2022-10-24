import socket as s
import threading as t

# setting up the socket
socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.bind(("127.0.0.1", 1028))
socket.listen(5)

# connection function
def connection(s,a):
    try:
        print(f"{str(a)}: {str(s.recv(1024).decode('utf-8'))}")
    except ConnectionResetError:
        print("a client as disconnected")

# server loop
while True:
        sc,ad = socket.accept()
        t.Thread(target = connection, args=(sc,ad)).start()
    