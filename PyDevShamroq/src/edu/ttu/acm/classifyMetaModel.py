import time
import spacy
import textacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")
i = 1

'''
Use this as the example to find patterns
https://spacy.io/api/matcher#_title
https://spacy.io/usage/rule-based-matching
https://demos.explosion.ai/matcher

'''
right_pattern_01 = [{'LOWER': 'has'},
                    {'LOWER': 'a'},
                    {'LOWER': 'right'},
                    {'LOWER': 'to'},
                    {'POS': 'VERB'}]
right_pattern_02 = [{'LOWER': 'has'},
                    {'LOWER': 'the'},
                    {'LOWER': 'right'},
                    {'LOWER': 'to'},
                    {'POS': 'VERB'}]
right_pattern_03 = [{'LOWER': 'retains'},
                    {'LOWER': 'the'},
                    {'LOWER': 'right'},
                    {'LOWER': 'to'},
                    {'POS': 'VERB'}]

obligation_pattern_01 = [{'LOWER': 'must'},
                         {'POS': 'VERB'}]
obligation_pattern_02 = [{'LOWER': 'is'},
                         {'LOWER': 'required'},
                         {'LOWER': 'to'},
                         {'POS': 'VERB'}]
obligation_pattern_03 = [{'LOWER': 'shall'},
                         {'POS': 'VERB'}, ]
obligation_pattern_04 = [{'LOWER': 'may'},
                         {'LOWER': 'not'}]
obligation_pattern_05 = [{'LOWER': 'is'},
                         {'LOWER': 'prohibited'}]
obligation_pattern_06 = [{'LOWER': 'is'},
                         {'LOWER': 'subject'},
                         {'LOWER': 'to'},
                         {'POS': 'VERB'}]
obligation_pattern_07 = [{'LOWER': 'must'},
                         {'LOWER': 'be'},
                         {'POS': 'ADV'},
                         {'POS': 'VERB'}]
priv_pattern_00 = [{'LOWER': 'may'},
                   {'IS_PUNCT': True, 'OP': '?'}]

priv_pattern_01 = [{'LOWER': 'may'},
                   {'POS': 'ADV', 'OP': '?'},
                   {'IS_PUNCT': True, 'OP': '?'},
                   {'POS': 'VERB'}]
priv_pattern_02 = [{'LOWER': 'may'},
                   {'LOWER': 'elect'},
                   {'LOWER': 'not'},
                   {'LOWER': 'to'}]
priv_pattern_03 = [{'LOWER': 'is'},
                   {'LOWER': 'not'},
                   {'LOWER': 'required'},
                   {'LOWER': 'to'},
                   {'POS': 'VERB'}]
priv_pattern_04 = [{'LOWER': 'requirement'},
                   {'LOWER': 'does'},
                   {'LOWER': 'not'},
                   {'LOWER': 'apply'},
                   {'LOWER': 'to'},
                   {'POS': 'VERB'}]
priv_pattern_05 = [{'LOWER': 'is'},
                   {'LOWER': 'permitted'},
                   {'LOWER': 'to'},
                   {'POS': 'VERB'}]
priv_pattern_06 = [{'LOWER': 'at'},
                   {'LOWER': 'the'},
                   {'LOWER': 'election'},
                   {'LOWER': 'of'},
                   {'POS': 'NOUN'}]
priv_pattern_07 = [{'LOWER': 'is'},
                   {'LOWER': 'not'},
                   {'LOWER': 'subject'},
                   {'LOWER': 'to'},
                   {'POS': 'VERB'}]
groundPattern01 = [{'POS': 'DET', 'OP': '?'},
                   {'POS': 'ADJ', 'OP': '*'},
                   {'POS': 'NOUN', 'OP': '+', 'DEP': 'nsubj'},
                   {'POS': 'VERB', 'DEP': 'ROOT'}]
#coppa 312.5 01
svo100 = [{'TAG': 'DT'},
         {'DEP': 'nsubjpass'},
         {'TAG': 'VBZ'},
         {'DEP': 'ROOT'},
         {'TAG': 'TO'},
         {'TAG': 'VB'},
         {'TAG': 'JJ', 'OP': '*'},
         {'DEP': 'dobj'}]

#coppa 312.5 02
svo101 = [{'TAG': 'DT'},
          {'DEP': 'nsubj'},
          {'TAG': 'MD'},
          {'DEP': 'ROOT'},
          {'TAG': 'DT'},
          {'TAG': 'NN'},
          {'TAG': 'DT'},
          {'DEP': 'dobj'}]

