1)
POX 0.3.0 (dart) / Copyright 2011-2014 James McCauley, et al.
DEBUG:core:POX 0.3.0 (dart) going up...
DEBUG:core:Running on CPython (2.7.6/Oct 26 2016 20:30:19)
DEBUG:core:Platform is Linux-4.2.0-27-generic-x86_64-with-Ubuntu-14.04-trusty
INFO:core:POX 0.3.0 (dart) is up.
DEBUG:openflow.of_01:Listening on 0.0.0.0:6633
INFO:openflow.of_01:[00-00-00-00-00-03 5] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-03 5]
INFO:openflow.of_01:[00-00-00-00-00-05 2] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-05 2]
INFO:openflow.of_01:[00-00-00-00-00-04 6] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-04 6]
INFO:openflow.of_01:[00-00-00-00-00-02 3] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-02 3]
INFO:openflow.of_01:[00-00-00-00-00-01 4] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-01 4]
INFO:openflow.of_01:[00-00-00-00-00-07 7] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-07 7]
INFO:openflow.of_01:[00-00-00-00-00-06 8] connected
DEBUG:forwarding.l2_learning:Connection [00-00-00-00-00-06 8]

DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.2 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.2
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.2 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.1 -> 00:00:00:00:00:01.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.2 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:05.3 -> 00:00:00:00:00:01.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.3
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.1 -> 00:00:00:00:00:05.2
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1
DEBUG:forwarding.l2_learning:installing flow for 00:00:00:00:00:01.3 -> 00:00:00:00:00:05.1

In this question, using the POX controller, i can instruct a high level policy, i.e. "h1 should be able to access h5". Then the POX controller figures out how that translates to low-level OpenFlow commands and deploy it on the network switching devices

From the output, we can see that the switches (s1, s2, s3, s5, s6) install the flow, which is computed by the POX controller, to enable that h1 can be access to h5.

2)

mininet> h1 ping h5
PING 10.0.0.5 (10.0.0.5) 56(84) bytes of data.
64 bytes from 10.0.0.5: icmp_seq=1 ttl=64 time=43.9 ms
64 bytes from 10.0.0.5: icmp_seq=2 ttl=64 time=0.367 ms
64 bytes from 10.0.0.5: icmp_seq=3 ttl=64 time=0.039 ms
64 bytes from 10.0.0.5: icmp_seq=4 ttl=64 time=0.041 ms
64 bytes from 10.0.0.5: icmp_seq=5 ttl=64 time=0.065 ms
64 bytes from 10.0.0.5: icmp_seq=6 ttl=64 time=0.037 ms
64 bytes from 10.0.0.5: icmp_seq=7 ttl=64 time=0.573 ms
64 bytes from 10.0.0.5: icmp_seq=8 ttl=64 time=0.041 ms
64 bytes from 10.0.0.5: icmp_seq=9 ttl=64 time=0.064 ms
64 bytes from 10.0.0.5: icmp_seq=10 ttl=64 time=0.036 ms
^C
--- 10.0.0.5 ping statistics ---
10 packets transmitted, 10 received, 0% packet loss, time 9002ms
rtt min/avg/max/mdev = 0.036/4.524/43.982/13.153 ms


Yes, there is a difference. The RTT of the first ping message is much larger than the subsequent ones.

Reason:
When ping first message, there are no flow tables in the switches. It takes a lot of time for controller to receive OpenFlow message, computes new flow table, and use OpenFlow to install new tables in switches; for routing algorithm to access network graph info, link state info, and computes routes.

For subsequent ping messages, the flow needed has been installed in the relevant switches.

3)

s1:

NXST_FLOW reply (xid=0x4):
cookie=0x0, duration=6.389s, table=0, n_packets=1, n_bytes=42, idle_timeout=10, hard_timeout=30, idle_age=6, priority=65535,arp,in_port=2,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,arp_spa=10.0.0.5,arp_tpa=10.0.0.1,arp_op=1 actions=output:1
cookie=0x0, duration=6.384s, table=0, n_packets=1, n_bytes=42, idle_timeout=10, hard_timeout=30, idle_age=6, priority=65535,arp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,arp_spa=10.0.0.1,arp_tpa=10.0.0.5,arp_op=2 actions=output:2
cookie=0x0, duration=27.386s, table=0, n_packets=27, n_bytes=2646, idle_timeout=10, hard_timeout=30, idle_age=1, priority=65535,icmp,in_port=2,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,nw_src=10.0.0.5,nw_dst=10.0.0.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:1
cookie=0x0, duration=27.394s, table=0, n_packets=27, n_bytes=2646, idle_timeout=10, hard_timeout=30, idle_age=1, priority=65535,icmp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,nw_src=10.0.0.1,nw_dst=10.0.0.5,nw_tos=0,icmp_type=8,icmp_code=0 actions=output:2

s2:

NXST_FLOW reply (xid=0x4):
cookie=0x0, duration=9.409s, table=0, n_packets=1, n_bytes=42, idle_timeout=10, hard_timeout=30, idle_age=9, priority=65535,arp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,arp_spa=10.0.0.5,arp_tpa=10.0.0.1,arp_op=1 actions=output:1
cookie=0x0, duration=9.404s, table=0, n_packets=1, n_bytes=42, idle_timeout=10, hard_timeout=30, idle_age=9, priority=65535,arp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,arp_spa=10.0.0.1,arp_tpa=10.0.0.5,arp_op=2 actions=output:3
cookie=0x0, duration=29.429s, table=0, n_packets=29, n_bytes=2842, idle_timeout=10, hard_timeout=30, idle_age=1, priority=65535,icmp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,nw_src=10.0.0.1,nw_dst=10.0.0.5,nw_tos=0,icmp_type=8,icmp_code=0 actions=output:3
cookie=0x0, duration=29.422s, table=0, n_packets=29, n_bytes=2842, idle_timeout=10, hard_timeout=30, idle_age=1, priority=65535,icmp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,nw_src=10.0.0.5,nw_dst=10.0.0.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:1

