import socket
import threading
from threading import Lock

threadList = []
open_ports={}

print_lock = Lock()

def check_ports(ip, port, open_ports):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(.001)
    result = sock.connect_ex((ip, port))#giving error because the ip from the checkboxes is not being passed properly

    if result == 0:
        open_ports[port]= ip # swap


def scanningPorts(host_ip):   #prints open ports
    local_threads=[]#test
    for port in range(1,1025):#creates 1025 threads and stores them in threadList
        thread = threading.Thread(target = check_ports, args=(host_ip, port, open_ports))#each thread will call the check ports function
        local_threads.append(thread)#test
        threadList.append(thread)

    for thread in local_threads:
        thread.start()
    

    for i in range(0,1024):#makes sure all the threads finih executing before the program continues
        threadList[i].join()

def printResults():
    printer = open("openPorts.txt","w")
    for key,value in open_ports.items():
            printer.write("Port Number: " + str(key) + " is Open on Device " + str(value)+"\n")


#startTime = datetime.now()
#endTime = datetime.now()
#scanningPorts('192.168.1.24',.001)
#print("Program took: {} ".format(endTime-startTime))
