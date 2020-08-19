For part A, those commands i list need to be typed in, and not to copy paste in the xterm terminals. Then you will find those commands can work and satisfy the requirements of Part A.

For part B, use the following command to run my python file in mininet VM, just like the given example in part A
sudo python custom_topology.py

Environment setup:
I have the experience use VirtualBox, so i do not have to download VirtualBox
Firstly, I download Mininet VM image (mininet-vm-x86_64.vmdk)
Then create the new Virtual machine of Linux(64 bits) operating system using the downloaded image.
Setup the Network of the VM, adapter 1 uses NAT, adapter uses Host-only-adapter, perimission mode allow all.
Run ifconfig -a to check IP address of VM
Because i use eth1 interface, run the sudo dhclient eth1 in VM
sudo service ssh start in VM
From host machine, ssh mininet@<VM IP>, where <VM IP>  you can now run  ifconfig -a to get eth1 IP addr to get
Now you have been ssh into mininet
Also you can transfer files using scp -r <PATH IN HOST MACHINE> mininet@<VM IP>:<PATH IN GUEST VM >




