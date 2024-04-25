from dpp import xml_parser as xml_parser
# def validate_xml(xml_path, xsd_path):
#     schema_root = etree.parse(xsd_path)
#     schema = etree.XMLSchema(schema_root)

#     xml_root = etree.parse(xml_path)

#     result = schema.validate(xml_root)

#     if result:
#         return True
#     else:
#         print(schema.error_log)
#         return False

# def parse_and_execute(xml_path):
#     tree = ET.parse(xml_path)
#     root = tree.getroot()

#     for stage in root.findall('stage'):
#         task = stage.find('task')
#         function_name = task.find('function').text
#         input_file_path = stage.find('input').text
#         output_file_path = stage.find('output').text
#         param = [param.text for param in task.findall('param')]

#         if hasattr(task_library, function_name):
#             if param:
#                 getattr(task_library, function_name)(input_file_path, output_file_path, param)
#             else:
#                 getattr(task_library, function_name)(input_file_path, output_file_path)

if __name__ == '__main__':
    if xml_parser.validate_xml('/home/chinmay/chin/semester8/data_modelling/project/data_processing_pipeline/input/input_text.xml', '/home/chinmay/chin/semester8/data_modelling/project/data_processing_pipeline/schema/pipeline2.xsd'):
        xml_parser.parse_and_execute('/home/chinmay/chin/semester8/data_modelling/project/data_processing_pipeline/input/input_text.xml')
    if xml_parser.validate_xml('/home/chinmay/chin/semester8/data_modelling/project/data_processing_pipeline/input/input_excel.xml', '/home/chinmay/chin/semester8/data_modelling/project/data_processing_pipeline/schema/pipeline2.xsd'):
        xml_parser.parse_and_execute('/home/chinmay/chin/semester8/data_modelling/project/data_processing_pipeline/input/input_excel.xml')
    else:
        print("The XML file is invalid.")