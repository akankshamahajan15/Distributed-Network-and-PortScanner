
import requests
import subprocess
import socket
import json
from requests.adapters import HTTPAdapter
from scapy.all import *

def tcp_scan(ip, ports):
	open_ports = ""
	closed_ports = []
	src_port = RandShort()

	for port in ports:
		port = int(port)
		# Creating a SYN packet and sending the packet
		response = sr1(IP(dst=ip)/TCP(sport=src_port,dport=port,flags="S"),timeout=10)
		
		if(str(type(response)) == "<type 'NoneType'>"):
			closed_ports.append(port)
		elif(response.haslayer(TCP)):
			if(response.getlayer(TCP).flags == 0x12):
				send_rst = sr(IP(dst=ip)/TCP(sport=src_port,dport=port,flags="AR"),timeout=10)
				open_ports+=str(port)
				open_ports+=","
			elif(response.getlayer(TCP).flags == 0x14):
				closed_ports.append(port)
	return open_ports

def syn_scan(ip, ports):
	open_ports = ""
	closed_ports = []
	filtered_ports = ""
	filt_open_ports = ""
	src_port = RandShort()
	
	for port in ports:
		port = int(port)
		response = sr1(IP(dst=ip)/TCP(sport=src_port,dport=port,flags="S"),timeout=10)
		if(str(type(response))=="<type 'NoneType'>"):
			#filtered_ports.append(port)
			filtered_ports+=str(port)
			filtered_ports+=","
		elif(response.haslayer(TCP)):
			if(response.getlayer(TCP).flags == 0x12):
				send_rst = sr(IP(dst=ip)/TCP(sport=src_port,dport=port,flags="R"),timeout=10)
				#open_ports.append(port)
				open_ports+=str(port)
				open_ports+=","
			elif(response.getlayer(TCP).flags == 0x14):
				closed_ports.append(port)
		elif(response.haslayer(ICMP)):
			if(int(response.getlayer(ICMP).type)==3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
				#filtered_ports.append(port)
				open_ports+=str(port)
				open_ports+=","

	filt_open_ports = open_ports + "-" + filtered_ports
	return filt_open_ports

def fin_scan(ip, ports):
	#open_ports = []
	open_ports = ""
	closed_ports = []
	#filtered_ports = []
	filtered_ports = ""
	filt_open_ports = ""
	#port_start = (int)(ports.split(',')[0], 10)
	#port_end = (int)(ports.split(',')[1], 10)
	
	src_port = RandShort()
	
	#for port in range(port_start, port_end):
	for port in ports:
		port = int(port)
		response = sr1(IP(dst=ip)/TCP(dport=port,flags="F"), timeout=10)
		if(str(type(response)) == "<type 'NoneType'>"):
			#open_ports.append(port)
			open_ports+=str(port)
			open_ports+=","
		elif(response.haslayer(TCP)):
			if(response.getlayer(TCP).flags == 0x14):
				closed_ports.append(port)
		elif(response.haslayer(ICMP)):
			if(int(response.getlayer(ICMP).type)==3 and int(response.getlayer(ICMP).code) in [1,2,3,9,10,13]):
				#filtered_ports.append(port)
				filtered_ports+=str(port)
				filtered_ports+=","
	filt_open_ports = open_ports + "-" + filtered_ports
	return filt_open_ports

def ping_test(ip):
	res = subprocess.call(['ping', ip, "-c", "3"])
	if res == 0:
		return True
	else:
		return False

s = requests.Session()

s.mount('http://', requests.adapters.HTTPAdapter(max_retries=3))
URL = "http://192.168.1.10:8000/scan_api/scan"
PARAMS = {'token': "c34c3", 'slave_ip': "192.168.1.8"}

try:
	r = s.get(url = URL, params = PARAMS)
	r.raise_for_status()
except requests.exceptions.HTTPError as errh:
	print ("HTTP Error:", errh)
except requests.exceptions.ConnectionError as errc:
	print ("Error Connecting:", errc)
except requests.exceptions.Timeout as errt:
	print ("Timeout Error:", errt)
except requests.exceptions.RequestException as err:
	print ("Something else:", err)

print(r.content)
string = r.content
string1 = string.decode('utf-8')
data = json.loads(string1)

#print(data["IP"])
#print(data["port_list"])

port_range = (data["port_list"]).encode('utf8')
#port_range = data["port_list"]
#port_list_new = []
port_list_new = port_range.split(',')
port_list_new = [i.encode('utf8') for i in port_list_new]
print(port_list_new)

res = ping_test(data["IP"])
print("Ping result", res)

#res_str = ""
if res == True:
	if "-1" in port_range:
		res_str = "Yes"
	elif data["type"] == "FULL_TCP_Connect":
		res_str = tcp_scan(data["IP"], port_list_new)
	elif data["type"] == "TCP_SYN":
		res_str = syn_scan(data["IP"], port_list_new)
	elif data["type"] == "TCP_FIN":
		res_str = fin_scan(data["IP"], port_list_new)
else:
	res_str = "No"

print(res_str)

PARAMS = {'token': "c34c3", 'slave_ip': "192.168.1.8", 'result': res_str}
r = requests.get(url = URL, params = PARAMS)

print("Result posted")
