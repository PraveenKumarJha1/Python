import socket

def main():
    hacker_socket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    IP="192.168.0.97"
    Port=8008

    socket_address=(IP, Port)
    hacker_socket.bind(socket_address)
    hacker_socket.listen(5)
    print("listening for incomming")


    hacker_socket, client_address = hacker_socket.accept()
    message="hacker is here "

    message_bytes = message.encode()
    hacker_socket.send(message_bytes)
    print("Message send from hacker")
    

    hacker_socket.close()


if __name__ =="__main__":
    main()