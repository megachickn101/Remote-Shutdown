
import time
import sys
import socket
import os

s = socket.socket()
host = socket.gethostname()
port = 8080
s.bind((host, port))
print(host)
print("waiting...")
s.listen(1)
conn, addr = s.accept()
print(f"{addr} connected to server")

command = input(str("Command: "))
conn.send(command.encode())
print("Sent... Standby")
time.sleep(1)
data = conn.recv(1024)
if data:
    print("Command Received")
