import time
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
    ''' 
    # rootNode.findall(".") returns the top most element: CFRGRANULE
    # rootNode.findall("./") returns the two main elements:  (1) FDSYS; (2) SECTION
    # rootNode.findall(".//") returns everything (elements and sub elements) under CFRGRANULE
    # rootNode.findall("./SECTION//P/*") returns the "E" sublements
    # rootNode.findall("./SECTION//*") returns the "P" and "E" tags - but skips the text after "E"

    for paragraph in rootNode.findall("./SECTION//*"):
        if paragraph.tag == 'P':
            innerText = ''.join(paragraph.itertext())
            print(innerText)
        elif paragraph.tag == 'E':
            pass
        else:
            print(paragraph.text)
        time.sleep(0)
    time.sleep(0)
    '''

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
