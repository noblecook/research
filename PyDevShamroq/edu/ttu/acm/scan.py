

import xml.etree.ElementTree as etree 



def readTextFile(textFile):
    textFileHandler = open(textFile, 'r').read();
    return textFileHandler;


def readXMLFile(xmlFile): 
    print('Filename  ------> ' + xmlFile + '\n')
    tree = etree.parse(xmlFile)
    rootNode = tree.getroot()
    return rootNode;
