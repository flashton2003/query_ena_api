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

def parse_xml_get_err(response, ena_accession):
    tree = ET.ElementTree(ET.fromstring(response.content))
    root = tree.getroot()
    for child in root.iter():
        try:
            ## the text attribute is the one I want
            if child.text.startswith('ERR'):
                print(ena_accession, child.text, sep = '\t')
                ## there should only be one ERR per file so can do this
                return
        except AttributeError:
            pass
    ## if get to the end of the file and not returned, then no hits
    print(f'No ERR record for {ena_accession}')

def main():
    '''
    Example output https://www.ebi.ac.uk/ena/browser/api/xml/ERS235824
    '''
    ena_accession = get_args()
    response = query_api_parse_response(ena_accession)
    parse_xml_get_err(response, ena_accession)

if __name__ == '__main__':
    main()
