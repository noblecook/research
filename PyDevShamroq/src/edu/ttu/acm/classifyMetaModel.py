import time
import spacy
from spacy.matcher import Matcher
from beautifultable import BeautifulTable
import pandas as pd
import matplotlib.pyplot as plt
linguisticFeatures = ['TEXT', 'PATTERN', 'SPAN', 'MODALITY', 'SUBJ', 'VERB', 'OBJECT']
df = pd.DataFrame(columns=linguisticFeatures)


nlp = spacy.load("en_core_web_lg")

'''
Use this as the example to find patterns
https://spacy.io/api/matcher#_title
https://spacy.io/usage/rule-based-matching
https://demos.explosion.ai/matcher

'''

right_pattern_01 = [{'LOWER': 'has'},{'LOWER': 'a'},{'LOWER': 'right'},{'LOWER': 'to'},{'POS': 'VERB'}]
right_pattern_02 = [{'LOWER': 'has'},{'LOWER': 'the'},{'LOWER': 'right'},{'LOWER': 'to'},{'POS': 'VERB'}]
right_pattern_03 = [{'LOWER': 'retains'}, {'LOWER': 'the'}, {'LOWER': 'right'}, {'LOWER': 'to'}, {'POS': 'VERB'}]

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



groundingMatcher = Matcher(nlp.vocab)

'''
--- Rights-----
'''
groundingMatcher.add("Right --> 01", [right_pattern_01], greedy="LONGEST")
groundingMatcher.add("Right --> 01", [right_pattern_02], greedy="LONGEST")
groundingMatcher.add("Right --> 01", [right_pattern_03], greedy="LONGEST")

'''
--- Obligations-----
'''
groundingMatcher.add("Obligation --> 01", [obligation_pattern_01], greedy="LONGEST")
groundingMatcher.add("Obligation --> 02", [obligation_pattern_02], greedy="LONGEST")
groundingMatcher.add("Obligation --> 03", [obligation_pattern_03], greedy="LONGEST")
groundingMatcher.add("Obligation --> 04", [obligation_pattern_04], greedy="LONGEST")
groundingMatcher.add("Obligation --> 05", [obligation_pattern_05], greedy="LONGEST")
groundingMatcher.add("Obligation --> 06", [obligation_pattern_06], greedy="LONGEST")

'''
--- Privileges-----
'''
groundingMatcher.add("Privileges --> 00", [priv_pattern_00], greedy="LONGEST")
groundingMatcher.add("Privileges --> 01", [priv_pattern_01], greedy="LONGEST")
groundingMatcher.add("Privileges --> 02", [priv_pattern_02], greedy="LONGEST")
groundingMatcher.add("Privileges --> 03", [priv_pattern_03], greedy="LONGEST")
groundingMatcher.add("Privileges --> 04", [priv_pattern_04], greedy="LONGEST")
groundingMatcher.add("Privileges --> 05", [priv_pattern_05], greedy="LONGEST")
groundingMatcher.add("Privileges --> 06", [priv_pattern_06], greedy="LONGEST")
groundingMatcher.add("Privileges --> 07", [priv_pattern_07], greedy="LONGEST")

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


def processEachProvision(params):
    for key, value in params.items():
        if key == "Metadata":
            print("key---------->", key)
            print("value-------->", value, "\n\n")
        if key == "Header":
            print("key---------->", key)
            print("value-------->", value, "\n\n")
        if key == "Body":
            print("body -------->  Body")
            for statementKey, statementValue in value.items():
                if statementKey == "content":
                    for x in range(len(statementValue)):
                        text = statementValue[x]

                        '''
                         ---> Process the Grounding
                        '''
                        classify(text)

                        '''
                        ---> Process the MetaModel
                        '''
                        #classifyMetaModel(text)
                        #print("Text... classifyMetaModel", text)


'''
 Textacy Documentation - https://textacy.readthedocs.io/en/0.11.0/api_reference/extract.html
 Tutorial - https://textacy.readthedocs.io/en/0.11.0/tutorials/tutorial-2.html


def setDataFrame():
    if (string_id == OBLIGATION):
        getObligationGroundingAndMetaModel()
    elif (string_id == PERMISSON):
        getPermissionGroundingAndMetaModel()
    elif(string_id == RIGHTS):
        getRightsGroundingAndMetaModel()
    else:
        pass;
'''


