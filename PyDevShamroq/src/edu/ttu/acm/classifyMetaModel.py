import time
import spacy
import pandas as pd
import srsly
from spacy.matcher import Matcher
from beautifultable import BeautifulTable

linguisticFeatures = ['TEXT', 'PATTERN', 'SPAN', 'SUBJ', 'VERB', 'OBJECT']
df = pd.DataFrame(columns=linguisticFeatures)
nlp = spacy.load("en_core_web_lg")
patternCfg = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/patterns.jsonl"
patternMMCfg = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/patterns-meta-model.jsonl"
patternPrepPhrCfg = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/patterns-prep-phrases.jsonl"

patterns = srsly.read_jsonl(patternPrepPhrCfg)
ruler = nlp.add_pipe("span_ruler")
ruler.add_patterns(patterns)


'''
Use this as the example to find patterns
https://spacy.io/api/matcher#_title
https://spacy.io/usage/rule-based-matching
https://demos.explosion.ai/matcher

'''


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

def basicActivityPattern01():
    '''
        (1) verb phrase masquerading as NOUN or ADJECTIVE.  That is,
        For a NOUN, ending in "ing" called gerunds or nouns that end in:
        -ance, -sion, -tion, -ism, -sure, -zure, and -ment often describe
        activites (i.e. VERBS!!) These verbs can be separated out and made
        into separate SVO statements.  These nouns are lexically similar to
        an expanded verb phrase

        For an ADJECTIVE, if derived from past-tense verbs, then they describe
        activities (i.e. VERBS!!). These verbs can too be separated out and
        made into separate SVO statements.  These adjective are followed by
        a noun which is said to always be the object of the described action.

    '''
def prescriptiveStatment():
    return pStmt

def constitutieveStatement():
    return cStmt

def listGroundingPatterns():
    '''
        The core objective is the predicate - leading with the ROOT Verb
        Everything else supports the verb.  Here, I use "thematic/semantic roles
        to describe each provision - Akin to Breaux's "ACTIVITY". In fact, Breaux
        says in table IV, of Semantic Parameterization, that his roles maps to the
        Inquiry Lifecyle Model.
        Definition - https://www.ling.upenn.edu/~beatrice/syntax-textbook/box-thematic.html
        More here - https://en.wikipedia.org/wiki/Grammatical_relation
    '''
    semanticRole01 = 'agent'
    semanticRole02 = 'cause'
    semanticRole03 = 'instrument'
    semanticRole04 = 'experiencer'
    semanticRole05 = 'location'
    semanticRole06 = 'path'
    semanticRole07 = 'goal'
    semanticRole08 = 'measure'
    semanticRole09 = 'theme'

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
    time.sleep(0)
    return doc


def findMasqueradingVerbPhrase(inputToken):
    vm = []
    '''
     Look for nouns that end in the following
     -ance, -sion, -tion, -ism, -sure, -zure, -ment
     then take the verb form
    '''

'''
    for i in inputToken.subtree:
        if i.tag_ == "VBG":
            print("ALERT - gerund ", i.lemma_)
            time.sleep(0)
        elif i.dep_ == "prep":
            for j in i.children:
                doc = nlp(j.text)
                for t in doc:
                    print("HOLD IT (LEMMA) ", t.lemma_)
                    print("HOLD IT (NORM) ", t.norm_)
                    print("HOLD IT (DOC) ", t.doc)
                    print("HOLD IT (SUFFIX) ", t.suffix_)
                    time.sleep(0)


    return vm
'''


def processPrepositionalPhrase(inputToken):
    '''
     if "before" is found then, it belongs in the antecedent
     also, the noun associated with the prepositional phrase
     must be in there present-x tense.
     (e.g. collection becomes collects; disclosure becomes discloses)
    '''

    if inputToken.text == "before":
        print("STOP.. FOUND BEFORE... ")
        for i in inputToken.subtree:
            print(i)
            # findMasqueradingVerbPhrase(inputToken)
        time.sleep(0)
    elif inputToken.text == "after":
        print("STOP.. FOUND AFTER... ")
        for j in inputToken.subtree:
            print(j)
        # findMasqueradingVerbPhrase(inputToken)
        time.sleep(0)

