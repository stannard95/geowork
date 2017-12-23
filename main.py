import xml.etree.ElementTree as ET
from flask import Flask
import test_server
import colorama
from colorama import Fore, Back, Style

colorama.init()
app = Flask(__name__)
@app.route("/")

# when the route is accessed call hello
def hello():
	tree = ET.parse('mini-schema.xml')
	root = tree.getroot()
	test_server.portTest()

	for i in root:
		for j in i:
			name = j.find('name').text
			notes = j.find('notes').text
			if (test_server.deviceValueTest(j.find('value').text)):
				value = int(j.find('value').text)
				print(name, value, notes)
			else:
				print(Fore.GREEN + "==> 	INVALID DEVICE VALUE: " + name, j.find('value').text, notes + Style.RESET_ALL)
	return "test xml devices"

if __name__ == '__main__':
    app.run(debug=True)



