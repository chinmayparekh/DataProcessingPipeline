import logging
import subprocess
import xml.etree.ElementTree as ET
from lxml import etree
from dpp import task_library, udf

logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(message)s')


def execute_shell_script(input_file_path, output_file_path, function_name, param):
    command = function_name  
    command += f" {input_file_path} {output_file_path}"  

    try:
        subprocess.run(command, shell=True, check=True)
        logging.info(f"Executed shell script: {command}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Shell script execution failed: {e}")
        raise
    
def validate_xml(xml_path):
    xsd_string = """<xs:schema elementFormDefault="qualified"
    xmlns:xs="http://www.w3.org/2001/XMLSchema">
    
    <xs:complexType name="inputType">
        <xs:simpleContent>
            <xs:extension base="xs:string">
                <xs:attribute type="xs:string" name="type" use="required" />
            </xs:extension>
        </xs:simpleContent>
    </xs:complexType>

    <xs:complexType name="taskType" mixed="true">
        <xs:sequence>
            <xs:element type="xs:string" name="function" minOccurs="1" maxOccurs="1" />
            <xs:element type="xs:string" name="param" minOccurs="0" maxOccurs="unbounded" />
        </xs:sequence>
        <xs:attribute type="xs:string" name="type" use="required" />
    </xs:complexType>

    <xs:simpleType name="outputType">
        <xs:restriction base="xs:string" />
    </xs:simpleType>

    <xs:simpleType name="sequenceIdType">
        <xs:restriction base="xs:integer" />
    </xs:simpleType>

    <xs:complexType name="stageType">
        <xs:sequence>
            <xs:element type="inputType" name="input" />
            <xs:element type="taskType" name="task" />
            <xs:element type="outputType" name="output" minOccurs="0" />
            <xs:element type="sequenceIdType" name="sequenceId" />
        </xs:sequence>
    </xs:complexType>

    <xs:element name="pipeline">
        <xs:complexType>
            <xs:sequence>
                <xs:element type="stageType" name="stage" maxOccurs="unbounded" minOccurs="0" />
                <xs:element type="xs:string" name="config" minOccurs="1" maxOccurs="1" />
            </xs:sequence>
        </xs:complexType>
    </xs:element>
</xs:schema> """
    schema_root = etree.fromstring(xsd_string)
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
    config_path = root.find('config').text
   
    for stage in root.findall('stage'):
        task = stage.find('task')
        function_name = task.find('function').text
        input_file_path = stage.find('input').text
        output_file_path = stage.find('output').text
        param = [param.text for param in task.findall('param')]

        if function_name.endswith('.sh'):
            # Execute shell script
            print("SHELLING")
            logging.info("Executing Shell Script " + function_name) 
            execute_shell_script(input_file_path, output_file_path, function_name, param)

        elif hasattr(udf, function_name):
            logging.info('Executing UDF ' + function_name)
            if param:
                getattr(udf, function_name)(input_file_path, output_file_path, param)
            else:
                getattr(udf, function_name)(input_file_path, output_file_path)
        else:
            if hasattr(task_library, function_name):
                if hasattr(task_library, function_name):
                    if param:
                        getattr(task_library, function_name)(input_file_path, output_file_path, param,config_path)
                    else:
                        getattr(task_library, function_name)(input_file_path, output_file_path,config_path)

# if __name__ == '__main__':
#     if validate_xml('input/input_text.xml', 'schema/pipeline2.xsd'):
#         parse_and_execute('input/input_text.xml')
#     if validate_xml('input/input_excel.xml', 'schema/pipeline2.xsd'):
#         parse_and_execute('input/input_excel.xml')
#     else:
#         print("The XML file is invalid.")