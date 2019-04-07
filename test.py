import socket
import sys


HOST = '127.0.0.1'
PORT = 5556
s = socket.socket()
s.bind((HOST, PORT))
s.connect((HOST, PORT))

while 1:
    msg = input("Command To Send: ")
    if msg == "close":
       s.close()
       sys.exit(0)
    s.send(msg.encode())