import spacy


def setRootElement():
    nice = xmlnsSchemaLocation + " " + xmlnsXSDCompact
    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    rootElement = etree.Element("LegalRuleML", {attr_qname: nice}, nsmap={
        None: xmlnsLRML,
        'ruleml': xmlnsRuleML,
        'xm': xmlnsSchemaDataTypes,
        'xsi': xmlnsSchemaInstance})
    return rootElement



def setIfAndElement(rootElement):
    ifStatement = etree.SubElement(lrmlRule, "{http://ruleml.org/spec}if")
    conjAnd = etree.SubElement(ifStatement, "{http://ruleml.org/spec}And")
    conjAnd.set("key", andKey)

    atom = etree.SubElement(conjAnd, "{http://ruleml.org/spec}Atom")
    atom.set("key", atomicKey1)

    antecedentRel = etree.SubElement(atom, "{http://ruleml.org/spec}Rel")
    antecedentRel.set("iri", relPredicate)

    antecedentVar = etree.SubElement(atom, "{http://ruleml.org/spec}Var")
    antecedentVar.text = relVar

def init():
    nlp = spacy.load("en_core_web_lg")
    test = "Hello World"
    doc = nlp(test)

    print(doc)

if __name__ == '__main__':
    init()
