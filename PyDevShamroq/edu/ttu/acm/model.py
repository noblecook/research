'''
Created on Jun 2, 2020

@author: patri
'''
import time

def getLeaves(label, subtree):
    leaves = [x[0] for x in subtree.leaves()]
    phrase = " ".join(leaves)
    print (label, phrase) 
    return phrase

def evaluateTree(chunkGrammarTree):
    leaf = "";
    counter = 1;
    
    for subtree in chunkGrammarTree.subtrees(): 
        print(counter)
        counter = counter + 1
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
        
    return leaf


def init(classificatonResults):
    print("... starting Model")
    for results in classificatonResults:
        evaluateTree(results)
        
        
        
        
        
          