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
import string


'''
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
import xml.etree.ElementTree as etree 
import rdflib
import time
import sys
import codecs



g = rdflib.Graph()
REGULATION = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_cfrtitle')
has_CFRTITLE = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_cfrtitle')
has_CFRTITLETEXT = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_cfrtitletext')
has_VOL = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_vol')
has_DATE = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_date')
has_ORIGINALDATE = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_originaldate')
has_COVERONLY = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_coveronly')
has_TITLE = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_title')
has_GRANULENUM = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_granulenum')
has_HEADING = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_heading')
has_ANCESTORS = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_ancestors')
has_PARENT = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_parent')
has_PARENT_HEADING = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_parent_heading')
has_PARENT_SEQUENCE = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_parent_sequence')


'''
inauguaral 
DBPedia
GeoNames
FOAF
Dublin Core
'''

FILEPREFIX = 'C:/Users/patri/git/research/PyDevShamroq/data/'

'''Food and Drug'''
xml_21_CFR_Section_11_10 = FILEPREFIX+'xml_21_CFR_Section_11_10.xml'
xml_21_CFR_Section_11_30 = FILEPREFIX+'xml_21_CFR_Section_11_30.xml'

'''Public Welfare'''
xml_45_CFR_Section_164_510 = FILEPREFIX+'xml_45_CFR_Section_164_510.xml'
xml_45_CFR_Section_164_520 = FILEPREFIX+'xml_45_CFR_Section_164_520.xml'
xml_45_CFR_Section_164_522 = FILEPREFIX+'xml_45_CFR_Section_164_522.xml'
xml_45_CFR_Section_164_524 = FILEPREFIX+'xml_45_CFR_Section_164_524.xml'
xml_45_CFR_Section_164_526 = FILEPREFIX+'xml_45_CFR_Section_164_526.xml'

'''Public Welfare'''
xml_45_CFR_Section_164_306 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-306.xml'
xml_45_CFR_Section_164_310 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-310.xml'
xml_45_CFR_Section_164_312 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-312.xml'
xml_45_CFR_Section_164_314 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-314.xml'

'''
In next revision, read this list from a file
'''
regList = [xml_21_CFR_Section_11_10, xml_21_CFR_Section_11_30, xml_45_CFR_Section_164_510, 
               xml_45_CFR_Section_164_520, xml_45_CFR_Section_164_522, xml_45_CFR_Section_164_524,
               xml_45_CFR_Section_164_526, xml_45_CFR_Section_164_306, xml_45_CFR_Section_164_310, 
               xml_45_CFR_Section_164_312, xml_45_CFR_Section_164_314]

xml_45_306 = FILEPREFIX+'CFR45-164-306.xml'
regListSingle = [xml_45_CFR_Section_164_510]

def pauseForTheCause ():
    time.sleep(5)

def getXMLData(node):
    if node != None:
        try:
            print('node.tag: ', node.tag)
            print('node.attrib: ', node.attrib)         
            try:
                '''
                There is an issue printing the $(<E T="03">1</E>) trailing information. The initial 
                observation is that the parser is not recognizing the CLOSING tags...
                As an example, <P>(a) <E T="03">General requirements.</E> Covered entities and business 
                associates must do the following:</P> only General requirements are printed - and not the 
                Covered entities statements. 
                '''
                if (node.tag == 'P'):
                    innerText = ''.join(node.itertext())
                    print('node.itertext(): ' + innerText)
                else:
                    print('node.text: ', node.text)
            except:
                '''
                The utf-8 encoder/decoder addresses the "unicodeencodeerror 'charmap' codec can't 
                encode character ' u\2009'.  The unicodeencodeerror was a byproduct of an "Thin Space"
                Unicode Character that was embedded in the xml file during the download. The character
                set is an "a-hat" followed by Euro-currency, followed by 0/00
                Example:   (U+2009) (thin space)
                
                Question:  
                (1) Why encode in utf-8, then decode with sys.stdout.encoding?
                (2) Is there another way to do this?
                '''
                #print('-->Exception<--: - node.text: ', node.text.encode('utf-8').decode(sys.stdout.encoding))
                innerText = ''.join(node.itertext())
                print('-->Exception<--: - node.text: ' + innerText.encode('utf-8').decode(sys.stdout.encoding))
                print('\n')
        except:
            print("Unexpected error 0:", sys.exc_info()[0])
            print("Unexpected error 1:", sys.exc_info()[1])
            print("Unexpected error 2:", sys.exc_info()[2])            
            print('\n')
            pauseForTheCause()
        for item in node:
            getXMLData(item)
    else:
        return 0

def getRootNode(listOfRegulations): 
    for regulation in listOfRegulations:
        tree = etree.parse(regulation)
        rootNode = tree.getroot()
        return rootNode    
  
def main(): 
    root = getRootNode(regListSingle) 
    getXMLData(root)  
    print("preProcessor() ------> Done!")
    
    
if __name__ == "__main__": 
    # calling main function 
    main() 


