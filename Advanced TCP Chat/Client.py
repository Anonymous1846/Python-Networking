import socket
import threading
class Client:
    def __init__(self):
        #the port number and non-hardcoded host-address/name
        self.HOST=socket.gethostbyname(socket.gethostname())
        self.PORT=23512
        
        #tcp socket 
        self.client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((self.HOST, self.PORT))
        self.username=input('Please Enter Your Username: ')
    #the two methods will run on different threads
    def recieve_msg(self):
        while True:
            message=self.client_socket.recv(1024).decode()
            if message=='Username:':
                self.client_socket.send(self.username.encode())
            else:
                print(message)
           
                
    def send_msg(self):
        while True:
            message=f'{self.username}: {input(">>")}'
            if message.replace(self.username+': ','').lower()=='exit':
                print('Are you sure you want to exit ?(y/n)')
                ans=input('>>')
                if ans=='y':
                    print('Exiting the chat room.............')
                    self.client_socket.close()
                else:
                    continue
            self.client_socket.send(message.encode())

client =Client()
r_thread=threading.Thread(target=client.recieve_msg)
r_thread.start()
s_thread=threading.Thread(target=client.send_msg)
s_thread.start()
        
        