"""
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


"""
import nltk
import re
from nltk.tokenize import PunktSentenceTokenizer

oneLiner = """
A covered entity or business associate must review and modify the security measures implemented under this subpart as needed to continue provision of reasonable and appropriate protection of electronic protected health information, and update documentation of such security measures in accordance with § 164.316(b)(2)(iii).
"""

smallSample = """
A covered entity or business associate must, in accordance with § 164.306:
(a)(1) Standard: Facility access controls. Implement policies and procedures to limit physical access to its electronic information systems and the facility or facilities in which they are housed, while ensuring that properly authorized access is allowed.
(2) Implementation specifications:
(i) Contingency operations (Addressable). Establish (and implement as needed) procedures that allow facility access in support of restoration of lost data under the disaster recovery plan and emergency mode operations plan in the event of an emergency.
(ii) Facility security plan (Addressable). Implement policies and procedures to safeguard the facility and the equipment therein from unauthorized physical access, tampering, and theft.
"""
sampleText = """
A covered entity or business associate must, in accordance with § 164.306:
(a)(1) Standard: Facility access controls. Implement policies and procedures to limit physical access to its electronic information systems and the facility or facilities in which they are housed, while ensuring that properly authorized access is allowed.
(2) Implementation specifications:
(i) Contingency operations (Addressable). Establish (and implement as needed) procedures that allow facility access in support of restoration of lost data under the disaster recovery plan and emergency mode operations plan in the event of an emergency.
(ii) Facility security plan (Addressable). Implement policies and procedures to safeguard the facility and the equipment therein from unauthorized physical access, tampering, and theft.
(iii) Access control and validation procedures (Addressable). Implement procedures to control and validate a person's access to facilities based on their role or function, including visitor control, and control of access to software programs for testing and revision.
(iv) Maintenance records (Addressable). Implement policies and procedures to document repairs and modifications to the physical components of a facility which are related to security (for example, hardware, walls, doors, and locks).
(b) Standard: Workstation use. Implement policies and procedures that specify the proper functions to be performed, the manner in which those functions are to be performed, and the physical attributes of the surroundings of a specific workstation or class of workstation that can access electronic protected health information.
(c) Standard: Workstation security. Implement physical safeguards for all workstations that access electronic protected health information, to restrict access to authorized users.
(d)(1) Standard: Device and media controls. Implement policies and procedures that govern the receipt and removal of hardware and electronic media that contain electronic protected health information into and out of a facility, and the movement of these items within the facility.
(2) Implementation specifications: 
(i) Disposal (Required). Implement policies and procedures to address the final disposition of electronic protected health information, and/or the hardware or electronic media on which it is stored.
(ii) Media re-use (Required). Implement procedures for removal of electronic protected health information from electronic media before the media are made available for re-use.
(iii) Accountability (Addressable). Maintain a record of the movements of hardware and electronic media and any person responsible therefore.
(iv) Data backup and storage (Addressable). Create a retrievable, exact copy of electronic protected health information, when needed, before movement of equipment.
"""

