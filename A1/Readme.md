1. Firstly, run the server.sh, like ./server.sh <req_code>. After running server file, you can run client.sh, e.g. ./client.sh <server_address> <n_port> <req_code> message. The <n_port> you can get from the client_log.txt. Remember that every time you rerun the server, the n_port is different because the free n_port is assigned by OS.

If you run a wrong IP or n_port, you will get an Error server_unavailable error.
If you run client with a wrong req_code, you will get invalid req_code

Remember to enter exit to quit after each iteration of running my client file

2. I run the server.sh on ubuntu1804-002 with ip: 10.1.154.34, and the two clients are on ubuntu1804-004 with ip 10.1.154.27, and ubuntu1804-008 with ip 10.1.152.47, to run the scenario given in the A1 document.

3. I use python3 for this assignment.

4. I will not submit the log.txt file for client and server. When you run my code, they will be created, and if you do not remove the log file, they will keep appending the relevant message received from client or server. I also write the the mentioned error in the client_log.txt.

