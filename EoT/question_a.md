I will list the commands to enable h2 to ping h4 each other:

ovs-vsctl set bridge s2 protocols=OpenFlow13  in xterm terminal of s2
ovs-vsctl set bridge s3 protocols=OpenFlow13  in xterm terminal of s3
ovs-vsctl set bridge s4 protocols=OpenFlow13  in xterm terminal of s4


then in xterm terminal of s2:

ovs-ofctl -O OpenFlow13 add-flow s2 in_port=1,ip,nw_src=10.0
.2.2,nw_dst=10.0.4.2,actions=mod_dl_src:0A:00:0D:01:00:04,mod_dl_dst:0A:00:0D:F
E:00:02,output=4

This command means that when switch s2 receives the packet whose src ip is 10.0.2.2, and dst ip is 10.0.4.2 at port 1, then fowards the packet to port 4, and modifies the MAC src to 0A:00:0D:01:00:04, modifies the MAC dst to 0A:00:0D:FE:00:02, to enable the packet flow to the switch with interface 0A:00:0D:FE:00:02.

ovs-ofctl -O OpenFlow13 add-flow s3 in_port=2,ip,nw_src=10.0
.2.2,nw_dst=10.0.4.2,actions=mod_dl_src:0A:00:0E:01:00:03,mod_dl_dst:0A:00:0E:F
E:00:02,output=3

This command means that when switch s3 receives the packet whose src ip is 10.0.2.2, and dst ip is 10.0.4.2 at port 2, then fowards the packet to port 3, and modifies the MAC src to 0A:00:0E:01:00:03, modifies the MAC dst to 0A:00:0E:FE:00:02, to enable the packet flow to the switch with interface 0A:00:0E:FE:00:02.

ovs-ofctl -O OpenFlow13 add-flow s4 in_port=2,ip,nw_src=10.0
.2.2,nw_dst=10.0.4.2,actions=mod_dl_src:0A:00:04:01:00:01,mod_dl_dst:0A:00:04:0
2:00:00,output=1

This command means that when switch s4 receives the packet whose src ip is 10.0.2.2, and dst ip is 10.0.4.2 at port 2, then fowards the packet to port 1, and modifies the MAC src to 0A:00:04:01:00:01, modifies the MAC dst to 0A:00:04:02:00:00, to enable the packet flow to h4 with interface 0A:00:04:02:00:00.

then in xterm terminal of s4:

ovs-ofctl -O OpenFlow13 add-flow s4 in_port=1,ip,nw_src=10.0
.4.2,nw_dst=10.0.2.2,actions=mod_dl_src:0A:00:0E:FE:00:02,mod_dl_dst:0A:00:0E:0
1:00:03,output=2

This command means that when switch s4 receives the packet whose src ip is 10.0.4.2, and dst ip is 10.0.2.2 at port 1, then fowards the packet to port 2, and modifies the MAC src to 0A:00:0E:FE:00:02, modifies the MAC dst to 0A:00:0E:01:00:03, to enable the packet flow to the switch with interface 0A:00:0E:01:00:03.

ovs-ofctl -O OpenFlow13 add-flow s3 in_port=3,ip,nw_src=10.0
.4.2,nw_dst=10.0.2.2,actions=mod_dl_src:0A:00:0D:FE:00:02,mod_dl_dst:0A:00:0D:0
1:00:04,output=2

This command means that when switch s3 receives the packet whose src ip is 10.0.4.2, and dst ip is 10.0.2.2 at port 3, then fowards the packet to port 2, and modifies the MAC src to 0A:00:0D:FE:00:02, modifies the MAC dst to 0A:00:0D:01:00:04, to enable the packet flow to the switch with interface 0A:00:0D:01:00:04.

ovs-ofctl -O OpenFlow13 add-flow s2 in_port=4,ip,nw_src=10.0
.4.2,nw_dst=10.0.2.2,actions=mod_dl_src:0A:00:02:01:00:01,mod_dl_dst:0A:00:02:0
2:00:00,output=1

This command means that when switch s2 receives the packet whose src ip is 10.0.4.2, and dst ip is 10.0.2.2 at port 4, then fowards the packet to port 1, and modifies the MAC src to 0A:00:02:01:00:01, modifies the MAC dst to 0A:00:02:02:00:00, to enable the packet flow to h2 with interface 0A:00:02:02:00:00.

Next i will list the commands to enable h1 to ping h6 each other:

ovs-vsctl set bridge s1 protocols=OpenFlow13  in xterm terminal of s1
ovs-vsctl set bridge s2 protocols=OpenFlow13  in xterm terminal of s2
ovs-vsctl set bridge s3 protocols=OpenFlow13  in xterm terminal of s3
ovs-vsctl set bridge s6 protocols=OpenFlow13  in xterm terminal of s6

