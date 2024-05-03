import logging
import subprocess
import xml.etree.ElementTree as ET
from lxml import etree
# from demo.use_cases.udf import udf
from dpp import task_library
import threading
from collections import defaultdict

logging.basicConfig(filename='app.log', level=logging.WARNING, format='%(asctime)s %(levelname)s %(message)s')

    
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
        <xs:attribute type="xs:string" name="language" use="optional" />
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
        return False

def parse_and_execute(xml_path):
    try:
        tree = ET.parse(xml_path)
        root = tree.getroot()
        config_path = root.find('config').text
    except Exception as e:
        logging.error("Error parsing XML: " + str(e))
        return

    # Group stages by sequence ID
    stage_groups = defaultdict(list)
    for stage in root.findall('stage'):
        sequence_id = int(stage.find('sequenceId').text)
        stage_groups[sequence_id].append(stage)

    # Execute stages in groups (based on sequence ID) in ascending order
    for sequence_id in sorted(stage_groups.keys()):
        # List to hold threads for current group
        threads = []

        # Create a thread for each stage in the current group
        for stage in stage_groups[sequence_id]:
            thread = threading.Thread(target=execute_stage, args=(stage, config_path))
            threads.append(thread)
            print("Number of threads is ", len(threads))
            thread.start()

        # Wait for all threads in the current group to finish
        for thread in threads:
            thread.join()

def execute_stage(stage, config_path):
    task = stage.find('task')
    function_name = task.find('function').text
    language = task.get('language')
    input_file_path = stage.find('input').text
    output_file_path = stage.find('output').text
    param = [param.text for param in task.findall('param')]
    print("EXECUTING ", function_name)
    try:
        if language == 'java':
            # Compile and run Java file
            logging.info("Compiling and running Java file " + function_name)
            task_library.execute_java_file(function_name, input_file_path, output_file_path, config_path)
        elif language=="shell":
            # Execute shell script
            logging.info("Executing Shell Script " + function_name)
            task_library.execute_shell_script(input_file_path, output_file_path, function_name, param, config_path)
        elif hasattr(udf, function_name):
            print("EXECUTING UDF")
            logging.info('Executing UDF ' + function_name)
            if param:
                print("PARAMS: ", param)
                getattr(udf, function_name)(input_file_path, output_file_path, param, config_path)
            else:
                getattr(udf, function_name)(input_file_path, output_file_path, config_path)
        elif function_name == "join":
            inps = input_file_path.split(",")
            inp1 = inps[0]
            inp2 = inps[1]

            task_library.join(inp1, inp2, output_file_path, param, config_path)
        else:
            if hasattr(task_library, function_name):
                if param:
                    getattr(task_library, function_name)(input_file_path, output_file_path, param, config_path)
                else:
                    getattr(task_library, function_name)(input_file_path, output_file_path, config_path)
    except Exception as e:
        logging.error("Error executing task: " + str(e))