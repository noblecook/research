import time
import xmlschema
from lxml import etree
from datetime import datetime
from PyDevShamroq.src.edu.ttu.acm import metadata_association_elements


OUTPUT = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/output/"
BASE_FILE = "C:/Users/patri/PycharmProjects/research/legalruleml-core-spec-v1.0-os/changeDTD/xsd-schema/compact/"
BASE_FILE_EXAMPLES = "C:/Users/patri/PycharmProjects/research/legalruleml-core-spec-v1.0-os/changeDTD/examples/"
xmlExampleLRML = "legalRuleML"
xsdFileExperimentsCompactLRML = "C:/Users/patri/OneDrive/Documents/20 PhD/experiments/lrml-compact.xsd"
xsd = BASE_FILE+"lrml-compact.xsd"
xml1 = BASE_FILE+"instance011.xml"
xmlschema.limits.MAX_MODEL_DEPTH = 1000
xmlnsLRML = "http://docs.oasis-open.org/legalruleml/ns/v1.0/"
xmlnsRuleML = "http://ruleml.org/spec"
xmlnsSchemaDataTypes = "http://www.w3.org/2001/XMLSchema-datatypes"
xmlnsSchemaInstance = "http://www.w3.org/2001/XMLSchema-instance"
xmlnsSchemaLocation = "http://docs.oasis-open.org/legalruleml/ns/v1.0/"
xmlnsXSDCompact = "file:/C:/Users/patri/PycharmProjects/research/legalruleml-core-spec-v1.0-os/changeDTD/xsd-schema/compact/lrml-compact.xsd"


def setPrefix(rootOfXML, redIDValue):
    prefixElement = etree.SubElement(rootOfXML, "Prefix")
    prefixElement.set("refID", redIDValue)
    return prefixElement


def setLegalSources(rootOfXML, keyValue, sameAsValue):
    legalSourcesPlural = etree.SubElement(rootOfXML, "LegalSources")
    legalSourceSingle = etree.SubElement(legalSourcesPlural, "LegalSource")
    legalSourceSingle.set("key", keyValue)
    legalSourceSingle.set("sameAs", sameAsValue)
    return legalSourcesPlural


def setReferences(rootOfXML, rtValue, rIDValue, rIDSystemValue):
    referencesPlural = etree.SubElement(rootOfXML, "References")
    referencesSingle = etree.SubElement(referencesPlural, "Reference")
    referencesSingle.set("refersTo", rtValue)
    referencesSingle.set("refID", rIDValue)
    referencesSingle.set("refIDSystemName", rIDSystemValue)
    return referencesPlural


def setTimes(rootOfXML, timeKeyValue, regTime):
    timesPlural = etree.SubElement(rootOfXML, "Times")
    timeSingular = etree.SubElement(timesPlural, "{http://ruleml.org/spec}Time")
    timeSingular.set("key", timeKeyValue)
    data = etree.SubElement(timeSingular, "{http://ruleml.org/spec}Data")
    data.set("{http://www.w3.org/2001/XMLSchema-instance}type", timeKeyValue)
    data.text = regTime
    return timesPlural


def setTemporalCharacteristics(rootOfXML, statsValue, developValue, atTimeValue):
    temporalCharacteristicsPlural = etree.SubElement(rootOfXML, "TemporalCharacteristics")
    temporalCharacteristic = etree.SubElement(temporalCharacteristicsPlural, "TemporalCharacteristic")
    status = etree.SubElement(temporalCharacteristic, "forStatus")
    status.set("iri", statsValue)
    statusDevelopment = etree.SubElement(temporalCharacteristic, "hasStatusDevelopment")
    statusDevelopment.set("iri", developValue)
    atTime = etree.SubElement(temporalCharacteristic, "atTime")
    atTime.set("keyref", atTimeValue)
    return temporalCharacteristicsPlural


