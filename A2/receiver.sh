#!/bin/bash


#Parameter:
#    $1: <hostname for the network emulator>
#    $2: <UDP port number used by the emulator to receive ACKs from the receiver>
#    $3: <UDP port number used by the receiver to receive data from the emulator>
#    $4: <name of the file into which the received data is written>



#For Python implementation
python3 receiver.py $1 $2 $3 "$4"
