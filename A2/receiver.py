from socket import *
import sys
import threading
from packet import packet
import math
import time

arrival_log = open('arrival.log', 'w')
rec_seq_num = []
SEQ_NUM_MODULO = 32


def RecSendAck(EmulatorHostName, EmulatorPortNumAckFrRec, RecPortNumRecDataFroE, FileNameToWriteData):

    receiverSocket = socket(AF_INET, SOCK_DGRAM)
    receiverSocket.bind(('', RecPortNumRecDataFroE))

    while True:
        packet_rec_udp, clientAddress = receiverSocket.recvfrom(2048)

        # parse the recieved packet
        packet_rec = packet.parse_udp_data(packet_rec_udp)

        seq_num_rec = packet_rec.seq_num

        # if the packet is not EOT, record in the arrival log
        if (packet_rec.type != 2):
            arrival_to_write = "{}{}".format(seq_num_rec, '\n')
            arrival_log.write(arrival_to_write)

        # deal with the first packet's seq num is not the seq num = 0 situation
        if (len(rec_seq_num) == 0 and seq_num_rec != 0):
            continue

        # receive the first expected packet
        if (len(rec_seq_num) == 0):
            rec_seq_num.append(seq_num_rec)
            Ack_packet = packet.create_ack(seq_num_rec)
            f.write(packet_rec.data)

            receiverSocket.sendto(Ack_packet.get_udp_data(), (EmulatorHostName, EmulatorPortNumAckFrRec))
            continue

        #receive the EOT packet
        if ((packet_rec.type == 2)):
            EOT_packet = packet.create_eot(seq_num_rec)
            receiverSocket.sendto(EOT_packet.get_udp_data(), (EmulatorHostName, EmulatorPortNumAckFrRec))
            arrival_log.close()
            receiverSocket.close()
            f.close()
            break


        #not receive the expected packet
        if (seq_num_rec != (((rec_seq_num[len(rec_seq_num) - 1] + 1) % SEQ_NUM_MODULO))):
            Ack_packet = packet.create_ack(rec_seq_num[len(rec_seq_num) - 1])
            receiverSocket.sendto(Ack_packet.get_udp_data(), (EmulatorHostName, EmulatorPortNumAckFrRec))
            continue

        #receive the expected packet
        if (seq_num_rec == (((rec_seq_num[len(rec_seq_num) - 1] + 1) % SEQ_NUM_MODULO))):
            rec_seq_num.append(seq_num_rec)
            Ack_packet = packet.create_ack(seq_num_rec)
            f.write(packet_rec.data)
            receiverSocket.sendto(Ack_packet.get_udp_data(), (EmulatorHostName, EmulatorPortNumAckFrRec))
            continue

if __name__ == "__main__":

    EmulatorHostName = sys.argv[1]

    EmulatorPortNumAckFrRec = int(sys.argv[2])

    RecPortNumRecDataFroE = int(sys.argv[3])

    FileNameToWriteData = sys.argv[4]

    f = open(FileNameToWriteData, 'w')

    RecSendAck(EmulatorHostName, EmulatorPortNumAckFrRec, RecPortNumRecDataFroE, FileNameToWriteData)
    exit(0)
