

def getMetaData():
    metadata = {
        'legalSources': {
            'legalKey': "lsref01cfr312.5",
            'legalSameAs': "www.patrick.cook.com",
        },
        'references': {
            'rt': "lsref02",
            'rID': "/us/USCODE/eng@/main#title16-sec312.5",
            'rIDSystem': "AkomaNtoso2.0.2012-10"
        },
        'times': {
            'timeKeyValue': "xm:dateTime",
            'regTime': "1998-10-21T00:00:00"
        },
        'temporalCharacter': {
            'statIRI': "&amp;lrmlv;#Efficacious",
            'statsDev': "&amp;lrmlv;#Starts",
            'endingDev': "&amp;lrmlv;#End",
            'tempAtTime1': "#t1",
            'tempAtTime2': "#t2"
        },
        'agent': {
            'agentKey': "aut1",
            'agentSameAs': "Richard Bryan (D-NV)"
        },
        'authorities': {
            'authoritiesKey': "Senate",
            'authoritiesSameAs': "https://www.senate.gov/"
        },
        'jurisdiction': {
            'jKey': "US",
            'jSameAs': "https://www.whitehouse.gov/"
        }
    }
    return metadata


def getAssociations():
    metadata = {
        'assocSource': {
            'assocKey': "assoc01",
            'appSourceValue': "#lsref01.cfr312.5",
            'keyRefRule': "#rule1"
        },
        'context': {
            'contextKey': "Context1",
            'appAssocKeyRef': "#assoc1",
            'appAltKeyRef': "#alt2",
            'inScopeKeyRef': "#ps1"
        }
    }
    return metadata


def getContextMetaData():
    metadata = {
        'context': {
            'contextKey': "Context1",
            'appAssocKeyRef': "#assoc1",
            'appAltKeyRef': "#alt2",
            'inScopeKeyRef': "#ps1"
        }
    }
    return metadata


def getStatementMetaData():
    ruleList = {
        'properties': {
            'legalProvision': ':rule1',
            'section': "#assoc1",
            'ruleKey': ':rule1',
            'ruleClosure': 'universal',
            'overRideOver': '#ps2',
            'overRideUnder': '#ps1',
            'andKey': 'And',
            'atomicKey1': ':atom1'
        },
        'antecedent': {
            'dobj': 'x',
            'pObj': 'from children',
            'predicate': 'collects',
            'subject': 'an operator'
        },
        'consequent': {
            'dobj': 'verifiable parental consent',
            'modality': 'must',
            'root': 'obtain',
            'subject': 'they'
        }

    }
    return ruleList



