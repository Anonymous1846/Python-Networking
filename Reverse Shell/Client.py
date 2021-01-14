#the Client part will reside in the target machine 
import os
import subprocess
import socket


HOST=''
PORT=43000

print('Initializing the Socket Object')
client_socket=socket.socket()
print('Connecting to Server.....')
client_socket.connect((HOST,PORT))
print(f'Connected to {HOST} at Port {PORT}')

while True:
	pass