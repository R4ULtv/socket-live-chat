import socket as s
import threading as t
import random
import json

# load config file
with open('config.json') as config:
    config = json.load(config)

# names file for random name
with open('names.json') as names:
    names = json.load(names)

# list of clients that contains name, address(ip,port)
clients = []
aliases = []

# setting up the socket
socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.bind((config["server"]["ip"], config["server"]["port"]))
socket.listen(5)

# broadcast messages
def broadcast(socket, message):
    for client in clients:
        client.send(message)

# handle clients
def handle_client(s,a):
    alias = aliases[clients.index(s)]
    print(f"\t\t[-- {alias} as Connected --]")

    while True:
        try:
            msg = f"{alias}: {s.recv(1024).decode('utf-8')}"
            broadcast(s, msg.encode('utf-8'))

        except ConnectionResetError:
            print(f"\t\t[-- {alias} as Disconnected --]")
            del_client(s)
            return

# delete client from clients list
def del_client(socket):
    for client in clients:
        if client==socket:
            clients.remove(client)

# server loop
while True:
        sc,ad = socket.accept()
        clients.append(sc)
        aliases.append(random.choice(names))
        t.Thread(target = handle_client, args=(sc,ad)).start()
        
    