then in xterm terminal of s1:

ovs-ofctl -O OpenFlow13 add-flow s1 in_port=1,ip,nw_src=10.0
.1.2,nw_dst=10.0.6.2,actions=mod_dl_src:0A:00:0C:01:00:03,mod_dl_dst:0A:00:0C:F
E:00:03,output=3

This command means that when switch s1 receives the packet whose src ip is 10.0.1.2, and dst ip is 10.0.6.2 at port 1, then fowards the packet to port 3, and modifies the MAC src to 0A:00:0C:01:00:03, modifies the MAC dst to 0A:00:0C:FE:00:03, to enable the packet flow to the switch with interface 0A:00:0C:FE:00:03.

ovs-ofctl -O OpenFlow13 add-flow s2 in_port=3,ip,nw_src=10.0
.1.2,nw_dst=10.0.6.2,actions=mod_dl_src:0A:00:0D:01:00:04,mod_dl_dst:0A:00:0D:F
E:00:02,output=4

This command means that when switch s2 receives the packet whose src ip is 10.0.1.2, and dst ip is 10.0.6.2 at port 3, then fowards the packet to port 4, and modifies the MAC src to 0A:00:0D:01:00:04, modifies the MAC dst to 0A:00:0D:FE:00:02, to enable the packet flow to the switch with interface 0A:00:0D:FE:00:02.

ovs-ofctl -O OpenFlow13 add-flow s3 in_port=2,ip,nw_src=10.0
.1.2,nw_dst=10.0.6.2,actions=mod_dl_src:0A:00:0F:01:00:04,mod_dl_dst:0A:00:0F:F
E:00:02,output=4

This command means that when switch s3 receives the packet whose src ip is 10.0.1.2, and dst ip is 10.0.6.2 at port 2, then fowards the packet to port 4, and modifies the MAC src to 0A:00:0F:01:00:04, modifies the MAC dst to 0A:00:0F:FE:00:02, to enable the packet flow to the switch with interface 0A:00:0F:FE:00:02.

ovs-ofctl -O OpenFlow13 add-flow s6 in_port=2,ip,nw_src=10.0
.1.2,nw_dst=10.0.6.2,actions=mod_dl_src:0A:00:06:01:00:01,mod_dl_dst:0A:00:06:0
2:00:00,output=1

This command means that when switch s6 receives the packet whose src ip is 10.0.1.2, and dst ip is 10.0.6.2 at port 2, then fowards the packet to port 1, and modifies the MAC src to 0A:00:06:01:00:01, modifies the MAC dst to 0A:00:06:02:00:00, to enable the packet flow to h6 with interface 0A:00:06:02:00:00.

then in xterm terminal of s6:

ovs-ofctl -O OpenFlow13 add-flow s6 in_port=1,ip,nw_src=10.0
.6.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:0F:FE:00:02,mod_dl_dst:0A:00:0F:0
1:00:04,output=2

This command means that when switch s6 receives the packet whose src ip is 10.0.6.2, and dst ip is 10.0.1.2 at port 1, then fowards the packet to port 2, and modifies the MAC src to 0A:00:0F:FE:00:02, modifies the MAC dst to 0A:00:0F:01:00:04, to enable the packet flow to the switch with interface 0A:00:0F:01:00:04.

ovs-ofctl -O OpenFlow13 add-flow s3 in_port=4,ip,nw_src=10.0
.6.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:0D:FE:00:02,mod_dl_dst:0A:00:0D:0
1:00:04,output=2

This command means that when switch s3 receives the packet whose src ip is 10.0.6.2, and dst ip is 10.0.1.2 at port 4, then fowards the packet to port 2, and modifies the MAC src to 0A:00:0D:FE:00:02, modifies the MAC dst to 0A:00:0D:01:00:04, to enable the packet flow to the switch with interface 0A:00:0D:01:00:04.

ovs-ofctl -O OpenFlow13 add-flow s2 in_port=4,ip,nw_src=10.0
.6.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:0C:FE:00:03,mod_dl_dst:0A:00:0A:F
E:00:02,output=3

This command means that when switch s2 receives the packet whose src ip is 10.0.6.2, and dst ip is 10.0.1.2 at port 4, then fowards the packet to port 3, and modifies the MAC src to 0A:00:0C:FE:00:03, modifies the MAC dst to 0A:00:0A:FE:00:02, to enable the packet flow to the switch with interface 0A:00:0A:FE:00:02.

ovs-ofctl -O OpenFlow13 add-flow s1 in_port=3,ip,nw_src=10.0
.6.2,nw_dst=10.0.1.2,actions=mod_dl_src:0A:00:01:01:00:01,mod_dl_dst:0A:00:01:0
2:00:00,output=1