def setAgents(rootOfXML, agentKey, agentSameAs):
    agentsPlural = etree.SubElement(rootOfXML, "Agents")
    agent = etree.SubElement(agentsPlural, "Agent")
    agent.set("key", agentKey)
    agent.set("sameAs", agentSameAs)
    return agentsPlural


def setAuthorities(rootOfXML, authKey, authSameAs):
    authorityPlural = etree.SubElement(rootOfXML, "Authorities")
    authority = etree.SubElement(authorityPlural, "Authority")
    authority.set("key", authKey)
    authority.set("sameAs", authSameAs)
    return authorityPlural


def setJurisdictions(rootOfXML, jurKey, jurSameAs):
    jurisdictionPlural = etree.SubElement(rootOfXML, "Jurisdictions")
    jurisdiction = etree.SubElement(jurisdictionPlural, "Jurisdiction")
    jurisdiction.set("key", jurKey)
    jurisdiction.set("sameAs", jurSameAs)
    return jurisdictionPlural


def setAssociationsSource(rootOfXML, assocKey, appSourceValue, keyRefRule):
    associationPlural = etree.SubElement(rootOfXML, "Associations")
    associationPlural.set("key", assocKey)
    association = etree.SubElement(associationPlural, "Association")
    appSource = etree.SubElement(association, "appliesSource")
    appSource.set("keyref", appSourceValue)
    toTarget = etree.SubElement(association, "toTarget")
    toTarget.set("keyref", keyRefRule)
    return associationPlural


def setContext(rootOfXML, contextKey, appAssocKeyRef, appAltKeyRef, inScopeKeyRef):
    contextElement = etree.SubElement(rootOfXML, "Context")
    contextElement.set("key", contextKey)
    appAssociation = etree.SubElement(contextElement, "appliesAssociations")
    appAssociation.set("keyref", appAssocKeyRef)
    appAlternatives = etree.SubElement(contextElement, "appliesAlternatives")
    appAlternatives.set("keyref", appAltKeyRef)
    inScope = etree.SubElement(contextElement, "inScope")
    inScope.set("keyref", inScopeKeyRef)
    return contextElement

# consider passing in a dictionary of key/value pairs vs. 10+ parameters


def setStatements(rootOfXML, overRideOver, overRideUnder, ruleKey, ruleClosure,
                  andKey, atomicKey1, relPredicate, relVar, consequentPredicate,
                  subj, obj):
    statementElement = etree.SubElement(rootOfXML, "Statements")
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

    set_If_Statement(lrmlRule, andKey)
    andKey = "Or"
    set_If_Statement(lrmlRule, andKey)

    andKey = "And"
    set_If_Statement(lrmlRule, andKey)

    set_Then_Statement(lrmlRule, consequentPredicate, subj, obj)

    return statementElement


def set_Then_Statement(parentLrmlRule, consequentPredicate, subj, obj):
    print("set_Then_Statement")
    thenStatement = etree.SubElement(parentLrmlRule, "{http://ruleml.org/spec}then")
    subOrderedList = etree.SubElement(thenStatement, "SuborderList")
    obligation = etree.SubElement(subOrderedList, "Obligation")

    oblAtom = etree.SubElement(obligation, "{http://ruleml.org/spec}Atom")
    oblRel = etree.SubElement(oblAtom, "{http://ruleml.org/spec}Rel")
    oblRel.set("iri", consequentPredicate)

    oblVarSubj = etree.SubElement(oblAtom, "{http://ruleml.org/spec}Var")
    oblVarSubj.text = subj
    oblVarObj = etree.SubElement(oblAtom, "{http://ruleml.org/spec}Var")
    oblVarObj.text = obj

    return thenStatement


