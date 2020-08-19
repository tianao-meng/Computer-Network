For this question, I use LinuxRouter as my routers instead of L3-Switch.

Firstly, run the following command to create the given topology:

sudo python custom_topology.py

Then run the follwing two commands to add route to Robert and Richard:

Richard route add -net 10.1.1.0/24 gw 10.4.4.14

This command makes Richard know that packets going to the 10.1.1.0/24 subnet should be routed via 10.4.4.14

Robert route add -net 10.6.6.0/24 gw 10.4.4.46

This command makes Robert know that packets going to the 10.6.6.0/24 subnet should be routed via 10.4.4.46

Then run Alice ping Carol get the following results:

PING 10.6.6.69 (10.6.6.69) 56(84) bytes of data.
64 bytes from 10.6.6.69: icmp_seq=1 ttl=62 time=1.34 ms
64 bytes from 10.6.6.69: icmp_seq=2 ttl=62 time=0.069 ms
64 bytes from 10.6.6.69: icmp_seq=3 ttl=62 time=0.070 ms
64 bytes from 10.6.6.69: icmp_seq=4 ttl=62 time=0.070 ms
64 bytes from 10.6.6.69: icmp_seq=5 ttl=62 time=0.051 ms
^C
--- 10.6.6.69 ping statistics ---
5 packets transmitted, 5 received, 0% packet loss, time 4002ms
rtt min/avg/max/mdev = 0.051/0.321/1.346/0.512 ms

Then Carol ping Alice get the following results:

PING 10.1.1.17 (10.1.1.17) 56(84) bytes of data.
64 bytes from 10.1.1.17: icmp_seq=1 ttl=62 time=0.835 ms
64 bytes from 10.1.1.17: icmp_seq=2 ttl=62 time=0.070 ms
64 bytes from 10.1.1.17: icmp_seq=3 ttl=62 time=0.071 ms
64 bytes from 10.1.1.17: icmp_seq=4 ttl=62 time=0.069 ms
^C
--- 10.1.1.17 ping statistics ---
4 packets transmitted, 4 received, 0% packet loss, time 3002ms
rtt min/avg/max/mdev = 0.069/0.261/0.835/0.331 ms






