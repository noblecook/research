
import nltk


def getGrammar():
    '''
        note the prepositional phrase is a part 
        of the noun phrase... see if we can define
        a prepositional phrase and add to the end of 
        noun phrase 
        
        The rules that make up a chunk grammar use "tag patterns" 
    '''
    cfgNPGrammar = r"""SECTION: {<\(><DT|CD|NN.*> <\)>}
                       Topic: {<JJ>+<NNS><\.>}
                       EXCEPTION: {<IN><WRB><DT><NN.*>+}
                       NOUN_PHRASE: {<IN>?<DT>?<JJ.*>*<NN.*>+}
                       MODALITY: {<MD>}
                       CONJ: {<CC>}
                       CONTINUANCE: {<\:>}
                       ACTION: {<RB.*>*<VBZ>?<VB.?>*<RB|RBR>?}
                       END_OF_STATEMENT: {<NOUN_PHRASE><\.>}
        """
    return cfgNPGrammar


'''
Note content is a nested dictionary with Metadata, Header, and Body.
Here we only look at the Body structure.  However, we should consider
collecting the Metadata and Header and storing the content.
'''


def extractParseTag(content):
    print("... starting Classify.extractParseTag()")
    newParseTree = []
    stagingList = content["Body"]["content"]
    cfgNPGrammar = getGrammar()
    chunkGrammar = nltk.RegexpParser(cfgNPGrammar)
    '''
     Basic NLP Pipeline processing:
     print("The staging List is broken up into " , len(stagingList), "parts")
     time.sleep(3) 
    '''
    for eachList in stagingList:
        wordTokens = nltk.word_tokenize(eachList)
        posTaggedWords = nltk.pos_tag(wordTokens)
        '''
        --- below we see chunked = chunkGrammar.parse(tagged);
        --- here is where we get the tree structure
        --- at this point in the game, the tree is not 
        --- stored anywhere, but can be accessed via the 
        --- chunked.subtrees() method.. 
        '''
        chunked = chunkGrammar.parse(posTaggedWords);
        newParseTree.append(chunked)
    return newParseTree;


'''
Now we need to consider using Owlready2 0.24
This class takes a python dictionary with three main keys
 (1) Metadata, 
 (2) Header, and 
 (3) Body
then passes the dictionary to the "extract parse tag" method to 
(a) tokenize the words in "content"; (b) add parts of speech tags; (c) group the sentences
into "chunks" commensurate with the grammar.  the aim of chunking is to isolate the 
noun phrases and verbs so that we can classify rights and obligations  
Finally, the ept method returns a python list
'''


def init(content):
    print("... starting Classify()")
    classifyResult = extractParseTag(content)
    return classifyResult


