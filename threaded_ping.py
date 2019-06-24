import subprocess
import ipaddress
import threading

net_addr = u'192.168.1.0/24'
ip_net = ipaddress.ip_network(net_addr)
all_hosts = list(ip_net.hosts())
port_list = [22, 1, 80, 34, 2]
alive_addr = []
def ping(ip):
	ping = subprocess.Popen(['ping', '-c', '1', ip], stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()[0]
	if "Destination Host Unreachable" in ping.decode('utf-8'):
		flag = False
	elif "Request timed out" in ping.decode('utf-8'):
		flag = False
	else:
		flag = True
		alive_addr.append(ip)

	return alive_addr

for i in range(len(all_hosts)):
	threading.Thread(target=ping, args=(str(all_hosts[i]),)).run()
print(alive_addr)
