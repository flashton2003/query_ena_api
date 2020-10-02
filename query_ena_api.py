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
        # print(child.tag, child.text)
        if child.text.startswith('ERR'):
            print(child.text)
        # print(dir(child))
        # if len(child) > 4:
            # print(child[4].tag, child[4].attrib)
        # print(child.tag, child.attrib)
    # for child in root.findall('ENA-RUN'):
        # print(child.tag, child.attrib)

    # pass

if __name__ == '__main__':
    main()