# linguisticFeatures = ['TEXT', 'PATTERN', 'SPAN', 'MODALITY', 'SUBJ', 'VERB', 'OBJECT']
def getObligationGroundingAndMetaModel(text, string_id, span):
    print("called - getObligationGroundingAndMetaModel")
    subject = "EMPTY"; root = "EMPTY"; directObject = "EMPTY"; modality = "EMPTY"
    pattern = string_id
    print(text)

    doc = nlp(text)
    for token in doc:
        if token.dep_ == "nsubj" and token.head.dep_ == "ROOT":
            subject = token.text
            #subject = list(token.subtree)
            #print("\nNominal Subject =", subject)
        elif token.dep_ == "nsubjpass" and token.head.pos_ == "VERB":
            subject = token.text
            #subject = list(token.subtree)
            #print("\nNominal PASSIVE Subject =", subject)
        elif token.tag_ == "MD":
            modality = token.text
            #print("MODAL VERB =", modality)
        elif token.pos_ == "VERB" and token.dep_ == "ROOT":
            #root = token.text
            root = list(token.subtree)
            #print("\nROOT = ", root)
        elif token.dep_ == "dobj":
            #directObject = list(token.subtree)
            directObject = token.text
            #print("Direct Object (subtree) = ", directObject)
            #print("\n")
        else:
            pass

    # linguisticFeatures = ['TEXT' (0), 'PATTERN'(1), 'SPAN'(2), 'MODALITY'(3), 'SUBJ'(4), 'VERB'(5), 'OBJECT'(6)]
    df.loc[len(df.index)] = [text, pattern, span, modality, subject, root, directObject]

    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)


    print("\n----------> Dataframe Results ...\n")
    print(df.iloc[0:10, 1:7])
    print("\n\n\n")
    time.sleep(1)
    return df;


def classify(text):
    doc = nlp(text)

    matches = groundingMatcher(doc)


    '''
        This yields good result, but I don't have control over the object (noun phrase)
        linguisticFeatures = ['TOKEN', 'POS', 'TAG', 'DEP']
        use spaCy 3.3.1
    '''
    for match_id, start, end in matches:
        '''
            If there is a match, classify the grounding
        '''
        # Get string representation
        string_id = nlp.vocab.strings[match_id]
        # The matched span
        span = doc[start:end]
        y = getObligationGroundingAndMetaModel(text, span, string_id)

        '''
            Then classify the metamodel and store in the dataframe
        '''
        #classifyMetaModel(text, df)


def classifyMetaModel(text):
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
        print("\n||||||||| ")
        print("\n<><><> ==========> ", string_id, start, end, span.text)
        print("\n||||||||| ")


def on_match(matcher, doc, id, matches):
    print("Hello World!")
    print("matcher ", matcher)
    print("doc ..", doc)
    print("id ..", id)
    print("matches ..", doc)
    time.sleep(100)



def setDataFrame(text):
    doc = nlp(text)
    for token in doc:
        df.loc[len(df.index)] = [token.text, token.pos_, token.tag_, token.dep_]
        #print(df)
    return df

def getFrequencyData(text):
    doc = nlp(text)
    countTags = doc.count_by(spacy.attrs.DEP)
    for pos, count in sorted(countTags.items()):
        senTag = doc.vocab[pos].text
        print(senTag, count)



'''
A list of dependency labels listed here 
- https://github.com/clir/clearnlp-guidelines/blob/master/md/specifications/dependency_labels.md
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

dfColHeadings = ['ACL', 'ACOMP', 'ADVCL', 'ADVMOD', 'AGENT', 'AMOD', 'APPOS', 'ATTR',
                     'AUX', 'AUXPASS', 'CASE', 'CC', 'CCOMP', 'COMPOUND', 'CONJ', 'CSUBJ',
                     'CUSBJPASS', 'DATIVE', 'DEP', 'DET', 'DOBJ', 'EXPL', 'INTJ', 'MARK',
                     'META', 'NEG', 'NOUNMOD', 'NPMOD', 'NSUBJ', 'NSUBJPASS', 'NUMMOD',
                     'OPRD', 'PARATAXIS', 'PCOMP', 'POBJ', 'POSS', 'PRECONJ', 'PREDET',
                     'PREP', 'PRT', 'PUNCT', 'QUANTMOD', 'RELCL', 'ROOT', 'XCOMP']
                     
    for token in doc:
        df.concat([token.text, token.lemma_, token.pos_, token.tag_,
                   token.dep_, token.head.text, token.head.pos_])


'''


def readConfigFile():
    config = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/rule-oblig.cfg"
    f = open(config, "r")
    for line in f.readline():
        print(line)
    f.close()


def init(inputDict):
    regulation = inputDict
    processEachProvision(regulation)
    #prepareModel()
    return regulation
