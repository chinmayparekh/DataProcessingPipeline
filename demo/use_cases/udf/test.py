from dpp import xml_parser as xml_parser

if __name__ == '__main__':
    if xml_parser.validate_xml('/chin/semester8/data_modelling/project/data_processing_pipeline/demo/use_cases/udf/input_udf.xml'):
        xml_parser.parse_and_execute("/chin/semester8/data_modelling/project/data_processing_pipeline/demo/use_cases/udf/input_udf.xml")
    else:
        print("The XML file is invalid.")