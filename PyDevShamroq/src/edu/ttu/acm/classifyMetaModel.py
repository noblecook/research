import time
import spacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

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
                        processGrounding(text)
            print("\n\n\n FINISHED\n\n\n")
        time.sleep(3)


def processGrounding(text):
    '''print Token type and attributes'''
    doc = nlp(text)
    for token in doc:
        print(token.text, token.pos_, token.tag_, token.dep_,token.is_stop)
        time.sleep(2)


def getMetalModel(inputDictionary):
    resultMM = inputDictionary
    return resultMM


def init(inputDict):
    metaModel = inputDict
    printEachProvision(metaModel)
    return metaModel
