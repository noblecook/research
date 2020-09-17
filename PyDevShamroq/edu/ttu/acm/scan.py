

import xml.etree.ElementTree as etree 
import time


def readTextFile(textFile):
    textFileHandler = open(textFile, 'r').read();
    return textFileHandler;


def readXMLFile(xmlFile): 
    #print('Filename  ------> ' + xmlFile + '\n')
    tree = etree.parse(xmlFile)
    rootNode = tree.getroot()
    return rootNode;

'''
The scanner receives as input an xml file.  In this instance, the xml file
represents a section of the code of federal regulations (CFR).  the xml files
is processed for programmatic use and stored in a "tree" data structure
'''

def init(file): 
    print("... starting Analyze.scan()")
    time.sleep(0)
    rootNode = readXMLFile(file)
    return rootNode;
