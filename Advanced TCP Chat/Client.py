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


with open('NewFile.jpg','wb') as f:
     while True:
          data=client_socket.recv(1024)
          if not data:
               break
          else:
               f.write(data)
print('Finishing............File Saved at ',str(os.getcwd()))

