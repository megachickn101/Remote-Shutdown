
import time
import sys
import os
import socket

s = socket.socket()
host = "Insert Hostname"
port = 8080
s.connect((host,port))
print("Connected")

command = s.recv(1024)
command =  command.decode()
if command == "shutdown":
    s.send("command recieved".encode())
    os.system("shutdown /s")