def set_If_Statement(parentLrmlRule, andOrValue):
    print("set_If_Statement")
    ifStatement = etree.SubElement(parentLrmlRule, "{http://ruleml.org/spec}if")
    print(andOrValue)
    time.sleep(10)
    if andOrValue == "And":
        andOrKey = etree.SubElement(ifStatement, "{http://ruleml.org/spec}And")
        andOrKey.set("key", ":and1")
    else:
        andOrKey = etree.SubElement(ifStatement, "{http://ruleml.org/spec}Or")
        andOrKey.set("key", ":or1")

    atom = etree.SubElement(andOrKey, "{http://ruleml.org/spec}Atom")
    atom.set("key", ":atom1")

    antecedentRel = etree.SubElement(atom, "{http://ruleml.org/spec}Rel")
    antecedentRel.set("iri", ":operator")

    antecedentVar = etree.SubElement(atom, "{http://ruleml.org/spec}Var")
    antecedentVar.text = "x"

    return ifStatement


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


def generateXMLFile(tree):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    xmlOutput = OUTPUT + xmlExampleLRML + now
    # Write the tree to an XML file
    with open(xmlOutput, "wb") as f:
        f.write(etree.tostring(tree, pretty_print=True))

    return xmlOutput


def setRootElement():
    nice = xmlnsSchemaLocation + " " + xmlnsXSDCompact
    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    rootElement = etree.Element("LegalRuleML", {attr_qname: nice}, nsmap={
        None: xmlnsLRML,
        'ruleml': xmlnsRuleML,
        'xm': xmlnsSchemaDataTypes,
        'xsi': xmlnsSchemaInstance})
    return rootElement


def set_RootElement_with_Namespaces():
    nice = xmlnsSchemaLocation + " " + xmlnsXSDCompact
    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    rootElement = etree.Element("LegalRuleML", {attr_qname: nice}, nsmap={
        None: xmlnsLRML,
        'ruleml': xmlnsRuleML,
        'xm': xmlnsSchemaDataTypes,
        'xsi': xmlnsSchemaInstance})
    return rootElement

# ToDo:  Set Values in initializeLRML via a "config"  (or json) file
# ToDo:  Refactor


def initializeLRML():
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    example = OUTPUT + xmlExampleLRML + now

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
    andKey = "And"
    atomicKey1 = ":atom1"
    realPredicate = ":operator"
    relVar = "x"
    conPred = ":obtain"
    nsubject = "x"
    obj = "y"

    # for multiple parameters like this, use a key/value pair
    setStatements(root, overRideOver, overRideUnder, ruleKey, ruleClosure,
                  andKey, atomicKey1, realPredicate, relVar,
                  conPred, nsubject, obj)

    generateXMLFile(example, root)
    validateSchema(xsd, example)
    validateSchema(xsd, xml1)
    return root


def set_MetaData(rootElement, keyValueAsParams):
    setPrefix(rootElement, "pre100")

    setLegalSources(rootElement, keyValueAsParams['legalSources']['legalKey'],
                    keyValueAsParams['legalSources']['legalSameAs'])
    # setLegalSources(rootElement, legalKey, legalSameAs)

    setReferences(rootElement, keyValueAsParams['references']['rt'],
                  keyValueAsParams['references']['rID'], keyValueAsParams['references']['rIDSystem'])
    # setReferences(rootElement, rt, rID, rIDSystem)

    setTimes(rootElement, keyValueAsParams['times']['timeKeyValue'], keyValueAsParams['times']['regTime'])
    # setTimes(rootElement, timeKeyValue, regTime)

    setTemporalCharacteristics(rootElement, keyValueAsParams['statIRI']['&amp;lrmlv;#Efficacious'],
                               keyValueAsParams['statsDev']['&amp;lrmlv;#Starts'],
                               keyValueAsParams['endingDev']['&amp;lrmlv;#End'],
                               keyValueAsParams['tempAtTime1']['#t1'],
                               keyValueAsParams['tempAtTime2']['#t2'])
    # setTemporalCharacteristics(rootOfXML, statsValue, developValue, atTimeValue)

    setAgents(rootElement, keyValueAsParams['agentKey']['aut1'], keyValueAsParams['agentSameAs']['Richard Bryan (D-NV)'])
    # setAgents(rootElement, agentKey, agentSameAs)

    setAuthorities(rootElement, keyValueAsParams['authoritiesKey']['Senate'],
                   keyValueAsParams['authoritiesSameAs']['https://www.senate.gov/'])
    # setAuthorities(rootElement, authKey, authSameAs)

    setJurisdictions(rootElement, keyValueAsParams['jKey']['US'], keyValueAsParams['jSameAs']['https://www.whitehouse.gov/'])
    # setJurisdictions(rootElement, jKey, jSameAs)