This command means that when switch s1 receives the packet whose src ip is 10.0.6.2, and dst ip is 10.0.1.2 at port 3, then fowards the packet to port 1, and modifies the MAC src to 0A:00:01:01:00:01, modifies the MAC dst to 0A:00:01:02:00:00, to enable the packet flow to h1 with interface 0A:00:01:02:00:00.


At last, i will list the commands to enable h0 to ping h3 each other:

ovs-vsctl set bridge s0 protocols=OpenFlow13  in xterm terminal of s0
ovs-vsctl set bridge s2 protocols=OpenFlow13  in xterm terminal of s2
ovs-vsctl set bridge s3 protocols=OpenFlow13  in xterm terminal of s3


then in xterm terminal of s0:

ovs-ofctl -O OpenFlow13 add-flow s0 in_port=1,ip,nw_src=10.0
.0.2,nw_dst=10.0.3.2,actions=mod_dl_src:0A:00:0B:01:00:03,mod_dl_dst:0A:00:0B:F
E:00:02,output=3

This command means that when switch s0 receives the packet whose src ip is 10.0.0.2, and dst ip is 10.0.3.2 at port 1, then fowards the packet to port 3, and modifies the MAC src to 0A:00:0B:01:00:03, modifies the MAC dst to 0A:00:0B:FE:00:02, to enable the packet flow to the switch with interface 0A:00:0B:FE:00:02.

ovs-ofctl -O OpenFlow13 add-flow s2 in_port=2,ip,nw_src=10.0
.0.2,nw_dst=10.0.3.2,actions=mod_dl_src:0A:00:0D:01:00:04,mod_dl_dst:0A:00:0D:F
E:00:02,output=4

This command means that when switch s2 receives the packet whose src ip is 10.0.0.2, and dst ip is 10.0.3.2 at port 2, then fowards the packet to port 4, and modifies the MAC src to 0A:00:0D:01:00:04, modifies the MAC dst to 0A:00:0D:FE:00:02, to enable the packet flow to the switch with interface 0A:00:0D:FE:00:02.

ovs-ofctl -O OpenFlow13 add-flow s3 in_port=2,ip,nw_src=10.0
.0.2,nw_dst=10.0.3.2,actions=mod_dl_src:0A:00:03:01:00:01,mod_dl_dst:0A:00:03:0
2:00:00,output=1

This command means that when switch s3 receives the packet whose src ip is 10.0.0.2, and dst ip is 10.0.3.2 at port 2, then fowards the packet to port 1, and modifies the MAC src to 0A:00:03:01:00:01, modifies the MAC dst to 0A:00:03:02:00:00, to enable the packet flow to h3 with interface 0A:00:03:02:00:00.

then in xterm terminal of s3:

ovs-ofctl -O OpenFlow13 add-flow s3 in_port=1,ip,nw_src=10.0
.3.2,nw_dst=10.0.0.2,actions=mod_dl_src:0A:00:0D:FE:00:02,mod_dl_dst:0A:00:0D:0
1:00:04,output=2

This command means that when switch s3 receives the packet whose src ip is 10.0.3.2, and dst ip is 10.0.0.2 at port 1, then fowards the packet to port 2, and modifies the MAC src to 0A:00:0D:FE:00:02, modifies the MAC dst to 0A:00:0D:01:00:04, to enable the packet flow to the switch with interface 0A:00:0D:01:00:04.

ovs-ofctl -O OpenFlow13 add-flow s2 in_port=4,ip,nw_src=10.0
.3.2,nw_dst=10.0.0.2,actions=mod_dl_src:0A:00:0B:FE:00:02,mod_dl_dst:0A:00:0B:0
1:00:03,output=2

This command means that when switch s2 receives the packet whose src ip is 10.0.3.2, and dst ip is 10.0.0.2 at port 4, then fowards the packet to port 2, and modifies the MAC src to 0A:00:0B:FE:00:02, modifies the MAC dst to 0A:00:0B:01:00:03, to enable the packet flow to the switch with interface 0A:00:0B:01:00:03.

ovs-ofctl -O OpenFlow13 add-flow s0 in_port=3,ip,nw_src=10.0
.3.2,nw_dst=10.0.0.2,actions=mod_dl_src:0A:00:00:01:00:01,mod_dl_dst:0A:00:00:0
2:00:00,output=1

This command means that when switch s0 receives the packet whose src ip is 10.0.3.2, and dst ip is 10.0.0.2 at port 3, then fowards the packet to port 1, and modifies the MAC src to 0A:00:00:01:00:01, modifies the MAC dst to 0A:00:00:02:00:00, to enable the packet flow to h1 with interface 0A:00:00:02:00:00.





