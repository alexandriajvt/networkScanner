import nmap
import os



def networkScanner(address):
        network = address
        nm=nmap.PortScanner()  #create a port scanner object
        nm.scan(hosts=network,arguments='-sn')#hosts=each ip adress in the network
        hostList=[(x, nm[x] ['status']['state'], nm[x]['vendor'])for x in nm.all_hosts()] #go through all the hosts found and create a list of them called hostList 
        f = open("devices.txt" , "r+")
        f.truncate(0)#clears file once we've gotten the ip adress info we need
        f.close()
        g=open("specifics.txt","r+")
        g.truncate(0)
        g.close
        with open("devices.txt","w")as file1, open("specifics.txt","w")as file2:
            for host, status,vendor in hostList:#print Host followed by each host/ip address
                file1.write("Host\t{0}\tStatus: {1}\tManufacturer: {2}\n".format(host,status,vendor))
                #file2.write("Host\t{}\n".format(host))
                file2.write("{0}\n".format(host))
        
        if(os.path.getsize("devices.txt")==0):
             f=open("devices.txt","w")
             f.write("No Hosts Found")

#networkScanner('192.168.1.0/24')