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
import preprocessor
import clean

'''
The driver method takes a 'list' datatype that contains 1 or more xml files
The xml files are representative of one section in the code of federal regulations (CFR).
The for loop reads each regulation, starting at index 0, and passes it to 
scanner.  The results of the scanner 

'''
def init_old(regulation):
    print("... starting Analyze")

    # scan.init() returns a nested xml structure and stores in xmlData
    xmlData = scan.init(regulation)

    # preprocessor.init() returns a dictionary of the xml version of the CFR
    preProcessResults = preprocessor.init(xmlData, regulation)

    # clean.sanitize() returns a structured dictionary
    cleanRegulations = clean.sanitize(preProcessResults)
    return cleanRegulations


def init(scannedFile):
    print("... starting Analyze")
    pass