svo01 = [{'TAG': 'DT'},
         {'DEP': 'nsubj'},
         {'TAG': 'MD'},
         {'DEP': 'ROOT'},
         {'TAG': 'JJ', 'OP': '*'},
         {'DEP': 'dobj'}]


svo02 = [{'TAG': 'DT'},
         {'TAG': 'JJ', 'OP': '*'},
         {'DEP': 'nsubj'},
         {'TAG': 'MD'},
         {'TAG': 'RB'},
         {'DEP': 'ROOT'},
         {'TAG': 'DT'},
         {'DEP': 'dobj'}]

#supports HIPAA
svo03 = [{'TAG': 'DT'},
         {'TAG': 'VBN'},
         {'TAG': 'NN', 'OP': '*'},
         {'DEP': 'nsubj'},
         {'TAG': 'MD'},
         {'TAG': ':'}]

#supports HIPAA
svo04 = [{'DEP': 'nsubj'},
         {'TAG': 'MD'},
         {'DEP': 'ROOT'},
         {'TAG': 'DT'},
         {'TAG': 'NN', 'OP': '*'},
         {'DEP': 'dobj'},
         {'TAG': 'CC', 'OP': '*'},
         {'TAG': 'VB'},
         {'TAG': 'RP'},
         {'DEP': 'dobj'}]

#supports GLBA
svo05 = [{'TAG': 'DT'},
         {'TAG': 'JJ', 'OP': '*'},
         {'DEP': 'nsubj'},
         {'TAG': 'MD'},
         {'DEP': 'ROOT'},
         {'TAG': 'CC'},
         {'DEP': 'conj'},
         {'TAG': 'VBN', 'OP': '*'},
         {'TAG': 'NN', 'OP': '*'},
         {'DEP': 'dobj'}]

svo06 = [{'DEP': 'nsubj'},
         {'TAG': 'MD'},
         {'TAG': 'RB'},
         {'DEP': 'ROOT'},
         {'TAG': 'IN'},
         {'TAG': 'DT'},
         {'TAG': 'NN'},
         {'TAG': 'MD'},
         {'TAG': 'VB'},
         {'TAG': 'JJ', 'OP': '*'},
         {'DEP': 'dobj'}]

#hipaa 164.510 01
svo200 = [{'TAG': 'DT'},
          {'TAG': 'JJ', 'OP': '*'},
          {'TAG': 'NN', 'OP': '*'},
          {'DEP': 'nsubj'},
          {'TAG': 'MD'},
          {'DEP': 'ROOT'},
          {'TAG': 'DT'},
          {'DEP': 'dobj'}]

#hipaa 164.510 01
svo201 = [{'TAG': 'DT'},
          {'TAG': 'VBN'},
          {'TAG': 'NN', 'OP': '*'},
          {'DEP': 'nsubj'},
          {'TAG': 'MD'},
          {'DEP': 'ROOT'},
          {'TAG': 'CC'},
          {'TAG': 'VB'},
          {'TAG': 'DT'},
          {'TAG': 'CC'},
          {'TAG': 'DT'}]

shamroqMatcher = Matcher(nlp.vocab)

shamroqMatcher.add("RIGHT01", [right_pattern_01])
shamroqMatcher.add("RIGHT02", [right_pattern_02])
shamroqMatcher.add("RIGHT03", [right_pattern_03])

shamroqMatcher.add("OBLIGATION01", [obligation_pattern_01])
shamroqMatcher.add("OBLIGATION02", [obligation_pattern_02])
shamroqMatcher.add("OBLIGATION03", [obligation_pattern_03])
shamroqMatcher.add("OBLIGATION04", [obligation_pattern_04])
shamroqMatcher.add("OBLIGATION05", [obligation_pattern_05])
shamroqMatcher.add("OBLIGATION06", [obligation_pattern_06])
shamroqMatcher.add("OBLIGATION07", [obligation_pattern_07])

shamroqMatcher.add("PRIVILEGE01", [priv_pattern_01])
shamroqMatcher.add("PRIVILEGE02", [priv_pattern_02])
shamroqMatcher.add("PRIVILEGE03", [priv_pattern_03])
shamroqMatcher.add("PRIVILEGE04", [priv_pattern_04])
shamroqMatcher.add("PRIVILEGE05", [priv_pattern_05])
shamroqMatcher.add("PRIVILEGE06", [priv_pattern_06])
shamroqMatcher.add("PRIVILEGE07", [priv_pattern_07])

