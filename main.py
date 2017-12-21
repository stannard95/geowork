import xml.etree.ElementTree as ET
from flask import Flask
import test_server

app = Flask(__name__)

@app.route("/")

# when the route is accessed call hello
def hello():
	tree = ET.parse('mini-schema.xml')
	root = tree.getroot()

	test_server.runTest()

	for i in root:
		for j in i:
			name = j.find('name').text
			value = int(j.find('value').text)
			test_server.test_return(value)
			notes = j.find('notes').text
			print(name, value, notes)
	return "test xml devices"


if __name__ == '__main__':
    app.run(debug=True)



