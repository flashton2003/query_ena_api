import requests

def main():
    response = requests.get('https://www.ebi.ac.uk/ena/browser/api/xml/ERS235824')
    print(response.json())
    # pass

if __name__ = '__main__':
    main()