def processMatcher(text, foundSpanOfText, spanOfPattern):
    print("called - processMatcher <>")
    print("pattern ...", spanOfPattern, "text --> ", foundSpanOfText)

    subject = "EMPTY"; root = "EMPTY"; directObject = "EMPTY"; pattern = foundSpanOfText
    indirectObj = "EMTPY"

    doc = nlp(foundSpanOfText)

    for token in doc:
        # print("TOKEN --> ", token.text)
        time.sleep(0)
        if token.dep_ == "nsubj" and token.head.dep_ == "ROOT":
            subject = token.text
            # subjectSubtree = list(token.subtree)
            # print(subject, "(x)")
            print("Subject (root head): ", subject)
            # print("\n")
            time.sleep(0)
        elif token.dep_ == "nsubj" and token.head.dep_ == "pcomp":
            subject = token.text
            # subjectSubtree = list(token.subtree)
            # print(subject, "(x)")
            print("Subject (pcomp): ", subject)
            # print("\n")
        elif token.dep_ == "nsubjpass" and token.head.dep_ == "ROOT":
            subject = token.text
            # subjectSubtree = list(token.subtree)
            # print(subject, "(x)")
            print("Subject (passive): ", subject)
            # print("\n")
        elif token.pos_ == "VERB" and token.dep_ == "ROOT":
            root = token.text
            print("VERB --->  ", root)
        elif token.dep_== "dative":
            indirectObj = token.text
            print("Indirect Object = ", indirectObj)
        elif token.dep_ == "dobj" and token.head.dep_ == "ROOT":
            # directObjectSubTree = list(token.subtree)
            directObject = token.text
            print("Object (root) = ", directObject)
            # print("Direct Object (token.subtree) = ", directObjectSubTree)
            # print("\n")
            time.sleep(0)
        elif token.dep_ == "dobj" and token.head.dep_ == "xcomp":
            # directObjectSubTree = list(token.subtree)
            directObject = token.text
            # print("Direct Object - xcomp = ", directObject)
            print("Object (xcomp) = ", directObject)
            # print("\n")
            time.sleep(0)
            # print("Direct Object - XCOMP HEAD -(token.text) = ", directObject)
        elif token.dep_ == "acl" and token.head.dep_ == 'acl':
            transaction = token.text
            print(transaction)
        elif token.text == "before":
            # processPrepositionalPhrase(doc)
            pass
        else:
            pass


    # linguisticFeatures = ['TEXT' (0), 'PATTERN'(1), 'SPAN'(2), 'SUBJ'(3), 'VERB'(4), 'OBJECT'(5)]
    # Store Results in a data frame

    if indirectObj != "EMTPY":
        print("\n---------GROUNDING-------------(1)")
        print("if ", subject, "(x)", indirectObj, "(y)", directObject, "(z)")
        print("then [OBL]", root, "(x, y, z)")
        time.sleep(0)
    else:
        print("\n---------GROUNDING-------------(2)")
        print("if ", subject, "(x)", directObject, "(y)")
        print("---> [OBL]", root, "(x, y)")
        time.sleep(0)
    '''
    df.loc[len(df.index)] = [text, pattern, spanOfPattern, subject, root, directObject]
    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)
    print("\n----------> Dataframe Results ...\n")
    print(df.iloc[0:500, 1:7])
    return df
    '''

