from dpp import xml_parser as xml_parser

if __name__ == '__main__':
    if xml_parser.validate_xml('/home/kritin/College/DM/Project/DataProcessingPipeline/input/input_udf.xml'):
        xml_parser.parse_and_execute("/home/kritin/College/DM/Project/DataProcessingPipeline/input/input_udf.xml")
    else:
        print("The XML file is invalid.")