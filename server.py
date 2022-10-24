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

# list of users that contains name, address(ip,port)
users = []

# setting up the socket
socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.bind((config["server"]["ip"], config["server"]["port"]))
socket.listen(5)

# connection function
def connection(s,a):
    print(f"\t\t[-- {find_name(a)} as Connected --]")
    while True:
        try:
            print(f"{find_name(a)}: {str(s.recv(1024).decode('utf-8'))}")
            s.send(" ".encode("utf-8"))
        except ConnectionResetError:
            print(f"\t\t[-- {find_name(a)} as Disconnected --]")
            del_user(address=a)
            return

# find the name based from ip and port
def find_name(address):
    for user in users:
        if user["address"] == address:
            return user["name"]
    return None

# delete user from users list
def del_user(name=None, address=None):
    for user in users:
        if user["name"] == name:
            users.remove(user)
        if user["address"] == address:
            users.remove(user)

# server loop
while True:
        sc,ad = socket.accept()
        users.append({"name": random.choice(names), "address": (ad[0], ad[1])})
        t.Thread(target = connection, args=(sc,ad)).start()
        
    