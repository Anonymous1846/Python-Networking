'''The server class provides the medium to broadcast the message to all the clients in the
Clients list
Using the following prgm clients can connect to the Server via IP address and Port Number Combinaton
We can send textual messages, text files ,and non-textual files via the prgm client
Smiley Support inculded'''
import socket
import threading

class Server:
    def __init__(self):
        self.PORT=32500
        #avoiding hardcoded hostnames(The IP V4 address will be stored in the host variable !)
        self.HOST=socket.gethostbyname(socket.gethostname())
        #initializing the socket object (TCP)
        #IPV4 family and the TCP protocol are the paramters
        self.server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #initializing the empty lists for client connections and their corresponding usernames 
        self.clients=[]
        self.usernames=[]
    #the method for initializing the connection !
    def initialize(self):
        print(f'Binding the IP address {self.HOST} and the Port {self.PORT}')
        self.server_socket.bind((self.HOST, self.PORT))
        print('Listening to the Clients.........')
        self.server_socket.listen()
    def handle_clients(self,client):
        while True:
            try:
                #fetching the message from one client and broadcasting to other clients 
                message=client.recv(1024)
                self.send_broadcast(message)
            except:
                f_client=self.clients.index(client)
                self.clients.remove(f_client)
                username=self.usernames[f_client]
                print(f'{username} has left the Chat.')
                self.send_broadcast(f'{username} has left the Chat.'.encode())
                self.usernames.remove(username)
                break
    def recieve(self):
        while True:
            #constantly accepting connections from the Clients !
            client_conn,address=self.server_socket.accept()
            print(f'[{address[0]} connected to Server, which is binded to Port [{address[1]}]')
            client_conn.send('Username:'.encode())
            username=client_conn.recv(1024).decode()
            #appending the client connection object and the usernames !
            self.usernames.append(username)
            self.clients.append(client_conn)
            print(f'{address} has Choosen the Username: {username}')
            self.send_broadcast(f'{username} has joined the chat !')
            client_conn.send('You\'re now Connected to the Chat Room !'.encode())
            #starting a thread for each new client !
            thread=threading.Thread(target=self.handle_clients,args=(client_conn,))
            thread.start()
    #this is used to send the broadcast message to all the connected clients !
    def send_broadcast(self,message):
        for client in self.clients:
            client.send(message.encode())
server=Server()
server.initialize()
server.recieve()
        
        


