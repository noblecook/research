import time
import xmlschema
import spacy
BASE_FILE = "C:/Users/patri/PycharmProjects/research/legalruleml-core-spec-v1.0-os/changeDTD/xsd-schema/compact/"
BASE_FILE_EXAMPLES = "C:/Users/patri/PycharmProjects/research/legalruleml-core-spec-v1.0-os/changeDTD/examples/"
xsdFileExperimentsCompactLRML = "C:/Users/patri/OneDrive/Documents/20 PhD/experiments/lrml-compact.xsd"
xsd = BASE_FILE+"lrml-compact.xsd"
xml1 = BASE_FILE+"instance011.xml"
xmlschema.limits.MAX_MODEL_DEPTH = 1000
from lxml import etree
xmlnsLRML = "http://docs.oasis-open.org/legalruleml/ns/v1.0/"
xmlnsRuleML = "http://ruleml.org/spec"
xmlnsSchemaDataTypes = "http://www.w3.org/2001/XMLSchema-datatypes"
xmlnsSchemaInstance = "http://www.w3.org/2001/XMLSchema-instance"
xmlnsSchemaLocation = "http://docs.oasis-open.org/legalruleml/ns/v1.0/"
xmlnsXSDCompact = "file:/C:/Users/patri/PycharmProjects/research/legalruleml-core-spec-v1.0-os/changeDTD/xsd-schema/compact/lrml-compact.xsd"


def leopard():
    '''
    # Define the regulation
    regulation = "If an operator collects personal information from a child, then it must obtain verifiable parental consent. If an operator uses personal information from a child, then it must obtain verifiable parental consent. If an operator discloses personal information from a child, then it must obtain verifiable parental consent."

    # Process the regulation text with spaCy
    doc = nlp(regulation)

    # Extract the "if" and "then" clauses
    for sent in doc.sents:
        if "if" in sent.text:
            # Create a PrescriptiveCondition element
            prescriptive_condition = etree.SubElement(root, "PrescriptiveCondition")
            # Create a condition element
            condition = etree.SubElement(prescriptive_condition, "condition")
            condition.text = sent.text

        if "then" in sent.text:
            # Create a consequence element
            consequence = etree.SubElement(prescriptive_condition, "consequence")
            consequence.text = sent.text

    def setup():
        # Load the spaCy model
        nlp = spacy.load("en_core_web_sm")
        return nlp
    '''


def setPrefix(seed, redIDValue):
    prefixElement = etree.SubElement(seed, "Prefix")
    prefixElement.set("refID", redIDValue)
    return prefixElement


def setLegalSources(seed, keyValue, sameAsValue):
    legalSourcesPlural = etree.SubElement(seed, "LegalSources")
    legalSourceSingle = etree.SubElement(legalSourcesPlural, "LegalSource")
    legalSourceSingle.set("key", keyValue)
    legalSourceSingle.set("sameAs", sameAsValue)
    return legalSourcesPlural


def setReferences(seed, rtValue, rIDValue, rIDSystemValue):
    referencesPlural = etree.SubElement(seed, "References")
    referencesSingle = etree.SubElement(referencesPlural, "Reference")
    referencesSingle.set("refersTo", rtValue)
    referencesSingle.set("refID", rIDValue)
    referencesSingle.set("refIDSystemName", rIDSystemValue)
    return referencesPlural


def setTimes(seed, timeKeyValue, regTime):
    timesPlural = etree.SubElement(seed, "Times")
    timeSingular = etree.SubElement(timesPlural, "{http://ruleml.org/spec}Time")
    timeSingular.set("key", timeKeyValue)
    data = etree.SubElement(timeSingular, "{http://ruleml.org/spec}Data")
    data.set("{http://www.w3.org/2001/XMLSchema-instance}type", timeKeyValue)
    data.text = regTime
    return timesPlural


