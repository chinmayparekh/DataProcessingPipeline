from lxml import etree

def validate_xml(xml_path, xsd_path):
    # Parse the XML Schema
    schema_root = etree.parse(xsd_path)
    schema = etree.XMLSchema(schema_root)

    # Parse the XML file
    xml_root = etree.parse(xml_path)

    # Validate the XML file against the schema
    result = schema.validate(xml_root)

    # Print the result
    if result:
        print("The XML file is valid.")
    else:
        print("The XML file is invalid.")
        print(schema.error_log)

# Validate the XML file
validate_xml("process1.xml", "pipeline.xsd")