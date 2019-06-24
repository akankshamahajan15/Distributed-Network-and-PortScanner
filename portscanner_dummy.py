import socket

#remoteServer = 'https://www.hackthissite.org/'
remoteServerIP  = '35.229.17.89'
#socket.gethostbyname(remoteServer)


try:
	for port in range(8123, 8124):
		print (port)
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			print(port)
		else: 
			print "closed"
		sock.close()

except socket.gaierror:
	print ('Hostname could not be resolved. Exiting')
	sys.exit()

except socket.error:
	print ('Couldnt connect to server')
	sys.exit()
