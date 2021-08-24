
import xml.etree.ElementTree as eTree


def readInJSON(textFile):
    textFileHandler = open(textFile, 'r').read()
    return textFileHandler


def readInText(textFile):
    textFileHandler = open(textFile, 'r').read()
    return textFileHandler


def readInXML(xmlFile):
    tree = eTree.parse(xmlFile)
    rootNode = tree.getroot()
    return rootNode

'''
The scanner receives as input an xml file.  In this instance, the xml file
represents a section of the code of federal regulations (CFR).  the xml files
is processed for programmatic use and stored in a "tree" data structure
More on eTree in python - https://docs.python.org/3/library/xml.etree.elementtree.html 
'''


def init(file): 
    print("... Starting scan.init()")
    rootNode = readInXML(file)
    return rootNode
