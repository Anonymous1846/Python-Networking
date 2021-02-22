import socket
import threading
#color used for ansi escape seqeunce !
import colorama
from colorama import Style as s
from colorama import Fore as f
colorama.init(convert=True)
class Client:
    def __init__(self):
        #the port number and non-hardcoded host-address/name
        self.HOST=socket.gethostbyname(socket.gethostname())
        self.PORT=23561
        
        #tcp socket 
        self.client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.username=input('Please Enter Your Username: ')
    #the two methods will run on different threads
    def recieve_msg(self):
        #the client will indefinetely recieve messages from the sever broadcast !
        while True:
            try:
                #the username sending and recieving procedure 
                #we have to first check whether the server has send the broadcast to listuser, so that we can skip that part 
                message=self.client_socket.recv(1024).decode()
                if message=='Username:':
                    self.client_socket.send(self.username.encode())
                else:
                    print(message)
            except:
                print('Connection has been broken')
                self.client_socket.close()
                break
           
                
    def send_msg(self):
        #the user can send the messages as long the user is connected to the chat room aka sthe Server 
        while True:
            #the message will be sent in the form of username : Message  
            message=f'{self.username}: {input(">>")}'
            #sending the request to show the list of currently logged in users to the chat bot private msg to one client only !
            if message.replace(self.username+': ','').lower()=='listusers':
                #removing the name of the client and showing only the listusers command !
                self.client_socket.send(message.replace(self.username+': ','').lower().encode())   
                continue
            if message.replace(self.username+': ','').lower().startswith('->'):
                self.client_socket.send((message[message.rindex('->'):]).encode())   
                
            #if the user sends a exit request then he opt out of the chat room if he presses the y button otherwise he can continue !
            if message.replace(self.username+': ','').lower()=='exit':
                print('Are you sure you want to exit ?(y/n)')
               
                ans=input('>>')
                if ans=='y':
                    print('Exiting the chat room.............')
                    self.client_socket.close()
                    break
                else:
                    continue
            
            self.client_socket.send(message.encode())

client =Client()
r_thread=threading.Thread(target=client.recieve_msg)
r_thread.start()
s_thread=threading.Thread(target=client.send_msg)
s_thread.start()
        
        
