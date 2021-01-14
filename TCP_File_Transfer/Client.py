#our Objective is send files sockets 
#they provide end to end file transfer 
import socket
#provide beautiful text art 
import pyfiglet
import os
import random
import pickle
server_heading=pyfiglet.figlet_format(text='File Tranfer Client.')
print(server_heading)
#initializing the socket object !
client_socket=socket.socket()
PORT=43599
HOST='127.0.0.1'
client_socket.connect((HOST,PORT))
print(f'Conencted to {HOST}')
file_size=int(client_socket.recv(1024).decode())
print(f'The expected size of the file is {file_size} bytes')

print(f'Recieving {file_size} bytes')
data=pickle.loads(client_socket.recv(file_size))

with open('NewFile.txt','wb') as f:
     f.write(data.encode())
print('Finishing............File Saved at ',str(os.getcwd()))