s3:

NXST_FLOW reply (xid=0x4):
cookie=0x0, duration=8.967s, table=0, n_packets=1, n_bytes=42, idle_timeout=10, hard_timeout=30, idle_age=8, priority=65535,arp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,arp_spa=10.0.0.5,arp_tpa=10.0.0.1,arp_op=1 actions=output:1
cookie=0x0, duration=8.965s, table=0, n_packets=1, n_bytes=42, idle_timeout=10, hard_timeout=30, idle_age=8, priority=65535,arp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,arp_spa=10.0.0.1,arp_tpa=10.0.0.5,arp_op=2 actions=output:3
cookie=0x0, duration=8.974s, table=0, n_packets=9, n_bytes=882, idle_timeout=10, hard_timeout=30, idle_age=0, priority=65535,icmp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,nw_src=10.0.0.1,nw_dst=10.0.0.5,nw_tos=0,icmp_type=8,icmp_code=0 actions=output:3
cookie=0x0, duration=8.891s, table=0, n_packets=9, n_bytes=882, idle_timeout=10, hard_timeout=30, idle_age=0, priority=65535,icmp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,nw_src=10.0.0.5,nw_dst=10.0.0.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:1

s4:

NXST_FLOW reply (xid=0x4):

s5:

NXST_FLOW reply (xid=0x4):
cookie=0x0, duration=10.311s, table=0, n_packets=1, n_bytes=42, idle_timeout=10, hard_timeout=30, idle_age=10, priority=65535,arp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,arp_spa=10.0.0.1,arp_tpa=10.0.0.5,arp_op=2 actions=output:1
cookie=0x0, duration=0.328s, table=0, n_packets=1, n_bytes=98, idle_timeout=10, hard_timeout=30, idle_age=0, priority=65535,icmp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,nw_src=10.0.0.1,nw_dst=10.0.0.5,nw_tos=0,icmp_type=8,icmp_code=0 actions=output:1
cookie=0x0, duration=0.324s, table=0, n_packets=1, n_bytes=98, idle_timeout=10, hard_timeout=30, idle_age=0, priority=65535,icmp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,nw_src=10.0.0.5,nw_dst=10.0.0.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:3

s6:

cookie=0x0, duration=10.158s, table=0, n_packets=11, n_bytes=1078, idle_timeout=10, hard_timeout=30, idle_age=2, priority=65535,icmp,in_port=3,vlan_tci=0x0000,dl_src=00:00:00:00:00:01,dl_dst=00:00:00:00:00:05,nw_src=10.0.0.1,nw_dst=10.0.0.5,nw_tos=0,icmp_type=8,icmp_code=0 actions=output:1
cookie=0x0, duration=10.157s, table=0, n_packets=11, n_bytes=1078, idle_timeout=10, hard_timeout=30, idle_age=0, priority=65535,icmp,in_port=1,vlan_tci=0x0000,dl_src=00:00:00:00:00:05,dl_dst=00:00:00:00:00:01,nw_src=10.0.0.5,nw_dst=10.0.0.1,nw_tos=0,icmp_type=0,icmp_code=0 actions=output:3

s7:

NXST_FLOW reply (xid=0x4):

Part A:

In part A, use h0 ping h1 command, and review commands installed in s0 and s1, then compare with Part C results

s0:

OFPST_FLOW reply (OF1.3) (xid=0x2):
cookie=0x0, duration=58.109s, table=0, n_packets=96, n_bytes=9408, ip,in_port=1,nw_src=10.0.0.2,nw_dst=10.0.1.2 actions=mod_dl_src:0a:00:0a:01:00:02,mod_dl_dst:0a:00:0a:fe:00:02,output:2
cookie=0x0, duration=47.922s, table=0, n_packets=96, n_bytes=9408, ip,in_port=2,nw_src=10.0.1.2,nw_dst=10.0.0.2 actions=mod_dl_src:0a:00:00:01:00:01,mod_dl_dst:0a:00:00:02:00:00,output:1

s1:

OFPST_FLOW reply (OF1.3) (xid=0x2):
cookie=0x0, duration=470.93s, table=0, n_packets=96, n_bytes=9408, ip,in_port=1,nw_src=10.0.1.2,nw_dst=10.0.0.2 actions=mod_dl_src:0a:00:0a:fe:00:02,mod_dl_dst:0a:00:0a:01:00:02,output:2
cookie=0x0, duration=87.038s, table=0, n_packets=96, n_bytes=9408, ip,in_port=2,nw_src=10.0.0.2,nw_dst=10.0.1.2 actions=mod_dl_src:0a:00:01:01:00:01,mod_dl_dst:0a:00:01:02:00:00,output:1

Therefore, we can see that the rules in Part C are similar to rules in Part A.
In part C, they collectively achieve that h1 can ping h5. We can see that there are no rules in s4 and s7 because s4 and s7 have no responsibility of forwarding packets when h1 ping h5. The results make sense.




