from socket import *
import sys
import pickle

def client_socekt(server_address, n_port, req_code, message):

    #create client_log txt file to record
    f = open('client_log.txt', 'a+')

    #create the client socket
    client_TCP_Socket = socket(AF_INET, SOCK_STREAM)

    try:
        #clent socket connect to the server
        client_TCP_Socket.connect((server_address, n_port))
    except:
        sys.stderr.write('Error server_unavailable\n')
        save_error = sys.stderr
        sys.stderr = f
        raise Exception, 'Error server_unavailable\n'
    else:
        #send req_code to initiate the negotiation to get r_port
        client_TCP_Socket.send(req_code.encode())

        r_port = client_TCP_Socket.recv(1024)

        if (r_port == '0'):
            client_TCP_Socket.close()
            sys.stderr.write('invalid req_code\n')
            save_error = sys.stderr
            sys.stderr = f
            raise Exception, 'invalid req_code\n'



        else:
            client_TCP_Socket.close()

            #create the UDP socket for transaction phase communication
            client_UDP_Socket = socket(AF_INET, SOCK_DGRAM)

            #print("message: ",message)
            client_UDP_Socket.sendto(message.encode(), (server_address, int(r_port)))

            # get the message_buffer from server
            message_buffer_received, serverAddress_UDP = client_UDP_Socket.recvfrom(2048)

            message_buffer = pickle.loads(message_buffer_received)
            if(len(message_buffer) == 0):
                print('NO MSG')
                str_to_write = "{}{} {}{}".format('r_port', ':', r_port, '\n')
                f.write(str_to_write)
                #f.write('r_port: %d\n', r_port)
                f.write('NO MSG\n\n')
            else:
                f.write('\n')
                str_to_write = "{}{} {}{}".format('r_port', ':', r_port, '\n')
                f.write(str_to_write)
                for i in message_buffer:
                    print(i)
                    f.write(i)
                    f.write('\n')

                print('NO MSG')
                f.write('NO MSG\n\n')

        f.close()



if __name__ == "__main__":

    server_address = sys.argv[1]
   
    n_port = int(sys.argv[2])
    
    req_code = sys.argv[3]
    
    message = sys.argv[4]
    
    client_socekt(server_address, n_port, req_code, message)
    print("please Enter exit to quit: ")
    str = input()

    exit(0)

