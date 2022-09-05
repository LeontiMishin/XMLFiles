import xml.etree.ElementTree as ET

tree = ET.parse('currency.xml')
root = tree.getroot()
print(root)


for currency in root.iter('currency'):
    print(currency.attrib)
    # year=child.get
    # for currency in root.findall('currency'):
    #     title = currency.find('title').text
    #     country = currency.get('country')
    #     print(title, country)
