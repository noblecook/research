
import nltk
import time
from nltk.tokenize import PunktSentenceTokenizer
from nltk.corpus import stopwords

trainingText = """
A covered entity may use or disclose protected health information, provided that the individual is
informed in advance of the use or disclosure and has the opportunity to agree to or prohibit or
restrict the use or disclosure, in accordance with the applicable requirements of this section. The
covered entity may orally inform the individual of and obtain the individual's oral agreement or
objection to a use or disclosure permitted by this section.
(a) Standard: Use and disclosure for facility directories—(1) Permitted uses and disclosure. Except
when an objection is expressed in accordance with paragraphs (a)(2) or (3) of this section, a covered
health care provider may:
(i) Use the following protected health information to maintain a directory of individuals in its facility:
(A) The individual's name;
(B) The individual's location in the covered health care provider's facility;
(C) The individual's condition described in general terms that does not communicate specific medical
information about the individual; and
(D) The individual's religious affiliation; and
(ii) Use or disclose for directory purposes such information:
(A) To members of the clergy; or
(B) Except for religious affiliation, to other persons who ask for the individual by name.
(2) Opportunity to object. A covered health care provider must inform an individual of the protected
health information that it may include in a directory and the persons to whom it may disclose such
information (including disclosures to clergy of information regarding religious affiliation) and provide
the individual with the opportunity to restrict or prohibit some or all of the uses or disclosures permitted by paragraph (a)(1) of this section.
(3) Emergency circumstances. (i) If the opportunity to object to uses or disclosures required by paragraph (a)(2) of this section cannot practicably be provided because of the individual's incapacity or an emergency treatment circumstance, a covered health care provider may use or disclose some or all of the protected health information permitted by paragraph (a)(1) of this section for the facility's directory, if such disclosure is:
(A) Consistent with a prior expressed preference of the individual, if any, that is known to the covered health care provider; and
(B) In the individual's best interest as determined by the covered health care provider, in the exercise of professional judgment.
(ii) The covered health care provider must inform the individual and provide an opportunity to object to uses or disclosures for directory purposes as required by paragraph (a)(2) of this section when it becomes practicable to do so.
(b) Standard: Uses and disclosures for involvement in the individual's care and notification purposes—(1) Permitted uses and disclosures. (i) A covered entity may, in accordance with paragraphs (b)(2), (b)(3), or (b)(5) of this section, disclose to a family member, other relative, or a close personal friend of the individual, or any other person identified by the individual, the protected health information directly relevant to such person's involvement with the individual's health care or payment related to the individual's health care.
(ii) A covered entity may use or disclose protected health information to notify, or assist in the notification of (including identifying or locating), a family member, a personal representative of the individual, or another person responsible for the care of the individual of the individual's location, general condition, or death. Any such use or disclosure of protected health information for such notification purposes must be in accordance with paragraphs (b)(2), (b)(3), (b)(4), or (b)(5) of this section, as applicable.
(2) Uses and disclosures with the individual present. If the individual is present for, or otherwise available prior to, a use or disclosure permitted by paragraph (b)(1) of this section and has the capacity to make health care decisions, the covered entity may use or disclose the protected health information if it:
(i) Obtains the individual's agreement;
(ii) Provides the individual with the opportunity to object to the disclosure, and the individual does not express an objection; or
(iii) Reasonably infers from the circumstances, based on the exercise of professional judgment, that the individual does not object to the disclosure.
(3) Limited uses and disclosures when the individual is not present. If the individual is not present, or the opportunity to agree or object to the use or disclosure cannot practicably be provided because of the individual's incapacity or an emergency circumstance, the covered entity may, in the exercise of professional judgment, determine whether the disclosure is in the best interests of the individual and, if so, disclose only the protected health information that is directly relevant to the person's involvement with the individual's care or payment related to the individual's health care or needed for notification purposes. A covered entity may use professional judgment and its experience with common practice to make reasonable inferences of the individual's best interest in allowing a person to act on behalf of the individual to pick up filled prescriptions, medical supplies, X-rays, or other similar forms of protected health information.
(4) Uses and disclosures for disaster relief purposes. A covered entity may use or disclose protected health information to a public or private entity authorized by law or by its charter to assist in disaster relief efforts, for the purpose of coordinating with such entities the uses or disclosures permitted by paragraph (b)(1)(ii) of this section. The requirements in paragraphs (b)(2), (b)(3), or (b)(5) of this section apply to such uses and disclosures to the extent that the covered entity, in the exercise of professional judgment, determines that the requirements do not interfere with the ability to respond to the emergency circumstances.
(5) Uses and disclosures when the individual is deceased. If the individual is deceased, a covered entity may disclose to a family member, or other persons identified in paragraph (b)(1) of this section who were involved in the individual's care or payment for health care prior to the individual's death, protected health information of the individual that is relevant to such person's involvement, unless doing so is inconsistent with any prior expressed preference of the individual that is known to the covered entity.
"""
            

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
        """;
    return cfgNPGrammar


def getContextFreeGrammar():
    '''
        note the prepositional phrase is a part 
        of the noun phrase... see if we can define
        a prepositional phrase and add to the end of 
        noun phrase 
        
        The rules that make up a chunk grammar use "tag patterns" 
    '''
    cfgNPGrammar = nltk.CFG.fromstring("""
                        S-> NP VP
                        VP -> V N
                        V -> "use" | "disclose"
                        NP -> "A covered entity"
                        N -> "information" 
                        """);
    return cfgNPGrammar


def removeStopWords(tokenziedWordsInput):
    stop_words = set(stopwords.words('english'))
    print (stop_words)
    time.sleep(5)
    wordsMinusStopWords = []
    for w in tokenziedWordsInput:
        if w not in stop_words:
            wordsMinusStopWords.append(w);
    return wordsMinusStopWords

'''
Note content is a nested dictionary with Metadata, Header, and Body.
Here is only look at the Body structure.  However, we should consider
collecting the Metadata and Header and storing the content.

'''
def extractParseTag(content):
    print("... starting Classify.extractParseTag()")
    newParseTree = [];
    stagingList = content["Body"]["content"]
    cfgNPGrammar = getGrammar() 
    chunckGrammar = nltk.RegexpParser(cfgNPGrammar);
    
    
    '''
     Basic NLP Pipeline processing:
     print("The staging List is broken up into " , len(stagingList), "parts")
     time.sleep(3) 
    '''
    for eachList in stagingList:  
        wordTokens = nltk.word_tokenize(eachList) 
        #tokensWithoutStopWords = removeStopWords(wordTokens)
        #posTaggedWords = nltk.pos_tag(tokensWithoutStopWords)
        posTaggedWords = nltk.pos_tag(wordTokens)
        '''
        --- below we see chunked = chunckGrammar.parse(tagged);
        --- here is where we get the tree structure
        --- at this point in the game, the tree is not 
        --- stored anywhere, but can be accessed via the 
        --- chunked.subtrees() method.. 
        '''
        chunked = chunckGrammar.parse(posTaggedWords);
        newParseTree.append(chunked)
    return newParseTree;


'''
Now we need to consider using Owlready2 0.24
'''
def init(content):
    print("... starting Classify()")
    classifyResult = extractParseTag(content)
    return classifyResult


