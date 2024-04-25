from dpp import xml_parser as xml_parser

if __name__ == '__main__':
    if xml_parser.validate_xml('excel.xml'):
        xml_parser.parse_and_execute("excel.xml")
    else:
        print("The XML file is invalid.")