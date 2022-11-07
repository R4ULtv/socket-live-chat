import socket as s
import threading
import json

# load config file
with open('config.json') as config:
    config = json.load(config)

# list of clients that contains name, address(ip,port)
clients = []
# list of aliases of the clients
aliases = []

# setting up the socket
socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.bind((config["server"]["ip"], config["server"]["port"]))
socket.listen(5)

# broadcast messages
def broadcast(socket, message):
    for client in clients:
        if client != socket:
            client.send(message)

# handle clients
def handle_client(s,a):

    # recive username and append client, alias
    alias = s.recv(1024).decode('utf-8')
    clients.append(s)
    aliases.append(alias)

    print(f"\t\t[-- {alias} as Connected --]")
    
    # loop send e recive msg
    while True:
        try:
            msg = f"{alias}: {s.recv(1024).decode('utf-8')}"
            print(msg)
            broadcast(s, msg.encode('utf-8'))

        except ConnectionResetError:
            # ConnectionResetError exception raise when the connection ends
            print(f"\t\t[-- {alias} as Disconnected --]")

            # delete the client and terminate the thread
            del_client_alias(s)
            return

# delete client from clients list
def del_client_alias(socket):
    for client in clients:
        if client==socket:
            del aliases[clients.index(client)]
            clients.remove(client)

# server loop
while True:
    # accept socket connection
    sc,ad = socket.accept()

    # create a Thread
    threading.Thread(target = handle_client, args=(sc,ad)).start()
        
    