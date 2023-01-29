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


def setAgents(seed, agentKey, agentSameAs):
    agentsPlural = etree.SubElement(seed, "Agents")
    agent = etree.SubElement(agentsPlural, "Agent")
    agent.set("key", agentKey)
    agent.set("sameAs", agentSameAs)
    return agentsPlural


def setAuthorities(seed, authKey, authSameAs):
    authorityPlural = etree.SubElement(seed, "Authorities")
    authority = etree.SubElement(authorityPlural, "Authority")
    authority.set("key", authKey)
    authority.set("sameAs", authSameAs)
    return authorityPlural


def setJurisdictions(seed, jurKey, jurSameAs):
    jurisdictionPlural = etree.SubElement(seed, "Jurisdictions")
    jurisdiction = etree.SubElement(jurisdictionPlural, "Jurisdiction")
    jurisdiction.set("key", jurKey)
    jurisdiction.set("sameAs", jurSameAs)
    return jurisdictionPlural


def setAssociationsSource(seed, assocKey, appSourceValue, keyRefRule):
    associationPlural = etree.SubElement(seed, "Associations")
    associationPlural.set("key", assocKey)
    association = etree.SubElement(associationPlural, "Association")
    appSource = etree.SubElement(association, "appliesSource")
    appSource.set("keyref", appSourceValue)
    toTarget = etree.SubElement(association, "toTarget")
    toTarget.set("keyref", keyRefRule)
    return associationPlural


def setContext(seed, contextKey, appAssocKeyRef, appAltKeyRef, inScopeKeyRef):
    contextElement = etree.SubElement(seed, "Context")
    contextElement.set("key", contextKey)
    appAssociation = etree.SubElement(contextElement, "appliesAssociations")
    appAssociation.set("keyref", appAssocKeyRef)
    appAlternatives = etree.SubElement(contextElement, "appliesAlternatives")
    appAlternatives.set("keyref", appAltKeyRef)
    inScope = etree.SubElement(contextElement, "inScope")
    inScope.set("keyref", inScopeKeyRef)
    return contextElement

# consider passing in a dictionary of key/value pairs vs. 10+ parameters


def setStatements(seed, overRideOver, overRideUnder, ruleKey, ruleClosure,
                  andKey, atomicKey1, relPredicate, relVar, consequentPredicate,
                  subj, obj):
    statementElement = etree.SubElement(seed, "Statements")
    hasQualification = etree.SubElement(statementElement, "hasQualification")
    overRide = etree.SubElement(hasQualification, "Override")
    overRide.set("over", overRideOver)
    overRide.set("under", overRideUnder)

    prescriptiveStmt = etree.SubElement(statementElement, "PrescriptiveStatement")
    lrmlRule = etree.SubElement(prescriptiveStmt, "{http://ruleml.org/spec}Rule")
    lrmlRule.set("key", ruleKey)
    lrmlRule.set("closure", ruleClosure)

    '''
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,,,,,,,,,,,
    '''
    #  Two things:
    #  (1) Create a dictionary for the parameters
    #  (2) Create Methods for each element under the Rule
    '''
    &&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&,,,,,,,,,,,
    '''

    strength = etree.SubElement(lrmlRule, "hasStrength")
    etree.SubElement(strength, "DefeasibleStrength")

    lrmlRule.append(etree.Comment("##########################"))
    lrmlRule.append(etree.Comment("The Conditional Statements"))
    lrmlRule.append(etree.Comment("##########################"))

    ifStatement = etree.SubElement(lrmlRule, "{http://ruleml.org/spec}if")
    conjAnd = etree.SubElement(ifStatement, "{http://ruleml.org/spec}And")
    conjAnd.set("key", andKey)

    atom = etree.SubElement(conjAnd, "{http://ruleml.org/spec}Atom")
    atom.set("key", atomicKey1)

    antecedentRel = etree.SubElement(atom, "{http://ruleml.org/spec}Rel")
    antecedentRel.set("iri", relPredicate)

    antecedentVar = etree.SubElement(atom, "{http://ruleml.org/spec}Var")
    antecedentVar.text = relVar

    thenStatement = etree.SubElement(lrmlRule, "{http://ruleml.org/spec}then")
    subOrderedList = etree.SubElement(thenStatement, "SuborderList")
    obligation = etree.SubElement(subOrderedList, "Obligation")
    oblAtom = etree.SubElement(obligation, "{http://ruleml.org/spec}Atom")

    oblRel = etree.SubElement(oblAtom, "{http://ruleml.org/spec}Rel")
    oblRel.set("iri", consequentPredicate)
    oblVarSubj = etree.SubElement(oblAtom, "{http://ruleml.org/spec}Var")
    oblVarSubj.text = subj
    oblVarObj = etree.SubElement(oblAtom, "{http://ruleml.org/spec}Var")
    oblVarObj.text = obj
    return statementElement


def validateSchema(lrmlCompactXsd, lrmlCompactXml):
    schema = xmlschema.XMLSchema(lrmlCompactXsd)
    try:
        # Validate the XML file
        schema.validate(lrmlCompactXml)
        print("Valid!!!")
        time.sleep(3)
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
# ToDo:  Refactor


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

    agentKey = "aut1"
    agentSameAs = "Richard Bryan (D-NV)"
    setAgents(root, agentKey, agentSameAs)

    authKey = "Senate"
    authSameAs = "https://www.senate.gov/"

    setAuthorities(root, authKey, authSameAs)

    jKey = "US"
    jSameAs = "https://www.whitehouse.gov/"

    setJurisdictions(root, jKey, jSameAs)

    assocKey = "assoc01"
    appSourceValue = "#lsref01.cfr312.5"
    keyRefRule = "#rule1"

    setAssociationsSource(root, assocKey, appSourceValue, keyRefRule)

    contextKey = "Context1"
    appAssocKeyRef = "#assoc1"
    appAltKeyRef = "#alt2"
    inScopeKeyRef = "#ps1"

    setContext(root, contextKey, appAssocKeyRef, appAltKeyRef, inScopeKeyRef)

    ruleKey = ":rule1"
    ruleClosure = "universal"
    overRideOver = "#ps2"
    overRideUnder = "#ps1"
    andKey = ":and1"
    atomicKey1 = ":atom1"
    realPredicate = ":operator"
    relVar = "x"
    conPred = ":obtain"
    nsubject = "x"
    obj = "y"

    setStatements(root, overRideOver, overRideUnder, ruleKey, ruleClosure,
                  andKey, atomicKey1, realPredicate, relVar,
                  conPred, nsubject, obj)



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


# ToDo: (3) Process if/then
# ToDo: (4) add the attributes to the other elements (5) Run the end-to-end test
# ToDo: (5) the input consist of three things:  (a) a config; (b) metadata (3) the provision

def main():
    init()


if __name__ == '__main__':
    main()