trainingText = """
(a) General requirements. Covered entities and business associates must do the following:
(1) Ensure the confidentiality, integrity, and availability of all electronic protected health information the covered entity or business associate creates, receives, maintains, or transmits.
(2) Protect against any reasonably anticipated threats or hazards to the security or integrity of such information.
(3) Protect against any reasonably anticipated uses or disclosures of such information that are not permitted or required under subpart E of this part.
(4) Ensure compliance with this subpart by its workforce.
(b) Flexibility of approach. (1) Covered entities and business associates may use any security measures that allow the covered entity or business associate to reasonably and appropriately implement the standards and implementation specifications as specified in this subpart.
(2) In deciding which security measures to use, a covered entity or business associate must take into account the following factors:
(i) The size, complexity, and capabilities of the covered entity or business associate.
(ii) The covered entity's or the business associate's technical infrastructure, hardware, and software security capabilities.
(iii) The costs of security measures.
(iv) The probability and criticality of potential risks to electronic protected health information.
(c) Standards. A covered entity or business associate must comply with the applicable standards as provided in this section and in §§ 164.308, 164.310, 164.312, 164.314 and 164.316 with respect to all electronic protected health information.
(d) Implementation specifications. In this subpart:
(1) Implementation specifications are required or addressable. If an implementation specification is required, the word “Required” appears in parentheses after the title of the implementation specification. If an implementation specification is addressable, the word “Addressable” appears in parentheses after the title of the implementation specification.
(2) When a standard adopted in § 164.308, § 164.310, § 164.312, § 164.314, or § 164.316 includes required implementation specifications, a covered entity or business associate must implement the implementation specifications.
(3) When a standard adopted in § 164.308, § 164.310, § 164.312, § 164.314, or § 164.316 includes addressable implementation specifications, a covered entity or business associate must—
(i) Assess whether each implementation specification is a reasonable and appropriate safeguard in its environment, when analyzed with reference to the likely contribution to protecting electronic protected health information; and
(ii) As applicable to the covered entity or business associate—
(A) Implement the implementation specification if reasonable and appropriate; or
(B) If implementing the implementation specification is not reasonable and appropriate—
$(1) Document why it would not be reasonable and appropriate to implement the implementation specification; and
$(2) Implement an equivalent alternative measure if reasonable and appropriate.
(e) Maintenance. A covered entity or business associate must review and modify the security measures implemented under this subpart as needed to continue provision of reasonable and appropriate protection of electronic protected health information, and update documentation of such security measures in accordance with § 164.316(b)(2)(iii).
"""


def condFreqDist():
    cfd = nltk.ConditionalFreqDist((genre, word)
        for genre in brown.categories()
            for word in brown.words(categories=genre))

    cfd.plot()

def getTokens(s):
    tokens = nltk.word_tokenize(s);
    return tokens;

def getLowerCaseWords(tok):
    lowerCaseWords = [w.lower() for w in tok]
    return lowerCaseWords;

def getVocabulary(lcw):
    vocab = sorted(set(lcw));
    return vocab;


'''
 regex metacharacters --->   . ^ $ * + ? { } [ ] \ | ( )
'''
def getRegularExpression(p, s):
    regexp = re.findall(p, s)
    return regexp;



"""
---------------------- MAIN()-------------------
"""
def driver1(s):
    tokens = getTokens(s);
    words = getLowerCaseWords(tokens)
    vocab = getVocabulary(words)

def driver2():
    ''' The goal is to print out the (a) in a sentence '''
    pattern = '\([\w]*\)'
    regex1 = getRegularExpression(pattern, myString)
    print ("The result = " , regex1);


def driver3():
    ''' The goal is to tokenize the words and tag the part of speech'''
    words = getTokens(regString);
    for token in words:
        tagged = nltk.pos_tag([token])
        print(tagged);


def driver4():
    ''' The goal is to create chunks'''
    customSentTokenizer = PunktSentenceTokenizer(trainingText)
    tokenizedRegs = customSentTokenizer.tokenize(sampleText)
    try:
        for regSent in tokenizedRegs:
            word = getTokens(regSent)
            tagged = nltk.pos_tag(word)

            cfgGrammar = r"""SHAMROQ: {<DT>?<JJ>*<CC>*<NN>?} """;
            
            parser = nltk.RegexpParser(cfgGrammar);
            output = parser.parse(tagged);
            output.draw;
        
            #print(output);
        
    except Exception as e:
        print(str(e) + '\n') 

def driver5():
    ''' The goal is to create chunks'''
    txt = oneLiner
    customSentTokenizer = PunktSentenceTokenizer(trainingText)
    tokenizedRegs = customSentTokenizer.tokenize(txt)
    try:
        for regSent in tokenizedRegs:
            word = getTokens(regSent)
            tagged = nltk.pos_tag(word)

            cfgGrammar = r"""SHAMROQ: {<DT>?<JJ>*<CC>*<NN>?} """;
            
            parser = nltk.RegexpParser(cfgGrammar);
            output = parser.parse(tagged);
            #output.draw;
        
            print(output);
        
    except Exception as e:
        print(str(e) + '\n')      

def main():
    driver5();

if __name__ == "__main__": 
    # calling main function 
    main()













    
