from socket import *
import sys
import threading
from packet import packet
import math
import time
import os
import signal
# GBN protocol
WindowSize = 10
Timeout = 0.1
SeqNumSentNotAck = []
PacketSentNotAck = []

SeqNumSent = []
SeqNumAck = []
seq_num_log = open('seqnum.log', 'w')
ack_log = open('ack.log', 'w')

# read the source file byte by byte
def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    f.close()
    return buf

# check if has been full window
# if full every 0.1 seconds check one time, until return True
def check_if_can_send():
    if (len(SeqNumSentNotAck) < WindowSize):
        return True

    else:
        time.sleep(0.1)
        return check_if_can_send()



#timeout resend
def resend(s,f):

    # restart the timer
    signal.setitimer(signal.ITIMER_REAL, Timeout)
    for i in PacketSentNotAck:
        SeqNumSent.append(i.seq_num)
        seq_num_to_write = "{}{}".format(i.seq_num, '\n')
        seq_num_log.write(seq_num_to_write)

        SenderSendSocket.sendto(i.get_udp_data(), (EmulatorHostAddress, EmulatorPortNumRecFrSender))



def RdtSend(EmulatorHostAddress, EmulatorPortNumRecFrSender, FileNameToTrans):

    signal.signal(signal.SIGALRM, resend)

    #divide the data bytes array into packets, each with 500 bytes data
    FileByteBuffer = read_into_buffer(FileNameToTrans)
    Num_Of_Packets = int(math.ceil( len(FileByteBuffer) / 500))

    #send use UDP
    global SenderSendSocket
    SenderSendSocket = socket(AF_INET, SOCK_DGRAM)

    seq_num = 0
    for i in range(Num_Of_Packets):

        if ((i != (Num_Of_Packets - 1)) and check_if_can_send()):


            if (len(SeqNumSentNotAck) == 0):

                #start the timer when the window is empty and begin start sending packet
                signal.setitimer(signal.ITIMER_REAL, Timeout)

            # 500 bytes data for the packet data field
            message = FileByteBuffer[(i * 500) : ((i * 500) + 500)]
            Message_Packet = packet.create_packet(seq_num, message.decode())

            seq_num_to_write = "{}{}".format(Message_Packet.seq_num, '\n')
            seq_num_log.write(seq_num_to_write)

            SeqNumSentNotAck.append(Message_Packet.seq_num)
            PacketSentNotAck.append(Message_Packet)
            SeqNumSent.append(Message_Packet.seq_num)
            SenderSendSocket.sendto(Message_Packet.get_udp_data(), (EmulatorHostAddress, EmulatorPortNumRecFrSender))
            seq_num += 1

            continue
        else:
            #send the last packet data of the source file
            message = FileByteBuffer[(i * 500): len(FileByteBuffer)]
            Message_Packet = packet.create_packet(seq_num, message.decode())

            seq_num_to_write = "{}{}".format(Message_Packet.seq_num, '\n')
            seq_num_log.write(seq_num_to_write)

            SeqNumSentNotAck.append(Message_Packet.seq_num)
            PacketSentNotAck.append(Message_Packet)
            SeqNumSent.append(Message_Packet.seq_num)
            SenderSendSocket.sendto(Message_Packet.get_udp_data(), (EmulatorHostAddress, EmulatorPortNumRecFrSender))

    # every 0.1 seconds to check if the sender has transimit successfully and acked all the ack
    while (len(SeqNumSentNotAck) != 0):
        time.sleep(0.1)

    # send EOT
    seq_num += 1
    EOT_Packet = packet.create_eot(seq_num)
    SenderSendSocket.sendto(EOT_Packet.get_udp_data(), (EmulatorHostAddress, EmulatorPortNumRecFrSender))
    SeqNumSent.append(EOT_Packet.seq_num)

    # wait the sender receiving socket to close and the EOT will not lose in the internet so i choose 1 second
    # only receive the EOT ack from receiver, the sender can close the sending socket
    time.sleep(1)
    SenderSendSocket.close()



def GetAck(SenderPortNumRecAckFroE):

    # sender receive the ACK through AckRec Socket
    AckRecSocket = socket(AF_INET, SOCK_DGRAM)
    AckRecSocket.bind(('', SenderPortNumRecAckFroE))

    global SeqNumSentNotAck
    global PacketSentNotAck

    while True:
        udp_packet, EmulatorAddress = AckRecSocket.recvfrom(2048)
        packet_rec = packet.parse_udp_data(udp_packet)
        AckSeq = packet_rec.seq_num
        type = packet_rec.type

        #check if it is EOT, if not record the seq num
        if (type != 2):
            ack_num_to_write = "{}{}".format(AckSeq, '\n')
            ack_log.write(ack_num_to_write)
            SeqNumAck.append(AckSeq)

        # receive EOT
        if (type == 2):

            seq_num_log.close()
            ack_log.close()
            time.sleep(0.2)
            AckRecSocket.close()
            break

        # deal with duplicate ack and the first seq not equal to 0
        if (len(SeqNumSentNotAck) == 0 ) or (AckSeq not in SeqNumSentNotAck):
            continue

        # slide the window and restart the timer
        if(SeqNumSentNotAck.index(AckSeq) >= 0):

            if(AckSeq in SeqNumSentNotAck):
                index = SeqNumSentNotAck.index(AckSeq)
                SeqNumSentNotAck = SeqNumSentNotAck[(index+1) : ]
                PacketSentNotAck = PacketSentNotAck[(index+1) : ]

                if (len(SeqNumSentNotAck)) != 0:
                    signal.setitimer(signal.ITIMER_REAL, Timeout)

                else:
                    # if there are no packets in the window, stop the timer
                    signal.setitimer(signal.ITIMER_REAL, 0)

            else: continue

if __name__ == "__main__":

    time_start1 = time.time()

    EmulatorHostAddress = sys.argv[1]

    EmulatorPortNumRecFrSender = int(sys.argv[2])

    SenderPortNumRecAckFroE = int(sys.argv[3])

    FileNameToTrans = sys.argv[4]


    # start the receive ack thread
    thread = threading.Thread(target=GetAck, name='RecAckThread',args = (SenderPortNumRecAckFroE,))
    thread.start()

    RdtSend(EmulatorHostAddress, EmulatorPortNumRecFrSender, FileNameToTrans)

    time_end1 = time.time()
    # get the sender's execution time
    sender_time =  time_end1 - time_start1

    # append the execution time to the time_log.txt
    time_log = open('time.log', 'a')
    time_log_to_write = "{}{}".format(sender_time, '\n')
    time_log.write(time_log_to_write)
    time_log.close()
    exit(0)

