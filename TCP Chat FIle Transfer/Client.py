#A Simple One on One Chat App with One Server and One Client
#this module is part of the Client Progm
import socket
import threading
#avoiding the hardcoded hostname assigning
HOST=socket.gethostbyname(socket.gethostname())
PORT=32500
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
print(f'Now Connected to Server at {HOST}')

msg=''
while True:
    msg=client_socket.recv(1024).decode()
    if msg.lower()=='exit !':
        client_socket.close()
        break
    print(msg)
    msg=input('Client: ')
    client_socket.send(msg.encode())
    

    
