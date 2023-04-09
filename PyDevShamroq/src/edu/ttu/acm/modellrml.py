import time
import xmlschema
import pprint
from lxml import etree
from datetime import datetime
from PyDevShamroq.src.edu.ttu.acm import metadata_association_elements


OUTPUT = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/output/"
BASE_FILE = "C:/Users/patri/PycharmProjects/research/legalruleml-core-spec-v1.0-os/changeDTD/xsd-schema/compact/"
BASE_FILE_EXAMPLES = "C:/Users/patri/PycharmProjects/research/legalruleml-core-spec-v1.0-os/changeDTD/examples/"
xmlExampleLRML = "LegalRuleML_"
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


def setTemporalCharacteristics(rootOfXML, statsDev, developValue, atTimeValue):
    temporalCharacteristicsPlural = etree.SubElement(rootOfXML, "TemporalCharacteristics")
    temporalCharacteristic = etree.SubElement(temporalCharacteristicsPlural, "TemporalCharacteristic")
    status = etree.SubElement(temporalCharacteristic, "forStatus")
    status.set("iri", statsDev)
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

    andKey = "And"
    set_If_Statement(lrmlRule, andKey)
    set_Then_Statement(lrmlRule, consequentPredicate, subj, obj)

    return statementElement


def set_Then_Statement(parentLrmlRule, consequentPredicate, subj, obj):

    thenStatement = etree.SubElement(parentLrmlRule, "{http://ruleml.org/spec}then")
    subOrderedList = etree.SubElement(thenStatement, "SuborderList")
    obligation = etree.SubElement(subOrderedList, "Obligation")

    oblAtom = etree.SubElement(obligation, "{http://ruleml.org/spec}Atom")
    oblRel = etree.SubElement(oblAtom, "{http://ruleml.org/spec}Rel")
    # oblRel.set("iri", consequentPredicate)
    oblRel.set("iri", ":HelloWorld")

    oblVarSubj = etree.SubElement(oblAtom, "{http://ruleml.org/spec}Var")
    oblVarSubj.text = subj
    oblVarObj = etree.SubElement(oblAtom, "{http://ruleml.org/spec}Var")
    oblVarObj.text = obj

    return thenStatement


def set_If_Statement(parentLrmlRule, andOrValue):

    ifStatement = etree.SubElement(parentLrmlRule, "{http://ruleml.org/spec}if")
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
    antecedentVar.text = "900x"

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
    ext =".xml"
    xmlOutput = OUTPUT + xmlExampleLRML + now + ext
    # Write the tree to an XML file
    with open(xmlOutput, "wb") as f:
        f.write(etree.tostring(tree, pretty_print=True))

    return xmlOutput


def set_RootElement_with_Namespaces():
    nice = xmlnsSchemaLocation + " " + xmlnsXSDCompact
    attr_qname = etree.QName("http://www.w3.org/2001/XMLSchema-instance", "schemaLocation")
    rootElement = etree.Element("LegalRuleML", {attr_qname: nice}, nsmap={
        None: xmlnsLRML,
        'ruleml': xmlnsRuleML,
        'xm': xmlnsSchemaDataTypes,
        'xsi': xmlnsSchemaInstance})
    return rootElement


def set_MetaData(rootElement, keyValueAsParams):
    setPrefix(rootElement, "pre100")

    setLegalSources(rootElement,
                    keyValueAsParams['legalSources']['legalKey'],
                    keyValueAsParams['legalSources']['legalSameAs'])

    setReferences(rootElement,
                  keyValueAsParams['references']['rt'],
                  keyValueAsParams['references']['rID'],
                  keyValueAsParams['references']['rIDSystem'])

    setTimes(rootElement,
             keyValueAsParams['times']['timeKeyValue'],
             keyValueAsParams['times']['regTime'])

    setTemporalCharacteristics(rootElement,
                               keyValueAsParams['temporalCharacter']['statsDev'],
                               keyValueAsParams['temporalCharacter']['endingDev'],
                               keyValueAsParams['temporalCharacter']['tempAtTime1'])
    setAgents(rootElement,
              keyValueAsParams['agent']['agentKey'],
              keyValueAsParams['agent']['agentSameAs'])

    setAuthorities(rootElement,
                   keyValueAsParams['authorities']['authoritiesKey'],
                   keyValueAsParams['authorities']['authoritiesSameAs'])

    setJurisdictions(rootElement,
                     keyValueAsParams['jurisdiction']['jKey'],
                     keyValueAsParams['jurisdiction']['jSameAs'])


def set_Associations(rootElement, keyValueAsParams):
    setAssociationsSource(rootElement,
                          keyValueAsParams['assocSource']['assocKey'],
                          keyValueAsParams['assocSource']['appSourceValue'],
                          keyValueAsParams['assocSource']['keyRefRule'])


def set_Statements_Related_Elements(rootElement, stmtKVP):
    context = metadata_association_elements.getContextMetaData()
    stmtMetadata = metadata_association_elements.getStatementMetaData()

    setContext(rootElement, context['context']['contextKey'], context['context']['appAssocKeyRef'],
               context['context']['appAltKeyRef'], context['context']['inScopeKeyRef'])

    # for multiple parameters like this, use a key/value pair
    setStatements(rootElement,
                  stmtMetadata['properties']['overRideOver'], stmtMetadata['properties']['overRideUnder'],
                  stmtMetadata['properties']['ruleKey'], stmtMetadata['properties']['ruleClosure'],
                  stmtMetadata['properties']['andKey'], stmtMetadata['properties']['atomicKey1'],
                  stmtMetadata['antecedent']['subject'],
                  stmtMetadata['antecedent']['predicate'],  # relVar maps to "x" (maybe enumerated x1, x2, ..., xn)
                  stmtMetadata['antecedent']['dobj'],  # conPred maps to "ROOT"
                  stmtMetadata['consequent']['subject'],  # nsubject maps to x
                  stmtMetadata['consequent']['root'])  # obj maps to x


def setLegalRuleML(metadata, assoc, stmts):
    # root should be done dynamically
    root = set_RootElement_with_Namespaces()
    set_MetaData(root, metadata)
    set_Associations(root, assoc)
    set_Statements_Related_Elements(root, stmts)
    return root


def init(input_dict_conditional_params):
    # Todo: The input is a list of dictionaries.  Iterate, take out
    # Todo: ... the dictionaries and create each provision in a loop

    metadata = metadata_association_elements.getMetaData()
    associations = metadata_association_elements.getAssociations()
    statements = input_dict_conditional_params
    regRoot = setLegalRuleML(metadata, associations, statements)
    output = generateXMLFile(regRoot)
    validateSchema(xsd, output)
    validateSchema(xsd, xml1)
    print(etree.tostring(regRoot, pretty_print=True).decode())

