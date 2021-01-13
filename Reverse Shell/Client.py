#the Client program for the demonstration of Reverse Shell
import socket
try:
	soc=socket.socket()
	soc.connect(('127.0.0.1',9100))
	soc.send(b'hey bitch !')
except socket.error as s_r:
	print('The socket ha met with some error :',str(s_r))