def setTemporalCharacteristics(seed, statsValue, developValue, atTimeValue):
    temporalCharacteristicsPlural = etree.SubElement(seed, "TemporalCharacteristics")
    temporalCharacteristic = etree.SubElement(temporalCharacteristicsPlural, "TemporalCharacteristic")
    status = etree.SubElement(temporalCharacteristic, "forStatus")
    status.set("iri", statsValue)
    statusDevelopment = etree.SubElement(temporalCharacteristic, "hasStatusDevelopment")
    statusDevelopment.set("iri", developValue)
    atTime = etree.SubElement(temporalCharacteristic, "atTime")
    atTime.set("keyref", atTimeValue)
    return temporalCharacteristicsPlural


def setAgents(seed):
    agentElement = etree.SubElement(seed, "Agents")
    return agentElement


def setAuthorities(seed):
    authorityElement = etree.SubElement(seed, "Authorities")
    return authorityElement


def setJurisdictions(seed):
    jurisdictionElement = etree.SubElement(seed, "Jurisdictions")
    return jurisdictionElement


def setAssociations(seed):
    associationElement = etree.SubElement(seed, "Associations")
    return associationElement


def setContext(seed):
    contextElement = etree.SubElement(seed, "Context")
    return contextElement


def setStatements(seed):
    statementElement = etree.SubElement(seed, "Statements")
    return statementElement


def validateSchema(lrmlCompactXsd, lrmlCompactXml):
    schema = xmlschema.XMLSchema(lrmlCompactXsd)
    try:
        # Validate the XML file
        schema.validate(lrmlCompactXml)
        print("Valid!!!")
        validBool = True
    except Exception as e:
        validBool = False
        print("|                       |")
        print("|    Invalid Schema     |")
        print("|                       |")
        print(e.reason)
        time.sleep(5)

    return validBool


def generateXMLFile(example, tree):
    # Write the tree to an XML file
    with open(example, "wb") as f:
        f.write(etree.tostring(tree, pretty_print=True))


def setRootElement():
    nice = xmlnsSchemaLocation + " " + xmlnsXSDCompact
    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    rootElement = etree.Element("LegalRuleML", {attr_qname: nice}, nsmap={
        None: xmlnsLRML,
        'ruleml': xmlnsRuleML,
        'xm': xmlnsSchemaDataTypes,
        'xsi': xmlnsSchemaInstance})

    return rootElement

# ToDo:  Set Values in initializeLRML via a "config" file


def initializeLRML():
    example = "example.xml"
    legalKey = "lsref01cfr312.5"
    legalSameAs = "www.patrick.cook.com"
    rt = "lsref02"
    rID = "/us/USCODE/eng@/main#title16-sec312.5"
    rIDSystem = "AkomaNtoso2.0.2012-10"
    timeKeyValue = "xm:dateTime"
    regTime = "1998-10-21T00:00:00"



    root = setRootElement()
    setPrefix(root, "pre100")
    setLegalSources(root, legalKey, legalSameAs)
    setReferences(root, rt, rID, rIDSystem)
    setTimes(root, timeKeyValue, regTime)

    statIRI = "&amp;lrmlv;#Efficacious"
    statsDev = "&amp;lrmlv;#Starts"
    tempAtTime = "#t1"

    setTemporalCharacteristics(root, statIRI, statsDev, tempAtTime)

    statIRI = "&amp;lrmlv;#Efficacious"
    statsDev = "&amp;lrmlv;#End"
    tempAtTime = "#t2"
    setTemporalCharacteristics(root, statIRI, statsDev, tempAtTime)



    setAgents(root)
    setAuthorities(root)
    setJurisdictions(root)
    setAssociations(root)
    setContext(root)
    setStatements(root)
    generateXMLFile(example, root)
    validateSchema(xsd, example)
    validateSchema(xsd, xml1)
    return root


# def init(input, metadata)
def processProvisions(r):
    print(etree.tostring(r, pretty_print=True).decode())


def init():
    regRoot = initializeLRML()
    processProvisions(regRoot)


# ToDo: (1) add the schema validation (2) complete the "Statement" element (3) Process if/then
# ToDo: (4) add the attributes to the other elements (5) Run the end-to-end test

def main():
    init()


if __name__ == '__main__':
    main()

