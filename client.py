import socket as s

socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.connect(("127.0.0.1", 1028))

print("You are connected to the chat.")

while True:
    string = str(input("You: "))
    if string != "":
        socket.send(string.encode())
        print(socket.recv(1024).decode('utf-8'))
