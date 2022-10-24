import socket as s
import threading as t
import random

# setting up the socket
socket = s.socket(s.AF_INET, s.SOCK_STREAM)
socket.bind(("127.0.0.1", 1028))
socket.listen(5)

names = ["Sufyaan Oneil", "Kavita O'Quinn", "Jayda Sullivan", "Ellis Shaw", "Sunil Robin", "Darnell Russell", "Pierce Vinson", "Dave Bautista", "Lilly-Ann Lawson", "Hannah Guerrero"]
user = []
# connection function
def connection(s,a):
    while True:
        try:
            print(f"{str(a)}: {str(s.recv(1024).decode('utf-8'))}")
        except ConnectionResetError:
            print(f"{str(a)} as disconnected")
            return


# server loop
while True:
        sc,ad = socket.accept()
        user.append({random.choice(names), ad})
        print(user)
        t.Thread(target = connection, args=(sc,ad)).start()
    