# linguisticFeatures = ['TEXT', 'PATTERN', 'SPAN', 'SUBJ', 'VERB', 'OBJECT']
def processMatches(text, foundSpanOfText, spanOfPattern):
    print("called - processMatches")
    print("pattern ...", spanOfPattern, "text --> ", foundSpanOfText)

    subject = "EMPTY"; root = "EMPTY"; directObject = "EMPTY"; pattern = foundSpanOfText
    indirectObj = "EMTPY"

    doc = nlp(foundSpanOfText)

    for token in doc:
        # print("TOKEN --> ", token.text)
        time.sleep(0)
        if token.dep_ == "nsubj" and token.head.dep_ == "ROOT":
            subject = token.text
            # subjectSubtree = list(token.subtree)
            # print(subject, "(x)")
            print("Subject (root head): ", subject)
            # print("\n")
            time.sleep(0)
        elif token.dep_ == "nsubj" and token.head.dep_ == "pcomp":
            subject = token.text
            # subjectSubtree = list(token.subtree)
            # print(subject, "(x)")
            print("Subject (pcomp): ", subject)
            # print("\n")
        elif token.dep_ == "nsubjpass" and token.head.dep_ == "ROOT":
            subject = token.text
            # subjectSubtree = list(token.subtree)
            # print(subject, "(x)")
            print("Subject (passive): ", subject)
            # print("\n")
        elif token.pos_ == "VERB" and token.dep_ == "ROOT":
            root = token.text
            print("VERB --->  ", root)
        elif token.tag_ == "MD" and token.head.dep_ == "ROOT" and token.text == "must":
            print("MODALITY = OBLIGATION ---> ", token.text)
            time.sleep(0)
        elif token.dep_== "dative":
            indirectObj = token.text
            print("Indirect Object = ", indirectObj)
        elif token.dep_ == "dobj" and token.head.dep_ == "ROOT":
            # directObjectSubTree = list(token.subtree)
            directObject = token.text
            print("Object (root) = ", directObject)
            # print("Direct Object (token.subtree) = ", directObjectSubTree)
            # print("\n")
            time.sleep(0)
        elif token.dep_ == "dobj" and token.head.dep_ == "xcomp":
            # directObjectSubTree = list(token.subtree)
            directObject = token.text
            # print("Direct Object - xcomp = ", directObject)
            print("Object (xcomp) = ", directObject)
            # print("\n")
            time.sleep(0)
            # print("Direct Object - XCOMP HEAD -(token.text) = ", directObject)
        elif token.dep_ == "acl" and token.head.dep_ == 'acl':
            transaction = token.text
            print(transaction)
        elif token.text == "before":
            # processPrepositionalPhrase(doc)
            pass
        else:
            pass


    # linguisticFeatures = ['TEXT' (0), 'PATTERN'(1), 'SPAN'(2), 'SUBJ'(3), 'VERB'(4), 'OBJECT'(5)]
    # Store Results in a data frame
    '''
    if indirectObj != "EMTPY":
        print("\n---------GROUNDING-------------(1)")
        print("if ", subject, "(x)", indirectObj, "(y)", directObject, "(z)")
        print("then [OBL]", root, "(x, y, z)")
        time.sleep(0)
    else:
        print("\n---------GROUNDING-------------(2)")
        print("if ", subject, "(x)", directObject, "(y)")
        print("---> [OBL]", root, "(x, y)")
        time.sleep(0)

    df.loc[len(df.index)] = [text, pattern, spanOfPattern, subject, root, directObject]
    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)
    print("\n----------> Dataframe Results ...\n")
    print(df.iloc[0:500, 1:7])
    return df
    '''


def classifySpan(text):
    doc = nlp(text)
    for span in doc.spans["ruler"]:
        y = processMatches(text, span.text, span.label_)
    # classifyMetaModel(text, df)


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
                        print("|                       |")
                        print("|   Evaluate Statement  |")
                        print("|                       |")
                        print(text)
                        getDepData(text)
                        classifySpan(text)
                        print("<<<<------------------------------------>>>>>\n\n")
                        time.sleep(0)

                        '''
                        ---> Process the MetaModel
                        '''
                        #classifyMetaModel(text)
                        #print("Text... classifyMetaModel", text)


def init(inputDict):
    regulation = inputDict
    processEachProvision(regulation)
    #prepareModel()
    return regulation
