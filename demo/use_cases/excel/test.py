from dpp import xml_parser as xml_parser

if __name__ == '__main__':
    if xml_parser.validate_xml('/home/kritin/College/DM/Project/DataProcessingPipeline/demo/use_cases/excel/input_excel.xml'):
        xml_parser.parse_and_execute("/home/kritin/College/DM/Project/DataProcessingPipeline/demo/use_cases/excel/input_excel.xml")
    else:
        print("The XML file is invalid.")