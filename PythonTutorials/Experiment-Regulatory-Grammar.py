"""
(2) Implementation specifications:
(i) Contingency operations (Addressable). Establish (and implement as needed) procedures that allow facility
access in support of restoration of lost data under the disaster recovery plan and emergency mode operations
plan in the event of an emergency.
(ii) Facility security plan (Addressable). Implement policies and procedures to safeguard the facility and the
equipment therein from unauthorized physical access, tampering, and theft.
(iii) Access control and validation procedures (Addressable). Implement procedures to control and validate a
person's access to facilities based on their role or function, including visitor control, and control of access
to software programs for testing and revision.
(iv) Maintenance records (Addressable). Implement policies and procedures to document repairs and modifications
to the physical components of a facility which are related to security (for example, hardware, walls, doors, and
locks).
(b) Standard: Workstation use. Implement policies and procedures that specify the proper functions to be performed,
the manner in which those functions are to be performed, and the physical attributes of the surroundings of a
specific workstation or class of workstation that can access electronic protected health information.

CC coordinating conjunction
CD cardinal digit
DT determiner
EX existential there (like: “there is” … think of it like “there exists”)
FW foreign word
IN preposition/subordinating conjunction
JJ adjective ‘big’
JJR adjective, comparative ‘bigger’
JJS adjective, superlative ‘biggest’
LS list marker 1)
MD modal could, will
NN noun, singular ‘desk’
NNS noun plural ‘desks’
NNP proper noun, singular ‘Harrison’
NNPS proper noun, plural ‘Americans’
PDT predeterminer ‘all the kids’
POS possessive ending parent’s
PRP personal pronoun I, he, she
PRP$ possessive pronoun my, his, hers
RB adverb very, silently,
RBR adverb, comparative better
RBS adverb, superlative best
RP particle give up
TO, to go ‘to’ the store.
UH interjection, errrrrrrrm
VB verb, base form take
VBD verb, past tense took
VBG verb, gerund/present participle taking
VBN verb, past participle taken
VBP verb, sing. present, non-3d take
VBZ verb, 3rd person sing. present takes
WDT wh-determiner which
WP wh-pronoun who, what
WP$ possessive wh-pronoun whose
WRB wh-abverb where, when

CFG - context free grammar
Definitions
1. Syntax
2. Grammar
3. Phrase Structure
4. Tokenization
5. Chunking (grouping tokens
6. Chinking
7. Parts of Speech Tags


X. Tree Representation
Sentence
Noun Phrase (NP) & Verb Phrase (VP)
NP Det Adj N
VP V PP
PP P NP
NP DET N

>>> from nltk import CFG
>>> grammar = CFG.fromstring(demo_grammar)
>>> print(grammar)
Grammar with 13 productions (start state = S)
    S -> NP VP
    NP -> Det N
    PP -> P NP
    VP -> 'slept'
    VP -> 'saw' NP
    VP -> 'walked' PP
    Det -> 'the'
    Det -> 'a'
    N -> 'man'
    N -> 'park'
    N -> 'dog'
    P -> 'in'
    P -> 'with'
A context-free grammar G is defined by the 4-tuple:[4]

G =(V,Σ,R,S)} where

V is a finite set; each element {\displaystyle v\in V}v\in V is called a nonterminal character or a variable. Each variable represents a different type of phrase or clause in the sentence. Variables are also sometimes called syntactic categories. Each variable defines a sub-language of the language defined by G.
Σ is a finite set of terminals, disjoint from V, which make up the actual content of the sentence. The set of terminals is the alphabet of the language defined by the grammar G.
R is a finite relation from V to {\displaystyle (V\cup \Sigma )^{*}}(V\cup \Sigma )^{*}, where the asterisk represents the Kleene star operation. The members of R are called the (rewrite) rules or productions of the grammar. (also commonly symbolized by a P)
S is the start variable (or start symbol), used to represent the whole sentence (or program). It must be an element of V.

"""
import nltk
import re
from nltk.tokenize import PunktSentenceTokenizer

