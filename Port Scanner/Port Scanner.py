#The following python script is used to scan for open ports of an IP Address.
#The program takes the IP address, starting port number and the ending port number as the command line arguements.
#the time module is required for calculating teh time of execution/scanning
import time
#the socket module/library is the main module of the program since we need to establish a connection with the remote device
import socket
#Since we are using the module pyfiglet, we need to install the module if not found on the machine !
# Inorder to reduce the hassle of installation the program will chack for the module, whether it is installed or not(if not it will install via subprocesses.run method) 
import subprocess 
#use the Threadpool Executer to run the scan faster !
import concurrent.futures
#thread lock, so that multiple threads cannot access the same resources
import threading
#for ascii art
import pyfiglet
import sys
#initializing the colorama
import colorama
colorama.init(convert=True)

#Thread lock for avoiding multiple threads to crumple the data(output )
print_lock=threading.Lock()
#The list will hold the open ports
open_ports=[]
#the function which will scan the individual ports !
#the function will scan an IP address and a Port at a given time !(If the port is open then it is added to the open ports list !)

#the timer function will be used as a decorator for the port scan function
def timer(func):
    #the wrapper function will take optional arguements/key word args
    def _timer(*args,**kwargs):
        #calculating the start time in secs
        start_time=time.time()
        #returns something if is bound to return 
        return_value=func(*args,**kwargs)
        print(colorama.Fore.GREEN+f'The Time Taken for The Scan is {round(time.time()-start_time,3)} Seconds...'+colorama.Fore.WHITE)
        return return_value
        #returning just the function object and not the call to the function !
    return _timer
def scan_me(addr,port):
    #creating the socket object !
    connection_socket=socket.socket(socket.AF_INET)
    #the Connect_ex return a zero for a successful connection, otherwise returns err_no variable !
    result=connection_socket.connect_ex((addr,port))==0
    if result:
        #print lock enabled to current object, so that is not used by other threads !
        with print_lock:
            open_ports.append(port) 
            print(colorama.Fore.BLUE+f'Port: {port} is Open.'+colorama.Fore.WHITE)
#the decorator timer for calculating the time taken for scanning !
@timer
def port_scan():
    if len(sys.argv)>3:
        # first of all we check if the command line arguements are given in correct number ie 3 First is the Program name, second is the ip address, third and foruth are the 
        #starting and ending indexes !
        #the ip address (eg:121.0.0.78)
        addr=sys.argv[1]
        #the starting port (eg:0-65535)
        port_start=int(sys.argv[2])
        #the ending port !
        port_end=int(sys.argv[3])
        #ascci art for The Heading!
        heading=pyfiglet.figlet_format('Whose Port')
        print(heading)
        print(colorama.Fore.CYAN+'Version 1.101'+colorama.Fore.WHITE)
        print('-'*200)
        #the time at starting of the scan!
        
        print(f'Scanning the IP address: {addr},Port range from {port_start} to {port_end}')
        # we will iterate from starting port to ending port+1(ending port is exclusive ) !
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executer:
            for i in range(port_start,port_end+1):
                #passing the fucntion aguements ip address and the port number in this case, from sys agrv[2] to sys.args[3]
                executer.submit(scan_me,addr,i)
            #the ports which are open will be displayed !
        print(colorama.Fore.GREEN+f'Scanning IP {addr} finished....{len(open_ports)} Open Ports !'+colorama.Fore.WHITE)
           
        
    else:
        #ansii character escape for Red color and back to normal !
        print('Correct usage of '+colorama.Fore.RED+'Command is python Port Scanner.py <ip-address> <starting-port> <ending-port>'+colorama.Fore.WHITE)
        print('Exiting Program.......')
        exit(0)

port_scan()

