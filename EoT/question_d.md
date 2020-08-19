From the given figure, fistly we can see that h0, h1, h2 are in the same subnet; therefore, there are no switches or routers in the middle.

For this question, i will use IP datagram's option fiel, which is rarely used, to identify whether the packet has been encrypted
1)

In h2, it firstly check the IP datagram's option filed. If the datagram has been encrypted, it will be sent to the given ip destination; otherwise, h2 will get the payload of the IP datagram, then use Caesar's code to encrypt the payload; then the encrypted UDP data is encapulated in a new IP datagram with the src IP is 10.0.0.102, the dst IP is the original packet's src IP; then the IP datagram is encapsulated in the link layer frame with src MAC is 10:00:00:00:00:02 and dst MAC is the original packet's src MAC.

Therefore, the OpenFlow protocol's match part not only for the src and dst IP or src and dst MAC, but also for the encryption flag in the IP datagram's option field.

2)
encryption_flag = 0 for not encrypted UDP
encryption_flag = 1 for encrypted UDP

OpenFlow rules at h2:

match:  src IP 10.0.0.100, dst IP 10.0.0.101,  encryption_flag = 0 action: encypted UPD, set encryption_flag = 1, forward back to 10.0.0.100

match:  src IP 10.0.0.100, dst IP 10.0.0.101,  encryption_flag = 1 action: forward  to 10.0.0.101

match:  src IP 10.0.0.101, dst IP 10.0.0.100,  encryption_flag = 0 action: encypted UPD, set encryption_flag = 1, forward back to 10.0.0.101

match:  src IP 10.0.0.101, dst IP 10.0.0.100,  encryption_flag = 1 action:  forward  to 10.0.0.100

OpenFlow rules at h0:

match:  src IP 10.0.0.102, dst IP 10.0.0.100,  encryption_flag = 1 action: forward  to 10.0.0.101

OpenFlow rules at h1:

match:  src IP 10.0.0.102, dst IP 10.0.0.101,  encryption_flag = 1 action: forward  to 10.0.0.100
3)

check(IP_datagram):

        ip_src = get_IP_src(IP_datagram)
        ip_dst = get_IP_dst(IP_datagram)
        encrypt_flag = get_encrypt_flag(IP_datagram)
        
        if(encrypt_flag == 0):
            original_payload = get_payload(IP_datagram)
            new_payload = Caesar(original_payload)
            packet = get_packet(host_ip, ip_src, new_payload)
            send(packet)
        else:
            send(IP_datagram)
