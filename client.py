import socket as s
import threading as t
import json
import random

# load config file
with open('config.json') as config:
    config = json.load(config)

# load config file
with open('names.json') as names:
    names = json.load(names)

# setting up the connection
socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.connect((config["server"]["ip"], config["server"]["port"]))

# send username
user = input("Username: ")
if user == "":
    user = random.choice(names)
    print("Username not entered. Your name now is ", user)    
socket.send(user.encode('utf-8'))

# get the msgs from the socket
def recive():
    while True:
        print(f"\n{socket.recv(1024).decode('utf-8')}")

# get the input and send to the socket
def send():
    while True:
        string = str(input("You: "))
        if string != "":
            socket.send(string.encode('utf-8'))

# two separete thread for handle send and recive at the same time
t.Thread(target=send).start()
t.Thread(target=recive).start()
