import sys, traceback
import subprocess

# import "ping_test.py"



def ping_test():
	address = '127.0.0.1'
	res = subprocess.call(['ping', address])
	if res == 0:
		print ("ping to", address, "successful")
	elif res == 2:
		print ("no response from "+ address)
	else:
		print ("ping to", address, "failed!")
	return res

portRange = '40, 80'

if portRange == 'all':
	portStart = 1
	portEnd = 1024
else:
	try:
		portStart = (int)(portRange.split(',')[0], 10)
		portEnd = (int)(portRange.split(',')[1], 10)
		if (portStart <=0 or portEnd <=0 or portStart > portEnd):
			print("INVALID RANGE")
			sys.exit(1)
	except ValueError:
		print("INVALID RANGE")
		sys.exit(1)

ping_test()




#s2_out = subprocess.check_output([sys.executable, 'python ping_test.py'])
# print("Value returned", s2_out)
print(portStart)
print(portEnd)
