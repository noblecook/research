

import xml.etree.ElementTree as etree 
import time


def readTextFile(textFile):
    textFileHandler = open(textFile, 'r').read();
    return textFileHandler;


def readXMLFile(xmlFile): 
    print('Filename  ------> ' + xmlFile + '\n')
    tree = etree.parse(xmlFile)
    rootNode = tree.getroot()
    return rootNode;

def init(xmlFile): 
    print("... starting scan")
    time.sleep(1)
    rootNode = readXMLFile(xmlFile)
    return rootNode;
