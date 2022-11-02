import time
import spacy
import textacy
from spacy.matcher import Matcher
from beautifultable import BeautifulTable


nlp = spacy.load("en_core_web_lg")

'''
Use this as the example to find patterns
https://spacy.io/api/matcher#_title
https://spacy.io/usage/rule-based-matching
https://demos.explosion.ai/matcher

'''

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
                        getDepData(text)
                        #classifyWithMatcher(text)
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
 Textacy Documentation - https://textacy.readthedocs.io/en/0.11.0/api_reference/extract.html
 Tutorial - https://textacy.readthedocs.io/en/0.11.0/tutorials/tutorial-2.html
'''


def getDepData(text):
    doc = nlp(text)
    SN = 10; TOKEN = 15; TAG = 10; EXPLAIN = 20; HEAD = 15; DEP = 10; CHILD = 15; ANCESTORS = 30; TREE = 20;
    table = BeautifulTable(maxwidth=165)
    table.columns.header = ['SN', 'Text', 'TAG', 'Expln Tag', 'HEAD', 'Dep', 'Expln Dep', 'Child', 'Ancestors', 'Subtree']
    table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
    table.columns.width = [SN, TOKEN, TAG, EXPLAIN, HEAD, DEP, EXPLAIN, CHILD, ANCESTORS, TREE]

    for token in doc:
        ancestors = [t.text for t in token.ancestors]
        children = [child for child in token.children]
        table.rows.append([token.i, token.text, token.tag_, spacy.explain(token.tag_), token.head.text,
                           token.dep_, spacy.explain(token.dep_), children, ancestors, list(token.subtree)])
    print(table)
    time.sleep(10)
    return doc

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
        print("\n<><><> ==========> ", string_id, start, end, span.text)
        time.sleep(10)


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
