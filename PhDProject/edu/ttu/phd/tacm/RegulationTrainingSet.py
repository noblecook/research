'''
Created on Dec 8, 2018
@author: Patrick Cook
Model Agent 

/*
    Main application to read the government regulations from the file and parse the information.
*/
'''
import xml.etree.ElementTree as etree 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import rdflib
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
DBPedia
GeoNames
FOAF
Dublin Core
'''

SIMPLE = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/simple.xml'

XML_10_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_10_CFR_ALL.xml'
XML_20_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_20_CFR_ALL.xml'
XML_30_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_30_CFR_ALL.xml'
XML_46_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_46_CFR_ALL.xml'
XML_47_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_47_CFR_ALL.xml'
XML_48_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_48_CFR_ALL.xml'
XML_49_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_49_CFR_ALL.xml'
XML_50_CFR_ALL = 'C:/Users/patcoo\git/research/PhDProject/data/XML_50_CFR_ALL.xml'

xml_21_CFR_Section_11_10 = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/xml_21_CFR_Section_11_10.xml'
xml_21_CFR_Section_11_30 = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/xml_21_CFR_Section_11_30.xml'
xml_45_CFR_Section_164_522 = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/xml_45_CFR_Section_164_522.xml'
xml_45_CFR_Section_164_510 = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/xml_45_CFR_Section_164_510.xml'



def getXMLData(node):
    if node != None:
        try:
            print('node.tag: ', node.tag)
            print('node.attrib: ', node.attrib)
            print('node.text: ', node.text)
            print('\n')
        except:
            print('--------------------->>>> could not print text')
        for item in node:
            getXMLData(item)
    else:
        return 0
    
def main(): 

    tree = etree.parse(xml_45_CFR_Section_164_510)
    root = tree.getroot()
    getXMLData(root)
    print (g)
    
if __name__ == "__main__": 
    # calling main function 
    main() 


