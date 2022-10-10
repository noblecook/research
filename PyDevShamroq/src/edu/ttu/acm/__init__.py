import time
import xmlschema

import analyze
import classify
import model
import relationExtractor
import scan
import preprocessor
import clean
import requests
from relationExtractor import *
from spacy import displacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
nlp = spacy.load("en_core_web_sm")
encoding = 'utf-8'




FILE_PREFIX_COPPA = 'C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/coppa/'
FILE_PREFIX_HIPAA = 'C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/hipaa/'
FILE_PREFIX_GLBA = 'C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/glba/'

# parent site for the regulations - https://www.govinfo.gov/


xml_45_164_306 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-306.xml'
xml_45_164_310 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-310.xml'
xml_45_164_312 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-312.xml'
xml_45_164_510 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-510.xml'

xml_16_132_002 = FILE_PREFIX_COPPA + 'CFR-2020-title16-vol1-sec312-2.xml'
xml_16_132_004 = FILE_PREFIX_COPPA + 'CFR-2020-title16-vol1-sec312-4.xml'
xml_16_132_005 = FILE_PREFIX_COPPA + 'CFR-2020-title16-vol1-sec312-5.xml'
xml_16_132_011 = FILE_PREFIX_COPPA + 'CFR-2020-title16-vol1-sec312-11.xml'
xml_16_132_ALL = FILE_PREFIX_COPPA + 'CFR-2020-title16-vol1-part312.xml'

xml_16_313_009 = FILE_PREFIX_GLBA + 'CFR-2020-title16-vol1-sec312-5.xml'


# regList = [xml_45_164_306, xml_45_164_310, xml_45_164_312, xml_45_164_510]

#regList = [xml_16_132_002, xml_16_132_004, xml_16_132_005, xml_16_132_011, xml_45_164_306, xml_45_164_310, xml_45_164_312, xml_45_164_510]
regList = [xml_16_132_005, xml_16_313_009, xml_45_164_510]


def getTimeNow():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Current Time =", current_time)
    return t


def shamroq(listOfRegulations):
    requirements = []
    getTimeNow()
    for regulation in listOfRegulations:
        # scan.init()
        # input  = "regulation", a string of the xml file location;
        # output = "scannedResults" a xml.etree.ElementTree.Element dataType;
        # ------>  10/5/22 add a debug flag to dynamically print portions if true
        # print("scannedResults is of type ", type(scannedResults));
        # time.sleep(100)
        scannedResults = scan.init(regulation)

        # preprocessor.init()
        # input 1 = "scannedResults", an xml.etree.ElementTree.Element dataType
        # input 2 = "regulation", a string of the file location;
        # output = "preProcessedResults" a dictionary of the CFR regulation
        # print("preProcessedResults is of type ", python Dictionary );
        # print("regulation is of type ", String);
        preProcessedResults = preprocessor.init(scannedResults, regulation)
        for key, value in preProcessedResults.items():
            print("key---------->", key)
            #time.sleep(1)
            print("value-------->", value, "\n\n")
            #time.sleep(3)


        # clean.init() returns a structured dictionary
        # cleanedResults = clean.init(preProcessedResults)




        # classify.init()
        # input => dictionary of x;
        # output => list
        # Option 1) use nltk, work tokenized, POS tagging, and chunking [ CURRENT ]
        # Option 2) use spacy and textacy 
        # List the pros and cons of each; then what I used and why
        # ----- THIS IS REALLY ANALYZE ------
        # ----- Build another class to use Spacy and Textacy ------
        '''
        classificationResults = classify.init(cleanedResults)
        for line in classificationResults:
            print(line)
            time.sleep(3)

        # ----- HERE WE WILL USE OWLREADY2 ------
        # ----- Build another class to use Spacy and Textacy ------
        # model.init() input = list of x; output = list
        # model.init(cleanedResults, classificationResults)
        '''
    time.sleep(5)

    getTimeNow()
    return requirements


def main():
    print("Number of regulations -->", len(regList))
    print("/------------------------------------------/")
    print("... starting main()")
    print("/------------------------------------------/")
    print("\n")
    shamroq(regList)

    time.sleep(100000)

    #validating LRML
    test = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/lrml/compact/lrml-compact.xsd"

    try:
        schema = xmlschema.XMLSchema11(test)
        print(schema.is_valid(test));
    except:
        print("Failed - please try again")

    print("\n")
    print("/------------------------------------------/")
    print("... completing main()")
    print("/------------------------------------------/")


if __name__ == '__main__':
    main()



'''
 for key, value in preProcessedResults.items():
            print(key)
            time.sleep(3)
            print(value)
            time.sleep(3)
'''