def set_Associations(rootElement, keyValueAsParams):
    assocKey = "assoc01"
    appSourceValue = "#lsref01.cfr312.5"
    keyRefRule = "#rule1"
    setAssociationsSource(rootElement, keyValueAsParams['a']['ab'], keyValueAsParams['a']['ab'],
                          keyValueAsParams['a']['ab'])
    setAssociationsSource(rootElement, assocKey, appSourceValue, keyRefRule)


def set_Statements_Related_Elements(rootElement, keyValueAsParams):
    setContext(rootElement, keyValueAsParams['a']['ab'], keyValueAsParams['a']['ab'],
               keyValueAsParams['a']['ab'], keyValueAsParams['a']['ab'])
    setContext(rootElement, contextKey, appAssocKeyRef, appAltKeyRef, inScopeKeyRef)

    # for multiple parameters like this, use a key/value pair
    setStatements(rootElement, keyValueAsParams['a']['ab'], keyValueAsParams['a']['ab'],
                  keyValueAsParams['a']['ab'], keyValueAsParams['a']['ab'],
                  keyValueAsParams['a']['ab'], keyValueAsParams['a']['ab'],
                  keyValueAsParams['a']['ab'], keyValueAsParams['a']['ab'],
                  keyValueAsParams['a']['ab'], keyValueAsParams['a']['ab'],
                  keyValueAsParams['a']['ab'])

    setStatements(rootElement, overRideOver, overRideUnder, ruleKey, ruleClosure,
                  andKey, atomicKey1, realPredicate, relVar,
                  conPred, nsubject, obj)


def setLegalRuleML(conditional_params):
    root = set_RootElement_with_Namespaces()

    metadata = metadata_association_elements.getMetaData()
    set_MetaData(root, metadata)

    associations = metadata_association_elements.getAssociations()
    set_Associations(root, associations)

    statements = conditional_params
    set_Statements_Related_Elements(statements)

    output = generateXMLFile(root)
    validateSchema(xsd, output)
    validateSchema(xsd, xml1)
    return root


# pass the json element here in initializeLRML()
def getDictValue():
    dict_LRML_ELEMENTS = {}
    dict_Legal_Sources = {}
    dict_References = {}
    dict_Times = {}
    dict_Temporal_Chars = {}
    dict_Agents = {}
    dict_Authorities = {}
    dict_Jurisdictions = {}
    dict_Association_Source = {}
    dict_Context = {}
    dict_Statements = {}

    legalKey = "lsref01cfr312.5"
    legalSameAs = "www.patrick.cook.com"
    rt = "lsref02"
    rID = "/us/USCODE/eng@/main#title16-sec312.5"
    rIDSystem = "AkomaNtoso2.0.2012-10"
    timeKeyValue = "xm:dateTime"
    regTime = "1998-10-21T00:00:00"
    dictKeyValues = {}
    if dictKeyValues != None:
        loadDictionary()
    else:
        dictKeyValues['x'] = "y"


def init(input_dict_conditional_params):
    # metadata = getMetaData()
    # associations = getAssociations()
    # statements = getStatements(input_dict_conditional_params)
    setLegalRuleML(input_dict_conditional_params)
    # regRoot = initializeLRML()
    # regDict = getDictValue(iFile)

    print(etree.tostring(regRoot, pretty_print=True).decode())


# ToDo: (3) Process if/then
# ToDo: (4) add the attributes to the other elements (5) Run the end-to-end test
# ToDo: (5) the input consist of three things:  (a) a config; (b) metadata (3) the provision



