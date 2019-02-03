import xml.etree.ElementTree as etree
import json

class JSONConnector:
    def __init__( self, filepath ):
        self._parsed_data = dict()
        with open(filepath, mode='r', encoding='utf-8') as f:
            self._parsed_data = json.load(f)

    @property
    def parsed_data( self ):
        return self._parsed_data

class XMLConnector:
    def __init__( self, filepath ):
        self.tree = etree.parse(filepath)

    @property
    def parsed_data( self ):
        return self.tree

def connection_factory( filepath ):
    if filepath.endswith('json'):
        connector = JSONConnector
    elif filepath.endswith('xml'):
        connector = XMLConnector
    else:
        raise ValueError(f'Cannot connect to {filepath}')
    return connector(filepath)

def connect_to( filepath ):
    factory = None
    try:
        factory = connection_factory( filepath )
    except ValueError as ve:
        print(ve)
    return factory

def main():
    sqlite_factory = connect_to('data/person.sq3')

    xml_factory = connect_to('data/person.xml')
    xml_data = xml_factory.parsed_data    
    [print(person.find('firstName').text, person.find('lastName').text, end=', ') 
        for person in xml_data.findall(".//person[lastName='Liar']")]
    print()
        
    # liars = xml_data.findall(
    #     "//{person}[{lastName='{}'}]"
    #         .format('Liar')
    # )
    # print(f'found: {len(liars)} persons')

    json_factory = connect_to('data/donut.json')
    json_data = json_factory.parsed_data
    print(f'found: {len(json_data)} donuts')
    for donut in json_data:
        print(f"name: {donut['name']}")
        print(f"price: ${donut['ppu']}")
        [print(f"topping: {t['id'], t['type']}") for t
            in donut['topping']]
        print()


if __name__ == '__main__':
       main()   

