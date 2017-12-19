import xml.etree.ElementTree as ET

tree = ET.parse('mini-schema.xml')
root = tree.getroot()

for i in root:
	for j in i:
		name = j.find('name').text
		value = int(j.find('value').text)
		notes = j.find('notes').text
		print(name, value, notes)