import socket as s
import json

# load config file
with open('config.json') as config:
    config = json.load(config)


socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.connect((config["server"]["ip"], config["server"]["port"]))

print("You are connected to the chat.")

while True:
    string = str(input("You: "))
    if string != "":
        socket.send(string.encode())
        print(socket.recv(1024).decode('utf-8'))
