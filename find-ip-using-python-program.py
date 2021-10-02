'''
#   First methord:
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
print(s.getsockname()[0])
'''


#-------------------------------------------------------------------------------------------------------
# Second Methord: run using python3 to get ip address 

'''
from netifaces import interfaces, ifaddresses, AF_INET
for ifaceName in interfaces():
	addresses = [i['addr']
	for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
	print(' '.join(addresses))
''' 
#--------------------------------------------------------------------------------------------------------
  #third Methord
## importing socket module
import socket
## getting the hostname by socket.gethostname() method
hostname = socket.gethostname()
print(type(hostname))
## getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)
## printing the hostname and ip_address
print("Hostname: " +hostname )
print("IP Address: {}" .format(ip_address))

