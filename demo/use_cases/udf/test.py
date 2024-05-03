from dpp import xml_parser as xml_parser

if __name__ == '__main__':
    if xml_parser.validate_xml('/Users/sumanth/Documents/sem8/DM/DataProcessingPipeline/demo/use_cases/udf/input_udf.xml'):
        xml_parser.parse_and_execute("/Users/sumanth/Documents/sem8/DM/DataProcessingPipeline/demo/use_cases/udf/input_udf.xml")
    else:
        print("The XML file is invalid.")