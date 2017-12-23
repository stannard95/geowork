import socket;
import unittest;
import colorama
from colorama import Fore, Back, Style

colorama.init()

def portTest():
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	result = sock.connect_ex(('localhost', 5000))

	print(Fore.GREEN + "==> 	RUNNING WEBSERVER TEST" + Style.RESET_ALL)

	if (result == 0):
	   print (Fore.GREEN + "==> 	Port is open\n" + Style.RESET_ALL)
	else:
	   print ("==> 	Port is not open\n" + Style.RESET_ALL)


def deviceValueTest(x):
	try:
  		int(x)
  		return True
	except ValueError:
		print (Fore.GREEN + "==> 	"+ x + " Not a int" + Style.RESET_ALL)
		return False