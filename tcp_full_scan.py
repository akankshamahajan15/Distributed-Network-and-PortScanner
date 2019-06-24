from scapy.all import *
 
def tcp_scan(ip, ports):
	open_ports = []
	closed_ports = []
	
	# Generating a random port as the source port
	src_port = RandShort()
	
	for port in range(ports):
		# Creating a SYN packet and sending the packet
		response = sr1(IP(dst=ip)/TCP(sport=src_port,dport=port,flags="S"),timeout=10)
		
		if(str(type(response)) == "<type 'NoneType'>"):
			closed_ports.append(port)
		elif(response.haslayer(TCP)):
			if(response.getlayer(TCP).flags == 0x12):
				send_rst = sr(IP(dst=ip)/TCP(sport=src_port,dport=port,flags="AR"),timeout=10)
				open_ports.append(port)
			elif(response.getlayer(TCP).flags == 0x14):
				closed_ports.append(port)
	return open_ports
