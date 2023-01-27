import time

import spacy
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


def setRootElement():
    rootElement = etree.Element("LegalRuleML", nsmap={
        'xmlns': xmlnsLRML,
        'ruleml': xmlnsRuleML,
        'xm': xmlnsSchemaDataTypes,
        'xsi': xmlnsSchemaInstance},
        attrib={'file': xmlnsXSDCompact})
    return rootElement


def setPrefix(seed):
    prefixElement = etree.SubElement(seed, "Prefix")
    return prefixElement


def setLegalSources(seed):
    legalSourceElement = etree.SubElement(seed, "LegalSources")
    return legalSourceElement


def setReferences(seed):
    referenceElement = etree.SubElement(seed, "References")
    return referenceElement


def setTimes(seed):
    timesElement = etree.SubElement(seed, "Times")
    return timesElement


def setTemporalCharacteristics(seed):
    temporalCharacteristicsElement = etree.SubElement(seed, "TemporalCharacteristics")
    return temporalCharacteristicsElement


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


def initializeLRML():
    root = setRootElement()
    setPrefix(root)
    lrmlLegalSources = setLegalSources(root)
    lrmlReferences = setReferences(root)
    lrmlTimes = setTimes(root)
    lrmlTemporalCharacteristics = setTemporalCharacteristics(root)
    lrmlAgents = setAgents(root)
    lrmlAuthorities = setAuthorities(root)
    lrmlJurisdictions = setJurisdictions(root)
    lrmlAssociations = setAssociations(root)
    lrmlContext = setContext(root)
    lrmlStatements = setStatements(root)
    # lrmlTree = assemblerElements(root)
    print(etree.tostring(root, pretty_print=True).decode())

    return root


# def init(input, metadata)
def init():
    initializeLRML()


def main():
    init()


if __name__ == '__main__':
    main()

