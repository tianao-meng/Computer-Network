from socket import *
import random
import sys
import pickle

def server_socekt(req_code):

    #create the welcome socket
    server_TCP_socket = socket(AF_INET,SOCK_STREAM)


    # get free port from os
    server_TCP_socket.bind(('', 0))
    
    n_port = server_TCP_socket.getsockname()[1]
    str_to_write = "{}{} {}{}".format('SERVER_PORT', ':', n_port, '\n')

    #create server_log txt file to record
    f = open('server_log.txt', 'a+')
    f.write(str_to_write)
    f.close()


    #sever begins listening for incoming TCP requests
    server_TCP_socket.listen(5)
    print("Welcome socket is ready")

    message_buffer = []

    while True:
        #get the req_code from the client through TCP connection
        connection_TCP_Socket, addr = server_TCP_socket.accept()

        req_code_received = connection_TCP_Socket.recv(1024).decode()

        #check if the req_code is valid
        if(req_code_received == req_code):
            
            #transaction phase
            server_UDP_Socket = socket(AF_INET, SOCK_DGRAM)
            server_UDP_Socket.bind(('', 0))
            
            r_port = server_UDP_Socket.getsockname()[1]
            r_port = str(r_port)
            
            connection_TCP_Socket.send(r_port.encode())
            connection_TCP_Socket.close()


            message, clientAddress = server_UDP_Socket.recvfrom(2048)
            buffer_to_send = pickle.dumps(message_buffer)

            if message != 'TERMINATE':
                if (message == 'GET'):
                    if (len(message_buffer) == 0):
                        server_UDP_Socket.sendto(buffer_to_send, clientAddress)
                        continue
                    server_UDP_Socket.sendto(buffer_to_send, clientAddress)
                    continue

                server_UDP_Socket.sendto(buffer_to_send, clientAddress)

                str_to_append = "{}{} {}".format(r_port,':',message)
                message_buffer.append(str_to_append)
                continue


            else:
                server_UDP_Socket.sendto(buffer_to_send, clientAddress)
                connection_TCP_Socket.close()
                server_TCP_socket.close()
                break

        else:
            r_port = '0' # invalid situation
            connection_TCP_Socket.send(r_port.encode())
            connection_TCP_Socket.close()


if __name__ == "__main__":

    server_socekt(sys.argv[1])
