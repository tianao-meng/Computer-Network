In my experiment, the nEmulator program runs on ubuntu1804-002, while the receiver program runs on ubuntu1804 – 004 and the sender program runs on unbuntu1804 – 008.

1. You need to run the nEmulator firstly, then run the receiver program, at last run the sender program to send the source file.

2. To run the receiver program, you need know the host name of the nEmulator, nEmulator's port to receive ack, receiver's port to receive data, name of the file to write data in.

In my experiment, the host name of the nEmulator is ubuntu1804 - 002. You can use the command provided in the A2_FAQ file to get the free port number on the machines where run nEmulator and receiver program. The name of the file is defined by yourself, which is the destination file name

The template to run the receiver.sh is:
./receiver.sh <host name of the emulator> <nEmulator's port to receive ack> <receiver's port to receive data> <the name of the file to write in>

3.To run the sender program, you need know the host address of the nEmulator, nEmulator's port to receive data, sender's port to receive ack, source file name.

In my experiment, the host address of the nEmulator is 10.1.154.34. You can use the command provided in the A2_FAQ file to get the free port number on the machines where run nEmulator and sender program. The name of the file is based on the file path you want to test my code

The template to run the receiver.sh is:
./sender.sh <host address of the emulator> <nEmulator's port to receive data> <sender's port to receive ack> <source file name>


4. I use python3 for this assignment.
5. The sender program will generate the seqnum.log, ack.log and time.log files
6. The receiver program will generate the arrival.log file.
7. Because I import the packet.py, so it need to be at the same path with my program.


