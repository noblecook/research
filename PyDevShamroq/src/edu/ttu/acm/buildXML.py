import xml.etree.ElementTree as ET
import xmlschema

BASE_FILE = "C:/Users/patri/PycharmProjects/research/legalruleml-core-spec-v1.0-os/changeDTD/xsd-schema/compact/"
xsdFileLRML = BASE_FILE + "lrml-compact.xsd"
instance = BASE_FILE + "lrml-compact.xsd"


def validateXML(xmlInstance, xsdFile):
    xmlschema.limits.MAX_MODEL_DEPTH = 1000
    schema = xmlschema.XMLSchema(xsdFile)
    return schema.is_valid(xmlInstance)


def init():   xmlDoc = ET.Element("root")
    legalRuleML = ET.SubElement(xmlDoc,"LegalRuleML")
    print(legalRuleML)


def main():
    init()
    print("Hello World!")

