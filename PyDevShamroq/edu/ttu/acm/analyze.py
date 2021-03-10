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
import time
       
        
'''
The driver method takes a 'list' datatype that contains 1 or more xml files
The xml files are representative of one section in the code of federal regulations (CFR).
The for loop reads each regulation, starting at index 0, and passes it to 
scanner.  The results of the scanner 

'''    

def init(regulation): 
    print("... starting Analyze")
    xmlData = scan.init(regulation)
    preProcessResults = preprocessor.init(xmlData, regulation)
    cleanRegulations = clean.sanitize(preProcessResults)
    print(cleanRegulations)
    time.sleep(1000000)
    return cleanRegulations 



