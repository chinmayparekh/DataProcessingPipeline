from dpp import xml_parser as xml_parser

if __name__ == '__main__':
    if xml_parser.validate_xml('/home/chinmay/chin/semester8/data_modelling/project/data_processing_pipeline/DataProcessingPipeline/demo/use_cases/star_schema/test_join.xml'):
        xml_parser.parse_and_execute("/home/chinmay/chin/semester8/data_modelling/project/data_processing_pipeline/DataProcessingPipeline/demo/use_cases/star_schema/test_join.xml")
    else:
        print("The XML file is invalid.")