import xmltodict
with open('r1.xml', 'r') as file:
    xml_data = file.read()

data_dict = xmltodict.parse(xml_data)
print(data_dict['router']['interfaces'])
