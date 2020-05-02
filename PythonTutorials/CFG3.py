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
The task thus required extracting structured information from English that had been formatted in a mixture of
two dimensional layout and free-running prose a daunting technical challenge, but one that was ultimately solved
successfully. More details about the solution follow, but ﬁrst, let’s place this problem in context.
"""


trainingText = """
In 2001 the U.S. Department of Labor was tasked with building a Web site that would help people ﬁ nd continuing
education opportunities at community colleges, universities, and organizations across the country.
The department wanted its Web site to support ﬁ elded Boolean searches over locations, dates, times, prerequisites,
instructors, topic areas, and course descriptions. Ultimately it was also interested in mining its new database for
patterns and educational trends. This was a major data integration project, aiming to automatically gather detailed,
structured information from tens of thousands of individual institutions every three months.  The ﬁrst and biggest
problem was that much of the data wasn’t available even in semi structured form, much less normalized, structured form.
Although some of the larger organizations had internal databases of their course listings, almost none of them had publicly
available interfaces to their databases. The only universally available public interfaces were Web pages designed for
human browsing. Unfortunately, but as expected, each organization used dif-ferent text formatting. Some of these Web pages
contained two dimensional text tables; many others used a stylized collection of paragraphs for each course offering;
still others had a single paragraph of English prose containing all the information about each course.
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
                shamroq-NP: {<DT>?<JJ>*<CC>?<NN>*<MD>?<VB|VBD|VBZ>*}
                shamroq-VP: {<PRP>?<VB|VBD|VBZ>*<RB|RBR>?}
                """;

            
            
            parser = nltk.RegexpParser(cfgNPGrammar2);
            output = parser.parse(tagged);
     
            print(output);
            output.draw;
        
    except Exception as e:
        print(str(e) + '\n')

        
def main():
    driver2();

if __name__ == "__main__": 
    # calling main function 
    main()













    
