import sys
import requests
import xml.etree.ElementTree as ET

def get_args():
    if len(sys.argv) != 2:
        print('Usage: python query_ena_api.py <ENA_ACCESSION>')
        sys.exit()
    else:
        return sys.argv[1]

def query_api_parse_response(ena_accession):
    response = requests.get(f'https://www.ebi.ac.uk/ena/browser/api/xml/{ena_accession}')
    return response

def parse_xml_get_err(response):
    tree = ET.ElementTree(ET.fromstring(response.content))
    # print(vars(tree))
    root = tree.getroot()
    # print(root.attrib)
    for child in root.iter():
        if child.text.startswith('ERR'):
            print(child.text)

def main():
    ena_accession = get_args()
    response = query_api_parse_response(ena_accession)
    parse_xml_get_err(response)

if __name__ == '__main__':
    main()
