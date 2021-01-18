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
try:
    import pyfiglet
    #if not found on the computer it will downlod the module by using the command pip install pyfiglet
except Exception as e:
    print('The Module is not found on Your System.......')
    print('Installing pyfiglet')
    subprocess.run('pip install pyfiglet')
    print('Installation Finished......!\nNow you can run your python script in the format python Port Scanner.py <ip-address> <starting range> <ending-range>')
    exit(0)
    #for system command line arguements !
import sys
class color:
   #ansii escape sequences for python print statements !
   #non-bold statements !
   NORMAL='\033[0m'
   BOLD = '\033[1m'
   #color for text !
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   WHITE ='\u001b[37m'
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
        print(f'The Time Taken for The Scan is {round(time.time()-start_time,3)} Seconds...')
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
            print(color.BLUE+f'Port: {port}'+color.GREEN+' is Open.'+color.WHITE)
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
        print(color.BOLD+'Version 1.101'+color.NORMAL)
        print('-'*200)
        #the time at starting of the scan!
        starting_time=time.time()
        print(f'Scanning the IP address: {addr},Port range from {port_start} to {port_end}')
        # we will iterate from starting port to ending port+1(ending port is exclusive ) !
        with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executer:
            for i in range(port_start,port_end+1):
                #passing the fucntion aguements ip address and the port number in this case, from sys agrv[2] to sys.args[3]
                executer.submit(scan_me,addr,i)
            #the ports which are open will be displayed !
        
        print(color.GREEN+f'Scanning IP {addr} finished....{len(open_ports)} Open Ports !'+color.WHITE+f'Total taken: {round(time.time()-starting_time,2)} Seconds.')
    else:
        #ansii character escape for Red color and back to normal !
        print('Correct usage of '+color.BOLD+color.RED+'Command is python Port Scanner.py <ip-address> <starting-port> <ending-port>'+color.NORMAL+color.WHITE)
        print('Exiting Program.......')
        exit(0)

port_scan()