groundMatcher = Matcher(nlp.vocab)
groundMatcher.add("GROUNDING_01", [groundPattern01])

bapMatcher = Matcher(nlp.vocab)
bapWithModality01 = [{'POS': 'DET', 'OP': '*'},
                     {'POS': 'ADJ', 'OP': '*'},
                     {'POS': 'NOUN', 'OP': '+', 'DEP': 'nsubj'}]


bapMatcher.add("BAP01", [bapWithModality01], greedy='LONGEST')


def printEachProvision(params):
    for key, value in params.items():
        if key == "Metadata":
            print("key---------->", key)
            print("value-------->", value, "\n\n")
        if key == "Header":
            print("key---------->", key)
            print("value-------->", value, "\n\n")
        if key == "Body":
            print("body -------->  Body")
            for proKey, proValue in value.items():
                if proKey == "content":
                    for x in range(len(proValue)):
                        '''
                         ---> Process the Grounding
                        '''
                        text = proValue[x]
                        print(text)
                        classifyWithMatcher(text)
                        # classifyHohfeldian(text)
                        # classifySVO(text)
                        #classifySVONounChunks(text)
                        # classifySVOList(text)
                        # classifyNounPhrases(text)
                        # classifyHohfeldian(text)
                        #classBasicActivityPattern(text)

            print("\n FINISHED\n\n\n")
        time.sleep(0)


'''
ideas
1. need a grammar
2. break the classification up into three parts
Part 1 - find the pattern
Part 2 - break the pattern into atomic isomorphic decompositon
Part 3 - store in a structure that can be use for Legal Rule ML
Note, this structure can be a json key/value paper that aligns with the Legal Rule ML spec

Because this is SO COMPLEX, work with one provision at a time, then run to see how many align, 
Let's see if this will yield no more that 50 patterns
use a combination of POS, OP, REGEX, and Morphology in Spacy... Let's gooooo!!!

The first two here
(1) An operator is required to obtain verifiable parental consent before any collection, use, or disclosure of personal information from children, including consent to any material change in the collection, use, or disclosure practices to which the parent has previously consented.</P>
(2) An operator must give the parent the option to consent to the collection and use of the child's personal information without consenting to disclosure of his or her personal information to third parties.</P>

def getGroundingData(text):
    print("----------------> getGroundingData  \n\n")

    doc = nlp(text)
    patternResults = findPattern(doc)
    aid = isomorphism(patternResults)
    storeLRML = legalRuleMLKB(aid)
    matches = bapMatcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        #print(string_id, "  ", span.text)
        print(match_id, string_id, start, end, span.text)
        print("\n")

    time.sleep(10)

    print("----------------> classBasicActivityPattern  \n\n")
'''

def classBasicActivityPattern(text):
    print("----------------> classBasicActivityPattern  \n\n")

    doc = nlp(text)
    matches = bapMatcher(doc)
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        #print(string_id, "  ", span.text)
        print(match_id, string_id, start, end, span.text)
        print("\n")

    time.sleep(10)

    print("----------------> classBasicActivityPattern  \n\n")


'''
 Textacy Documentation - https://textacy.readthedocs.io/en/0.11.0/api_reference/extract.html
 Tutorial - https://textacy.readthedocs.io/en/0.11.0/tutorials/tutorial-2.html
'''


def classifyWithMatcher(text):
    doc = nlp(text)
    regMatcher = Matcher(nlp.vocab)
    regMatcher.add("Subject Verb Object  -----> svo100 ", [svo100], greedy="LONGEST")
    regMatcher.add("Subject Verb Object  -----> svo101 ", [svo101], greedy="LONGEST")
    regMatcher.add("Subject Verb Object  -----> svo01 ", [svo01], greedy="LONGEST")
    regMatcher.add("Subject Verb Object  -----> svo02 ", [svo02], greedy="LONGEST")
    regMatcher.add("Subject Verb Object  -----> svo03 ", [svo03], greedy="LONGEST")
    regMatcher.add("Subject Verb Object  -----> svo04 ", [svo04], greedy="LONGEST")
    regMatcher.add("Subject Verb Object  -----> svo05 ", [svo05], greedy="LONGEST")
    regMatcher.add("Subject Verb Object  -----> svo06 ", [svo06], greedy="LONGEST")
    regMatcher.add("Subject Verb Object  -----> svo200 ", [svo200], greedy="LONGEST")
    regMatcher.add("Subject Verb Object  -----> svo201 ", [svo201], greedy="LONGEST")

    matches = regMatcher(doc)

    '''
    This yields good result, but I don't have control over the object (noun phrase)
    '''
    for match_id, start, end in matches:
        # Get string representation
        string_id = nlp.vocab.strings[match_id]
        # The matched span
        span = doc[start:end]
        print("\n<><><> = ", string_id, start, end, span.text)
        time.sleep(10)

    print("----------------> Complete:  classifyWithMatcher  \n\n")