sampleText = """
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
"""



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


def condFreqDist():
    cfd = nltk.ConditionalFreqDist((genre, word)
        for genre in brown.categories()
            for word in brown.words(categories=genre))

    cfd.plot()


def getPunktSentTokens(raw):
    return PunktSentenceTokenizer(raw);

def getWordTokens(sent):
    return nltk.word_tokenize(sent);

def getLowerCaseWords(tok):
    lowerCaseWords = [w.lower() for w in tok]
    return lowerCaseWords;

def getVocabulary(lcw):
    vocab = sorted(set(lcw));
    return vocab;


'''
 regex metacharacters --->   . ^ $ * + ? { } [ ] \ | ( )
 . (Dot.) matches any character except a newline
 * match 0 or more repetitions 
 ? match 0 or 1 repetitions
 + match 1 or more repetitions 
 
 https://docs.python.org/3/library/re.html#re-syntax
'''
def getRegularExpression(p, s):
    regexp = re.findall(p, s)
    return regexp;

def driver2():
    ''' The goal is to create chunks'''
    txt = sampleText
    customSentTokenizer = getPunktSentTokens(trainingText)
    tokenizedRegs = customSentTokenizer.tokenize(txt)
    print(type(tokenizedRegs))
    time.sleep(100)
    try:
        for regSent in tokenizedRegs:
            word = getWordTokens(regSent)
            tagged = nltk.pos_tag(word)
            for t in tagged:
                print(t);

    except Exception as e:
        print(str(e) + '\n')

"""
---------------------- MAIN()-------------------
"""
   

def driver():
    ''' The goal is to create chunks'''
    txt = sampleText
 
    
    customSentTokenizer = getPunktSentTokens(trainingText)
    tokenizedRegs = customSentTokenizer.tokenize(txt)
    print(type(tokenizedRegs))
    time.sleep(100)
    try:
        for regSent in tokenizedRegs:
            word = getWordTokens(regSent)
            tagged = nltk.pos_tag(word)
           
            """
                https://en.wikipedia.org/wiki/Context-free_grammar
                it really looks like these are all terminals
                so, can you really have defin a grammar in
                this manner.  Recall for a grammar you need
                the following:
                x,
                Y,
                Z. 
            """
            cfgNPGrammar = r"""
                shamroq-CLAUSE: {<NP><VP>}
                shamroq-NP: {<DT>?<JJ>*<CC>?<NN>*}
                shamroq-MODAL: {<MD>?<VB|VBD|VBZ>*}
                shamroq-VP: {<PRP>?<VB|VBD|VBZ>*<RB|RBR>?}
                """;

            cfgNPGrammar2 = r"""
                shamroq-CLAUSE: {<NP><VP>}
                shamroq-NP: {<DT>?<JJ>*<NN>*}
                shamroq-MODALITY: {<MD>?<VB|VBD|VBZ>*}
                """;
            cfgNPGrammar3 = r"""
                shamroq-CLAUSE: {<NP><VP>}
                shamroq-NP: {<DT>?<JJ>*<NN.*>*}
                shamroq-Modality: {<MD><VB.*>*}
                shamroq-Purpose: {<TO><VB.*>?}
                """;
            cfgNPGrammar4 = r"""
                shamroq-CLAUSE: {<NP><VP>}
                shamroq-NP: {<DT>?<JJ>*<NN.*>*}
                shamroq-Modal-with-VERB: {<MD><VB.*>*<CC>?<VB.*>*}
                shamroq-Modal-with-ADVERB: {<MD><RB.*>?<VB.*>}
                shamroq-Purpose: {<TO><VB.*>?}
                """;


            
            
            cfg = nltk.RegexpParser(cfgNPGrammar4);
            result = cfg.parse(tagged);
     
            print(result);
            #result.draw();
        
    except Exception as e:
        print(str(e) + '\n')

        
def main():
    driver();

if __name__ == "__main__": 
    # calling main function 
    main()













    
