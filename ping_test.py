import subprocess

def main():
	address = '127.0.0.1'
	res = subprocess.call(['ping', address])
	if res == 0:
		print ("ping to", address, "successful")
	elif res == 2:
		print ("no response from "+ address)
	else:
		print ("ping to", address, "failed!")
	return res

if __name__ == "__main__":
    main()
