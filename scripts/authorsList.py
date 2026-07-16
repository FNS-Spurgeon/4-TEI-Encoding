import os
import xml.etree.ElementTree as ET

list_folder = "../tei-files/vol2-1876-1900-xml"
authors_xml = "../tei-files/authors.xml"
list_author = []

ns = {'tei': 'http://www.tei-c.org/ns/1.0'}
ET.register_namespace('', 'http://www.tei-c.org/ns/1.0')

for subdir, dirs, files in os.walk(list_folder):
    for file in files:
        xml_path = os.path.join(subdir, file)

        if not xml_path.endswith('.DS_Store') | xml_path.endswith('taxonomy.xml') | xml_path.endswith('.xpr') | xml_path.endswith('authors.xml'):
            tree = ET.parse(xml_path)
            root = tree.getroot()
            # print(root)

            author = root.find('.//tei:analytic/tei:author', ns)
            list_author.append(author.text)

list_author = list(dict.fromkeys(list_author))
list_author.sort()
# print(list_author)

tree = ET.parse(authors_xml)
root = tree.getroot()
standOff = root.find('.//tei:standOff', ns)
listPerson = ET.SubElement(standOff, 'listPerson')

for author in list_author:
    firstName = author.split(",")[0]

    person = ET.SubElement(listPerson, "person")
    person.set('n', firstName)
    person.set('{http://www.w3.org/XML/1998/namespace}id', firstName)

    name = ET.SubElement(person, "name")
    name.text = author

ET.indent(listPerson)
print(ET.tostring(root, encoding='unicode', method='xml', short_empty_elements=True))

tree.write(authors_xml, encoding="UTF-8", xml_declaration=True)