def classifySVO(text):
    print("----------------> classifySVO  \n\n")
    doc = nlp(text)
    triples = textacy.extract.subject_verb_object_triples(doc)
    tuples_to_list = list(triples)
    '''
    This yields good result, but I don't have control over the object (noun phrase)
    '''
    for svo in tuples_to_list:
        print("Subject ===>", svo.subject)
        print("Verb ===> ", svo.verb)
        print("Object ===>", svo.object, "\n")

    print("----------------> classifySVO  \n\n")


def classifySVONounChunks(text):
    print("----------------> classifySVONounChunks  \n\n")

    doc = nlp(text)
    print("classify SVO Noun Chucks START \n")
    svoNounChunks = textacy.extract.basics.noun_chunks(doc)
    for svongram in svoNounChunks:
        print(svongram)
    print("classify SVO Noun Chucks DONE ")

    print("----------------> classifySVONounChunks  \n\n")


def classifySVOWords(text):
    print("----------------> classifySVOWords  \n\n")
    doc = nlp(text)
    print("classifySVOWords \n")
    svoWords = textacy.extract.basics.words(doc)
    for svongram in svoWords:
        print(svongram)
    print("classifySVOList DONE ")

    print("----------------> classifySVOWords  \n\n")


def classifySVOList(text):
    print("----------------> classifySVOList  \n\n")

    doc = nlp(text)
    print("classifySVOList")
    svoList = list(textacy.extract.ngrams(doc, 3, filter_stops=True, filter_punct=True, filter_nums=False))
    svoWords = textacy.extract.basics.words(doc)
    for svongram in svoList:
        print(svongram)
    print("classifySVOList DONE ")

    print("----------------> classifySVOList  \n\n")


def classifyNounPhrases(text):
    print("----------------> classifyNounPhrases  \n\n")

    doc = nlp(text)
    for chunk in doc.noun_chunks:
        print("chunk.text --> ", chunk.text)
        print("chunk.root.text --> ", chunk.root.text)
        print("chunk.root.dep_ --> ", chunk.root.dep_)
        print("chunk.root.head.text --> ", chunk.root.head.text)
        print("\n\n")
        time.sleep(0)

    print("----------------> classifyNounPhrases  \n\n")


def classifyHohfeldian(text):
    print("----------------> classifyHohfeldian  \n\n")

    doc = nlp(text)
    for match_id, start, end in shamroqMatcher(doc):
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        print(string_id, "  ", span.text)
        print("\n")
        time.sleep(0)

    print("----------------> classifyHohfeldian  \n\n")


def classifyGrounding(text):
    '''
    https://demos.explosion.ai/matcher
      takes a nlp doc object
      need to set up teh following
    (1) a pattern in the form of
        groundPattern01 =
           [{'POS': 'DET', 'OP': '?'},
           {'POS': 'ADJ', 'OP': '*'},
           {'POS': 'NOUN', 'OP': '+', 'DEP': 'nsubj'},
           {'POS': 'VERB', 'DEP': 'ROOT'}]
    (2) print Token type and attributes

    '''
    doc = nlp(text)
    for match_id, start, end in groundMatcher(doc):
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        print(string_id, "  ", span.text)
        print("\n")
        time.sleep(0)


def getMetalModel(inputDictionary):
    resultMM = inputDictionary
    return resultMM


'''
Universal POS tags - https://universaldependencies.org/u/pos/
Deplacy - https://spacy.io/universe/project/deplacy

OP	DESCRIPTION
!	Negate the pattern, by requiring it to match exactly 0 times.
?	Make the pattern optional, by allowing it to match 0 or 1 times.
+	Require the pattern to match 1 or more times.
*	Allow the pattern to match zero or more times.
{n}	Require the pattern to match exactly n times.
{n,m}	Require the pattern to match at least n but not more than m times.
{n,}	Require the pattern to match at least n times.
{,m}	Require the pattern to match at most m times.


'''


def init(inputDict):
    metaModel = inputDict
    printEachProvision(metaModel)
    return metaModel
