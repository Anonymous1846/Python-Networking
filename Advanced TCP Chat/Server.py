import socket
import os
import tkinter as tk
import time 
from tkinter import Label,Entry,Button
import threading
class Server:
    def initiate_conn(self):
        print(f'Binding the IP: {self.HOST} with the PORT {self.PORT}')
        self.server_socket.bind((self.HOST, self.PORT))
        print('Listening to Connections')
        self.server_socket.listen()
        print('ADMIN is Waiting for Someone to Connect.....')
        #broadcasting the message to other clients !
    def send_broadcast(self,message):
        for client in self.client_list:
            client.send(message)
    def handle_clients(self,client):
        #the function for handling the clients
        while True:
            try:
                message=client.recv(1024)
                client.send(message)
            except:
                #manipulating the list of clients and thier nicknames
                #we obtain the index of the faulty connection username 
                faulty_client=self.client_list.index(client)
                #remove from the list of clients based on the index 
                self.client_list.remove(faulty_client)
                #closing the client connection
                client.close()
                #also using the same index remove the username from the username list!
                faulty_username=self.username[faulty_client]
                self.usernames.remove(faulty_username)
                #breaking the loop 
                break
    def recieve(self):
        #accepting the conncetion from the client !
        connection,address=self.server_socket.accept()
        print(f'Connceted to {address[0]} which is on Port {address[1]}')
        connection.send('USERNAME'.encode('utf-8'))
        username_of_client=connection.recv(1024).decode('utf-8')
        self.client_list.append(connection)
        self.usernames.append(username_of_client)
        print(f'The Client {address} has choosen {username_of_client}')
        self.send_broadcast(f'{username_of_client} has joined the chat.')
        connection.send('You\'re Now Connected to Server'.encode('utf-8'))
        new_thread=threading.Thread(target=self.handle_clients,args=(connection,))
        new_thread.start()
    def logCheck(self,event):
        if self.username.get()=='admin':
            self.initiate_conn()
            self.recieve()
            #used to Withdraw the window without terminating the program !
            self.root.withdraw()
        else:
            self.warning.config(text='Invalid Username.')
    def _exit(self,event):
        exit(0)
    def __init__(self):
        #the body of the tkinter window !
        self.root=tk.Tk()
        #the title 
        self.root.title('Server')
        #the diemensions
        self.root.geometry('300x250')
        #the ip address and the port number !
        self.HOST='127.0.0.1'
        self.PORT=49990
        #the list of clients and their corresponding nicknames
        self.usernames=[]
        self.client_list=[]
        #defining a TCP socket !
        self.server_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Label().place function we can place the label at the absolute x,y coordinates 
        #the login button the exit button placed at absolute x and y positions 
        self.login=Button(self.root, text="Enter", bg="#e07000", fg="white")
        self.exit=Button(self.root, text="Exit", bg="#748c3e", fg="white")
        #binding the buttons with exit and log functions with single click 
        self.login.bind('<Button>',self.logCheck)
        self.exit.bind('<Button>',self._exit)
        self.exit.place(x=50, y=200)
        self.login.place(x=200, y=200)
        #label for username prompt
        Label(self.root, text="Username:",fg="black").place(x=25, y=75)         
        self.username=Entry(self.root,)
        #warning set to null, triggered when the username is wrong !
        self.warning=Label(self.root,text='',fg='red')
        self.warning.place(x=50,y=150)
        self.username.place(x=100, y=75)
        self.root.mainloop()
   
if __name__ == '__main__':
    server=Server()

