import socket
import os
import tkinter as tk
import time 
from tkinter import Label,Entry,Button

class Client:
    def initiate_conn(self):
        print(f'The target IP is {self.HOST}.')
        self.client_socket.connect((self.HOST, self.PORT))
    def logCheck(self,event):
        if self.username.get()=='admin':
            self.initiate_conn()
            #used to Withdraw the window without terminating the program !
            self.root.withdraw()
        else:
            self.warning.config(text='Invalid Username.')
    def _exit(self,event):
        exit(0)
    def __init__(self):
        self.root=tk.Tk()
        self.root.title('Client')
        self.root.geometry('300x250')
        self.HOST='127.0.0.1'
        self.PORT=49990
        #defining a TCP socket !
        self.client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #Label().place function we can place the label at the absolute x,y coordinates 
        self.login=Button(self.root, text="Enter", bg="#e07000", fg="white")
        self.exit=Button(self.root, text="Exit", bg="#748c3e", fg="white")
        self.login.bind('<Button>',self.logCheck)
        self.exit.bind('<Button>',self._exit)
        self.exit.place(x=50, y=200)
        self.login.place(x=200, y=200)
        Label(self.root, text="Username:",fg="black").place(x=25, y=75)         
        self.username=Entry(self.root,)
        self.warning=Label(self.root,text='',fg='red')
        self.warning.place(x=50,y=150)
        self.username.place(x=100, y=75)
        self.root.mainloop()
   
if __name__ == '__main__':
    client=Client()

