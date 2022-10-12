import time
import spacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
nlp = spacy.load("en_core_web_sm")
i = 1
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

shamroqMatcher.add("PRIVILEGE01", [priv_pattern_01])
shamroqMatcher.add("PRIVILEGE02", [priv_pattern_02])
shamroqMatcher.add("PRIVILEGE03", [priv_pattern_03])
shamroqMatcher.add("PRIVILEGE04", [priv_pattern_04])
shamroqMatcher.add("PRIVILEGE05", [priv_pattern_05])
shamroqMatcher.add("PRIVILEGE06", [priv_pattern_06])
shamroqMatcher.add("PRIVILEGE07", [priv_pattern_07])

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
                        classifyHohfeldian(text)
                        classifyNounPhrases(text)
                        #processGrounding(text)
            print("\n FINISHED\n\n\n")
        time.sleep(0)


def classifyNounPhrases(text):
    doc = nlp(text)
    for chunk in doc.noun_chunks:
        print("chunk.text --> ", chunk.text)
        print("chunk.root.text --> ", chunk.root.text)
        print("chunk.root.dep_ --> ", chunk.root.dep_)
        print("chunk.root.head.text --> ", chunk.root.head.text)
        print("\n\n")
        time.sleep(0)




def classifyHohfeldian(text):
    doc = nlp(text)
    for match_id, start, end in shamroqMatcher(doc):
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        print(string_id, "  ", span.text)
        print("\n")
        time.sleep(0)


def processGrounding(text):
    '''print Token type and attributes'''
    doc = nlp(text)
    for token in doc:
        print(token.text, token.pos_, token.tag_, token.dep_,token.is_stop)


def getMetalModel(inputDictionary):
    resultMM = inputDictionary
    return resultMM


def init(inputDict):
    metaModel = inputDict
    printEachProvision(metaModel)
    return metaModel
