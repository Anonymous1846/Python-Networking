#A Simple One on One Chat App with One Server and One Client
#this module is part of the Server Progm
import socket
import threading
#avoiding the hardcoded hostname assigning
HOST=socket.gethostbyname(socket.gethostname())
PORT=32500

server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(f'Binding The Host {HOST} with Port Number :{PORT}')
server_socket.bind((HOST,PORT))
print('Listening to the Clients')
server_socket.listen()
print('Now Ready to Accept Connections')
conn,addr =server_socket.accept()
print(f'Now Connected to {addr[0]} whose on Port {addr[1]}')
msg=''
while True:
    if msg.lower()=='exit !':
        server_socket.close()
        break
    msg=input('Server: ')
    server_socket.send(msg.encode())
    print(server_socket.recv(1024).decode())
