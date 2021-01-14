#the Client program for the demonstration of Reverse Shell
import socket
try:
	soc=socket.socket()
	soc.connect(('127.0.0.1',9100))
	print('Ready to Chat !')
	cmd=''
	while True:
		if cmd.lower()=='quit':
			soc.close()
			print('Bye Server !')
			break
		print('Server: ',soc.recv(1024).decode())
		cmd=input('>>')
		print('Client: ',cmd)
		soc.send(cmd.encode())
except socket.error as s_r:
	print('The socket ha met with some error :',str(s_r))
