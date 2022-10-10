'''
Created on Jun 2, 2020

@author: patri
'''
import time
from owlready2 import *
from owlready2.namespace import onto_path

'''
Be sure to read the ontology from a file
'''
shamroqOntology = "C:\projects\phd\sekeConf\crc\shamroq.owl"
onto_path.append(shamroqOntology)


def getLeaves(label, subtree):
    leaves = [x[0] for x in subtree.leaves()]
    phrase = " ".join(leaves)
    print (label, phrase)
    time.sleep(0) 
    return phrase


'''
chunkGrammarTree is a "Sentence" Tree tagged with the Grammar Rules
during the classify stage.  This method navigates the tree to model  
'''
def evaluateTree(chunkGrammarTree):
    leaf = ""
    i = 0;
    print("entering evaluateTree")
    for subtree in chunkGrammarTree.subtrees():  
        print(subtree)
        print ("//////////")
        print ("--", i, "--")
        print ("//////////")
        i = i+1
        time.sleep(0)
        '''
        time.sleep(1)            
        if subtree.label() == 'SECTION':
            leaf = getLeaves(subtree.label(), subtree)
        elif subtree.label() == 'Topic':
            leaf = getLeaves(subtree.label(), subtree)
        elif subtree.label() == 'EXCEPTION': 
            leaf = getLeaves(subtree.label(), subtree)
        elif subtree.label() == 'NOUN_PHRASE':
            leaf = getLeaves(subtree.label(), subtree)
        elif subtree.label() == 'VERB_PHRASE':
            leaf = getLeaves(subtree.label(), subtree)
        elif subtree.label() == 'MODALITY':
            leaf = getLeaves(subtree.label(), subtree)
        elif subtree.label() == 'CONJ':
            leaf = getLeaves(subtree.label(), subtree)
        elif subtree.label() == 'CONTINUANCE':
            leaf = getLeaves(subtree.label(), subtree)
        elif subtree.label() == 'ACTION':
            leaf = getLeaves(subtree.label(), subtree)
        elif subtree.label() == 'END_OF_STATEMENT':
            leaf = getLeaves(subtree.label(), subtree)
        else:
            #print("NULL Statement as defined by the ONTOLOGY")
            pass
            
        '''
    print("done... I think!")  
    
      
    return leaf

def evaluateTree2(chunkGrammarTree):
    leaf = ""
    i = 0;
    print("entering evaluateTree2")
    for topTree in chunkGrammarTree:
        for subtree in topTree.subtrees():  
            print(subtree)
            print ("//////////")
            print ("--", i, "--")
            print ("//////////")
            i = i+1

            if subtree.label() == 'SECTION':
                leaf = getLeaves(subtree.label(), subtree)
            elif subtree.label() == 'Topic':
                leaf = getLeaves(subtree.label(), subtree)
            elif subtree.label() == 'EXCEPTION': 
                leaf = getLeaves(subtree.label(), subtree)
            elif subtree.label() == 'NOUN_PHRASE':
                leaf = getLeaves(subtree.label(), subtree)
            elif subtree.label() == 'VERB_PHRASE':
                leaf = getLeaves(subtree.label(), subtree)
            elif subtree.label() == 'MODALITY':
                leaf = getLeaves(subtree.label(), subtree)
            elif subtree.label() == 'CONJ':
                leaf = getLeaves(subtree.label(), subtree)
            elif subtree.label() == 'CONTINUANCE':
                leaf = getLeaves(subtree.label(), subtree)
            elif subtree.label() == 'ACTION':
                leaf = getLeaves(subtree.label(), subtree)
            elif subtree.label() == 'END_OF_STATEMENT':
                leaf = getLeaves(subtree.label(), subtree)
            else:
                #print("NULL Statement as defined by the ONTOLOGY")
                pass
    print("done... I think!")    
    return leaf


def printResults(dictionaryResult):
    print("\n")
    print("Printing Semi-Structured Data of the CFR - as a python dictionary")
    time.sleep(1);
    for key, value in dictionaryResult.items():
        print("Key:", key)       
        for nestedCategory in value:
            print ('   ' + nestedCategory + ' : ', value[nestedCategory])

        
def modelRegulatoryFacts(TreeStructure):
    i = 0;
    '''
    The TreeStructure contains the entire text of 
    the regulations.  the results contain each
    sentence - classified - as a . Each sentence must be modeled
    '''
    for results in TreeStructure:
        evaluateTree(results)  
        print("--------")
        print("--", i, "--")
        print("--------")
        i = i+1
        time.sleep(3)
        print("line 135 of model.py -  in the modelRegulatoryFacts(TreeStructure) method")


def init(metaDataDictionary, classificationResults):
    print("... starting Model")
    
    '''
    -- Given the meta data, create the NEW class and add the
    base set of attributes (properties) to the Regulation
    '''
    print("metaDataDictionary", type(metaDataDictionary))
    print("classificationResults", type(classificationResults))
    modelRegulatoryFacts(classificationResults)