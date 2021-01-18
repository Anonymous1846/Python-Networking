import threading
import socket
import colorama
from colorama import Style as s
from colorama import Fore as f
colorama.init(convert=True)
class Server:
    def __init__(self):
        #the port number and non-hardcoded host-address/name
        self.HOST=socket.gethostbyname(socket.gethostname())
        self.PORT=23560
        #initializing the empty lists 
        self.clients=[]
        self.usernames=[]
        #A Simple TCP Socket with IPv4 Address Family 
        self.server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(f.GREEN+f'Binding the IP address {self.HOST} and the Port Number {self.PORT}'+f.RESET)
        self.server_socket.bind((self.HOST, self.PORT))
        print(s.BRIGHT+f.BLUE+'The Server can now Listen Up 100 Clients'+f.RESET)
        self.server_socket.listen(100)
    #the method for broadcasting the message to the clients in the clients list 
    def broadcast_msg(self,message):
        for client in self.clients:
            client.send(message)
    def handle_clients(self,client):
        while True:
            try:
                #message from one client will be broadcasted to another clients on the networks !
                message_from_client=client.recv(1024)
                
                self.broadcast_msg(message_from_client)
            except:
                #this will handle the exception if any client abruptly interfere in the connection or disconnect !
                the_index_of_faulty_client = int(self.clients.index(client))
                #first of all we obtain the index/position of the client in the client list !!
                #then we remove the client from the client list !
                self.clients.remove(client)
                #then we close the connection between the current client and the server !
                client.close()
                #after removing the client connection object we remove the corresponding username of the client 
                username_to_be_removed=self.usernames[the_index_of_faulty_client]
                #and broadcast it to the rest of the clients
                prompt=f'{username_to_be_removed} has left the chat.'
                print(prompt)
                self.broadcast_msg(prompt.encode())
                self.usernames.remove(username_to_be_removed)
                #removing the same from the corresponding username list !
                break

    #this method will continue to accept the connections as long as the connection is in intact !
    def recieve_conn(self):
        while True:
            #accepting the client connections
            client_conn,addr=self.server_socket.accept()
            print(f'{addr[0]} Connected to the Server, which is on Port {self.PORT}')
            #the server is sending a request for the client to input or send his/her username
            client_conn.send('Username:'.encode())
            username=client_conn.recv(1024).decode()
            #appending the clients to the connection list and their corresponding username list !
           
         
            self.usernames.append(username)
            self.clients.append(client_conn)
            #prinitng the currently active clients by printing out the client list !
            print(f'Currently Active Users: {self.usernames}')
            print(f'{username} has now joined the chat.')
            self.broadcast_msg(f'{username} has now joined the chat.'.encode())
            client_conn.send('You\'re Now Connected To The Server.'.encode())
          
            #the multi threaded  client -server architecture 
            the_client_handle_thread = threading.Thread(target=self.handle_clients,args=(client_conn,))
            the_client_handle_thread.start()  

#the server object initialised and recieve method invoked !
server=Server()
server.recieve_conn()
        
