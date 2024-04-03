import xml.etree.ElementTree as ET
from lxml import etree
import lib.task_library as task_library

def validate_xml(xml_path, xsd_path):
    schema_root = etree.parse(xsd_path)
    schema = etree.XMLSchema(schema_root)

    xml_root = etree.parse(xml_path)

    result = schema.validate(xml_root)

    if result:
        return True
    else:
        print(schema.error_log)
        return False

def parse_and_execute(xml_path):
    tree = ET.parse(xml_path)
    root = tree.getroot()

    for stage in root.findall('stage'):
        task = stage.find('task').text
        print(task)
        input_file_path = stage.find('input').text
        output_file_path = stage.find('output').text

        # Calling the appropriate function from the task library
        if hasattr(task_library, task):
            getattr(task_library, task)(input_file_path, output_file_path)



if validate_xml('input/process1.xml', 'schema/pipeline.xsd'):
    parse_and_execute('input/process1.xml')
else:
    print("The XML file is invalid.")