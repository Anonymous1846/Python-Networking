import socket
import threading

#avoiding hardcoded ip addresses
HOST=socket.gethostbyname(socket.gethostname())
PORT=45000
#the username inputted by the user 
username=input('Please Enter The Username: ')
#creating a tcp server to bind the Ip address and the Port 
client_socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST,PORT))
print(f'Connected to {HOST} {PORT}')

def send_msg():
    while 1:
        message=f'{username}: {input(">>")}'
        client_socket.send(message)
def get_msg():
    while 1:
        try:
            #get the message from the server broadcast
            message=client_socket.recv(1024).decode()
            if message=='USERNAME:':
                client_socket.send(username.encode())
            else:
                print(message)
        except:
            print('Exiting the Connections')
            client_socket.close()
            break
#seperate threads for writing and sending messages to and from the server and the client 
get_thread = threading.Thread(target=get_msg)
get_thread.start()
send_thread = threading.Thread(target=send_msg)
send_thread.start()
