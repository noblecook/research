import time

import pandas
import spacy
import pandas as pd
import hashlib
import srsly
from spacy.matcher import Matcher
from beautifultable import BeautifulTable
import re
import openai
OPENAI_API_ORGANIZATION = "org-LoXrXAuJvjt0NRH6zbtHn6kb"
OPENAI_API_KEY = "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"
MODEL_LOCATION = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/shamroq.training-TRAINING.jsonl"



linguisticFeatures = ['TEXT', 'PATTERN', 'SPAN', 'SUBJ', 'VERB', 'OBJECT']
df = pd.DataFrame(columns=linguisticFeatures)
nlp = spacy.load("en_core_web_lg")
patternCfg = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/patterns.jsonl"
patternMMCfg = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/patterns-meta-model.jsonl"
patternPrepPhrCfg = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/patterns-prep-phrases.jsonl"


'''
Adding items to the nlp pipeline
https://spacy.io/usage/processing-pipelines
'''
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
def printShortDepData(text):
    doc = nlp(text)
    SN = 8; TOKEN = 15; POS = 8; TAG = 8; EXPLAIN = 20; HEAD = 15; DEP = 8; CHILD = 15; ANCESTORS = 28; TREE = 20;
    table = BeautifulTable(maxwidth=80)
    table.columns.header = ['SN', 'Text', 'POS', 'TAG', 'HEAD', 'Dep']
    table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
    table.columns.width = [SN, TOKEN, POS, TAG, HEAD, DEP]

    for token in doc:
        table.rows.append([token.i, token.text, token.pos_, token.tag_, token.head.text,
                           token.dep_])
    print(table)
    time.sleep(0)
    return doc

