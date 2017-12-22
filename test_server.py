import socket;
import unittest;

def runTest():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('localhost', 5000))

	print("==> RUNNING WEBSERVER TEST")
	if (result == 0):
	   print ("==> Port is open\n")
	else:
	   print ("==> Port is not open\n")


def test_return(x):
	try:
  		int(x)
  		print ("==> Is an int")
  		return True
	except ValueError:
		print ("==> Not a int")
		return False