import socket
import threading
from SpecialChar import SpecialChar as sp
#initializing the client objects lists and the corresponding username lists !
clients=[]
usernames=[]
#avoiding hardcoded ip addresses
HOST=socket.gethostbyname(socket.gethostname())
PORT=45000
#creating a tcp server to bind the Ip address and the Port 
server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print(sp.Green+f'Binding {HOST} to the Port {PORT}'+sp.Reset)
server_socket.bind((HOST,PORT))
print('The Server is now Listening for Connections.')
server_socket.listen()
#this method is used to broadcast the message to the rest of the clients connected to the server 
def broadcast_msg(message):
    for client in clients:
        client.send(message.encode())
def handle(client):
    while 1:
        try:
        #if some error occur in the network we remove the client from the client list and also from the nickname list !'
            message=client.recv(1024)
            broadcast_msg(message)
        except:
            index_of_client=clients.index(client)
            clients.remove(client)
            username=usernames[index_of_client]
            print(f'{username} has left the chat....')
            usernames.remove(username)
            break            
def recieve_conn():
    while 1:
        #now we have to accept the connections from the clients !
        client_conn,address=server_socket.accept()
        print(f'{address[0]} is now connected to the network, which is on port: {address[1]}')
        client_conn.send('USERNAME:'.encode())
        username=client_conn.recv(1024).decode()
        #the clients connection object added to the clients list and the username added to the usernames list !
        clients.append(client_conn)
        usernames.append(username)
        print(f'{username} has now joined the chat.')
        broadcast_msg(f'{username} has now joined the chat.')
        client_conn.send('You\'re Now Connected to the Server.'.encode())

        thread_for_handling=threading.Thread(target=handle,args=(client_conn,))
        thread_for_handling.start()

recieve_conn()