def printDepData(text):
    doc = nlp(text)
    SN = 8; TOKEN = 15; POS = 8; TAG = 8; EXPLAIN = 20; HEAD = 15; DEP = 8; CHILD = 15; ANCESTORS = 28; TREE = 20;
    table = BeautifulTable(maxwidth=165)
    table.columns.header = ['SN', 'Text', 'POS', 'TAG', 'Expln Tag', 'HEAD', 'Dep', 'Expln Dep', 'Child', 'Ancestors', 'Subtree']
    table.set_style(BeautifulTable.STYLE_BOX_ROUNDED)
    table.columns.width = [SN, TOKEN, POS, TAG, EXPLAIN, HEAD, DEP, EXPLAIN, CHILD, ANCESTORS, TREE]

    for token in doc:
        ancestors = [t.text for t in token.ancestors]
        children = [child for child in token.children]
        table.rows.append([token.i, token.text, token.pos_, token.tag_, spacy.explain(token.tag_), token.head.text,
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

def processBACKUPMatcher(text, foundSpanOfText, spanOfPattern):
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
    subject = "EMPTY"; root = "EMPTY"; directObject = "EMPTY"; pattern = foundSpanOfText
    indirectObj = "EMTPY"

    # doc = nlp(foundSpanOfText)
    doc = nlp(text)

    for token in doc:
        # print("TOKEN --> ", token.text)
        time.sleep(0)
        if token.dep_ == "nsubj" and token.head.dep_ == "ROOT":
            subject = token.text
            print("Subject (root head): ", subject)
        elif token.dep_ == "nsubj" and token.head.dep_ == "pcomp":
            subject = token.text
            print("Subject (pcomp): ", subject)
            # print("\n")
        elif token.dep_ == "nsubjpass" and token.head.dep_ == "ROOT":
            subject = token.text
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
            directObject = token.text
            print("Object (root) = ", directObject)
        elif token.dep_ == "dobj" and token.head.dep_ == "xcomp":
            directObject = token.text
            print("Object (xcomp) = ", directObject)
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

    df.loc[len(df.index)] = [text, pattern, spanOfPattern, subject, root, directObject]
    pd.set_option('display.max_rows', None)
    pd.set_option('display.expand_frame_repr', False)
    print("\n----------> Dataframe Results ...\n")
    print(df.iloc[0:500, 1:7])
    return df


def getPP01(nlpDoc):
    ppDictionary = None
    for token in nlpDoc:
        if token.text == "before" and token.head.dep_ == "ROOT":
            subject = token.text
            ppDictionary["subject"] = subject
        elif token.dep_ == "nsubj" and token.head.dep_ == "pcomp":
            subject = token.text
            ppDictionary["subject"] = subject
        elif token.dep_ == "nsubjpass" and token.head.dep_ == "ROOT":
            subject = token.text
            ppDictionary["subject"] = subject
        elif token.pos_ == "VERB" and token.dep_ == "ROOT":
            root = token.text
            ppDictionary["root"] = root
        elif token.tag_ == "MD" and token.head.dep_ == "ROOT" and token.text == "must":
            modality = token.text
            ppDictionary["modality"] = modality
        elif token.dep_ == "dative":
            indirectObj = token.text
            ppDictionary["indirectObj"] = indirectObj
        elif token.dep_ == "dobj" and token.head.dep_ == "ROOT":
            # directObject = token.text
            directObject = list(token.subtree)
            ppDictionary["directObject"] = directObject
        elif token.dep_ == "dobj" and token.head.dep_ == "xcomp":
            # directObject = token.text
            directObject = list(token.subtree)
            ppDictionary["directObject"] = directObject
        else:
            pass


    return ppDictionary


def getPrepositionPredication(label, text):
    predicate_dictionary = None
    doc = nlp(text)
    if label == "preposition_01":
        pass
        # predicate_dictionary = getPP01(doc)
    elif label == "preposition_02":
        pass
        #predicate_dictionary = getPP01(doc)
    elif label == "preposition_03":
        pass

    return predicate_dictionary


def getSVOPredication(text):
    svo_dictionary = {}
    subject = "EMPTY"; modality = "EMPTY"; root = "EMPTY"; indirectObj = "EMTPY"; directObject = "EMPTY";  result = None
    doc = nlp(text)
    for token in doc:
        if token.dep_ == "nsubj" and token.head.dep_ == "ROOT":
            subject = token.text
            svo_dictionary["subject"] = subject
        elif token.dep_ == "nsubj" and token.head.dep_ == "pcomp":
            subject = token.text
            svo_dictionary["subject"] = subject
        elif token.dep_ == "nsubjpass" and token.head.dep_ == "ROOT":
            subject = token.text
            svo_dictionary["subject"] = subject
        elif token.pos_ == "VERB" and token.dep_ == "ROOT":
            root = token.text
            svo_dictionary["root"] = root
        elif token.tag_ == "MD" and token.head.dep_ == "ROOT" and token.text == "must":
            modality = token.text
            svo_dictionary["modality"] = modality
        elif token.dep_ == "dative":
            indirectObj = token.text
            svo_dictionary["indirectObj"] = indirectObj
        elif token.dep_ == "dobj" and token.head.dep_ == "ROOT":
            # directObject = token.text
            directObject = list(token.subtree)
            svo_dictionary["directObject"] = directObject
        elif token.dep_ == "dobj" and token.head.dep_ == "xcomp":
            # directObject = token.text
            directObject = list(token.subtree)
            svo_dictionary["directObject"] = directObject
        else:
            pass

    # linguisticFeatures = ['TEXT' (0), 'PATTERN'(1), 'SPAN'(2), 'SUBJ'(3), 'VERB'(4), 'OBJECT'(5)]
    # Store Results in a data frame

    if indirectObj != "EMTPY":
        print("\n---------GROUNDING-------------(1)")
        print("if ", subject, "(x)", indirectObj, "(y)", directObject, "(z)" "=> [OBL: ", modality, "]", root, "(x, y, z)")
    else:
        print("\n---------GROUNDING-------------(2)")
        print("if ", subject, "(x)", directObject, "(y)", "=> [OBL: ", modality, "]",  root, "(x, y)")

    return svo_dictionary


def getPredicates(label, spanText, origText):
    svoMatch = re.search(r'subj_verb_obj_\d\d', label)
    prepMatch = re.search(r'preposition_\d\d', label)
    predicates = None
    if svoMatch:
        print("Subject Verb [iobj] Object as LABEL <><><>--> ", label)
        print("Subject Verb [iobj] Object as TEXT <><><>--> ", spanText)
        print("Original Text <><><>--> ", origText)
        # predicates = getSVOPredication(text)
        # print("Subject Verb [iobj] Object as dictionary <><><>--> ", predicates)
        time.sleep(1)
    elif prepMatch:
        predicates = getPrepositionPredication(label, spanText)
        # print("Predicates as dictionary ", predicates)
        print("Prepositional Phrases as LABEL <><><>--> ", label)
        print("Prepositional Phrases as TEXT <><><>--> ", spanText)
        print("Original Text <><><>--> ", origText)
        #printDepData(spanText)
        time.sleep(1)
    else:
        pass
    return predicates


def classifySpan(oaim, text):
    doc = nlp(text)
    my_dictionary = {}
    predication = None

    # SpanRule - https://spacy.io/api/spanruler | https://spacy.io/usage/rule-based-matching#spanruler
    for span in doc.spans["ruler"]:
        # y = processMatches(text, span.text, span.label_)
        # my_dictionary[span.label_] = span.text
        # print("Match Found (Label) ", span.label_, "Text: ", span.text, "Predication ", predication)
        print("Match Found (Label) ", span.label_, "Text: ", span.text)
        # print(text)
        getOpenAIResponse(oaim, text)
        # predication = getPredicates(span.label_, span.text, text)
        time.sleep(0)

    # print("DONE.... ")
    # print(doc.spans["ruler"])
    # print(my_dictionary)
    # time.sleep(0)
    # classifyMetaModel(text, df)
    return predication


def initializeModel():
    openai.organization = OPENAI_API_ORGANIZATION
    openai.api_key = OPENAI_API_KEY
    # prints the list of models
    # print("openai.Model.list() Type --> ", type(openai.Model.list()))
    # print(openai.Model.list())
    return openai


def getOpenAIResponse(oaim, text):
    # print("getOpenAIResponse(oaim, regPrompt): ", "\n")
    context = "I want you to act as an attorney. I will give you a section of a regulation."
    openaigoal = "You will split and rephrase each regulation into multiple shorter if/then statements that express one idea."
    supplementalInfo = "You will express each if/then statement in the simple present tense."
    inputTag = "Regulation: "
    regPrompt = context + openaigoal + supplementalInfo + inputTag + text

    response = oaim.Completion.create(
        model="text-davinci-003",
        prompt=regPrompt,
        temperature=.8,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # Extract the generated text from the response
    responseText = response["choices"][0]["text"]
    lines = responseText.strip().split("\n")

    # Remove leading and trailing whitespace from each line
    lines = [line.strip() for line in lines]

    # print("PROMPT: ", regPrompt, "\n")
    # print("RESPONSE :", response["choices"][0]["text"])
    # print("<<<<------------------------------------>>>>>\n\n")
    time.sleep(0)
    return lines


def printJSONL(oaiModel, text):
    prefix = "{\"prompt\": "
    quotationMark = "\""
    completionQuotationMark = "\" "
    promptCompletion = "\\n\\n###\\n\\n"
    separator = ","
    completionKeyword = "\"completion\": "
    openaiOutputList = getOpenAIResponse(oaiModel, text)
    openaiOutputString = " ".join(openaiOutputList)
    endKeyWord = " END\"}"

    print(prefix + quotationMark + text + promptCompletion + quotationMark + separator +
          completionKeyword + completionQuotationMark + openaiOutputString + endKeyWord)

    return openaiOutputString


def getHashOfText(inputText):
    # Create a hash object
    hash_object = hashlib.md5()
    # Hash the string
    hash_object.update(inputText.encode())
    # Get the hexadecimal representation of the hash
    hash_value = hash_object.hexdigest()
    return hash_value


def loadDataFrame(hashValue, text, openAIResult, dfs):
    data = [{'promptID': hashValue,
             'promptText': text,
             'completion': openAIResult,
             'changes': None,
             'comments': None,
             'open1': None,
             'open2': None
             }]
    dfObject = pd.DataFrame(data)
    # Remove the empty string
    dfObject = dfObject[dfObject.completion != ""]
    dfs = pd.concat([dfs, dfObject], ignore_index=True)

    print(dfs[["promptID", "promptText", "completion"]])
    time.sleep(0)
    return dfs


def processEachProvision(openAIModel, params, dfStore):

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
                        # print("|                       |")
                        # print("|   Evaluate Statement  |")
                        # print("|                       |")

                        # print(text)
                        # printShortDepData(text)
                        # printJSONL(openAIModel, text)
                        openAIResult = printJSONL(openAIModel, text)
                        hashValue = getHashOfText(text)
                        dfStore = loadDataFrame(hashValue, text, openAIResult, dfStore)
                        # classifySpan(openAIModel, text)
                        # printShortDepData(text)
                        # print("<<<<------------------------------------>>>>>\n\n")
                        time.sleep(0)

                        '''
                        ---> Process the MetaModel
                        '''
                        # classifyMetaModel(text)
                        # print("Text... classifyMetaModel", text)

    return dfStore


def initializeDataFrame():
    # Define the column names
    column_names = ["promptID", "promptText", "completion", "changes", "comments", "open1", "open2"]
    # Load the list of lines into a DataFrame
    iDF = pd.DataFrame(columns=column_names)

    # Change the display options to show more text
    pd.set_option('max_colwidth', 80)
    print(" <><><><> INIT dataframe <><><><>")
    print(iDF)
    time.sleep(0)
    return iDF




def init(inputDict):
    regulation = inputDict
    myOpenai = initializeModel()
    dfReg = initializeDataFrame()
    outputDF = processEachProvision(myOpenai, regulation, dfReg)

    # Define the file name and path
    file_name = "data.csv"

    # Write the DataFrame to a CSV file
    outputDF.to_csv(file_name, index=False)
    return regulation
