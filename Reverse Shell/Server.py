#The Demo of the Server Program.
#We Initiate TCP Connection via the Server.py prgm
#The Following module is required to use the TCP facility !
import socket
import os
import sys

HOST=''
# we have the option to choose from 0-65535(0-1023 are reserved !)
PORT=43000
try:
	#initializing the socket object !
	print('Socket Object Initialized !')
	server_socket=socket.socket()
	#now we need to bind the ip address to the PORT Number !
	#it takes a single arguement that is the tuple containing the ip and port !
	print('Binding the port to the IP address.')
	server_socket.bind((HOST,PORT))
	#at most 3 devices can wait until the network timeout !
	print(f'Listening on Port {PORT}')
	server_socket.listen(3)
	print('Connection To Be Initiated !')
	#when an actual Client Connects to the Network !
	conn,addr=server_socket.accept()
	print(f'The Server is now Connected to {addr[0]}, which is at {addr[1]}')
	#now we can continously chat until the we enter the quit statement !
	#the Command will take the input from the server side keyboard !
	command=''
	while True:
		if command=='exit':
			conn.close()
			server_socket.close()
			sys.exit()
		if len(command.encode())>0:
			#sending Actual Commands to the Client !
			conn.send(command.encode())
			print(conn.recv.decode(),end='')

except Exception as e:
	print('Fatal Error Occured :',str(e))
