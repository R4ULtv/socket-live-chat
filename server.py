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

# list of message
messages = []

# setting up the socket
socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.bind((config["server"]["ip"], config["server"]["port"]))
socket.listen(5)

# connection function
def handle_client(s,a):
    name = find_name(a)
    print(f"\t\t[-- {name} as Connected --]")

    while True:
        try:
            msg = s.recv(1024).decode('utf-8')

            messages.append({"name": name, "msg": msg})

        except ConnectionResetError:
            print(f"\t\t[-- {name} as Disconnected --]")
            del_user(address=a)
            return

# find the name based from ip and port
def find_name(address):
    for client in clients:
        if client["address"] == address:
            return client["name"]
    return None

# delete client from clients list
def del_user(name=None, address=None):
    for client in clients:
        if client["name"] == name:
            client.remove(client)
        if client["address"] == address:
            client.remove(client)

# server loop
while True:
        sc,ad = socket.accept()
        clients.append({"name": random.choice(names), "address": (ad[0], ad[1])})
        t.Thread(target = handle_client, args=(sc,ad)).start()
        
    