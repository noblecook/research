"""

When the texts of a corpus are divided into several categories,
by genre, topic, author, etc, we can maintain separate frequency
distributions for each category. This will allow us to study
systematic differences between the categories.

This is relevant for checking modal verbs in different Legal Context.
For Example, Department of Energy vs. Health and Human Services vs.

\d
Matches any decimal digit; this is equivalent to the class [0-9].

\D
Matches any non-digit character; this is equivalent to the class [^0-9].

\s
Matches any whitespace character; this is equivalent to the class [ \t\n\r\f\v].

\S
Matches any non-whitespace character; this is equivalent to the class [^ \t\n\r\f\v].

\w
Matches any alphanumeric character; this is equivalent to the class [a-zA-Z0-9_].

\W
Matches any non-alphanumeric character; this is equivalent to the class [^a-zA-Z0-9_].

"""
import nltk
import re


simpleString = '''(a) General requirements. Covered entities and business associates must do the following:  (1) Ensure the confidentiality, integrity, and availability of all electronic protected health information the covered entity or business associate creates, receives, maintains, or transmits. (2) Protect against any reasonably anticipated threats or hazards to the security or integrity of such information.  (3) Protect against any reasonably anticipated uses or disclosures of such information that are not permitted or required under subpart E of this part.(4) Ensure compliance with this subpart by its workforce.  (b) Flexibility of approach. (1) Covered entities and business associates may use any security measures that allow the covered entity or business associate to reasonably and appropriately implement the standards and implementation specifications as specified in this subpart.(2) In deciding which security measures to use, a covered entity or business associate must take into account the following factors:  (i) The size, complexity, and capabilities of the covered entity or business associate. (ii) The covered entity's or the business associate's technical infrastructure, hardware, and software security capabilities. (iii) The costs of security measures.(iv) The probability and criticality of potential risks to electronic protected health information'''


myString = """
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
(iv) The probability and criticality of potential risks to electronic protected health information
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
def driver1():
    tokens = getTokens(simpleString);
    words = getLowerCaseWords(tokens)
    vocab = getVocabulary(words)

def driver2():
    ''' The goal is to print out the (a) in a sentence '''
    pattern = '\([\w]*\)'
    regex1 = getRegularExpression(pattern, myString)
    print ("The result = " , regex1);
    
def main():
    driver2()
    

    
    
if __name__ == "__main__": 
    # calling main function 
    main()













    
