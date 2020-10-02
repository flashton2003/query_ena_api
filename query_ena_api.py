import requests
import xml.etree.ElementTree as ET

def main():
    response = requests.get('https://www.ebi.ac.uk/ena/browser/api/xml/ERS235824')
    # print(vars(response))
    # print(response.content)
    tree = ET.ElementTree(ET.fromstring(response.content))
    # print(vars(tree))
    root = tree.getroot()
    # print(root.attrib)
    for child in root.iter():
        if child.text.startswith('ERR'):
            print(child.text)


if __name__ == '__main__':
    main()
