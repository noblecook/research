'''
Created on Dec 8, 2018
@author: Patrick Cook
Model Agent 

/*
    Main application to read the government regulations from the file and parse the information.
    
    Parsing the Regulation - https://docs.python.org/2/library/xml.etree.elementtree.html
    Here, we used the "Element" type - a container object that stores hierarchial data structures
    The ElementTree wraps an element structure, and convert it from and to XML.
    The ElementTree represents the ENTIRE document as a tree structure, whereas, the Element
    represents a single node in the tree.  Therefore, use ElementTree to read and write to files.
    To interact with an element and subelements use the Element level 
*/
'''

import scan
import preprocess
import clean
import time
import classify
'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt, word_tokenize 

'''
FILEPREFIX = 'C:/Users/patri/git/research/PyDevShamroq/data/'
xml_45_164_306 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-306.xml'
xml_45_164_310 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-310.xml'
xml_45_164_312 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-312.xml'
xml_45_164_510 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-510.xml'
#regListSingle = [xml_45_164_306, xml_45_164_310, xml_45_164_312, xml_45_164_510]
regListSingle = [xml_45_164_510]

def printData(dictionaryResult):
    for key, value in dictionaryResult.items():
        print("Key:", key)       
        for nestedCategory in value:
            print ('   ' + nestedCategory + ' : ', value[nestedCategory])
            time.sleep(0)
          
def driver(listOfRegulations): 
    print('Number of Regulations ---------> ' , len(regListSingle))
    for regulation in listOfRegulations:
        xmlData = scan.init(regulation)
        preProcessResults = preprocess.init(xmlData, regulation)
        cleanResults = clean.init(preProcessResults)
        #printData(cleanResults)
        classifyResults = classify.init(cleanResults)
        #printData(classifyResults)

def main(): 
    print("... starting analyze")
    time.sleep(1)
    driver(regListSingle) 
    print("preProcessor() ------> Done!")
    
    
if __name__ == "__main__": 
    # calling main function 
    main() 


