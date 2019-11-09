'''
Created on Dec 8, 2018
@author: Patrick Cook
Model Agent 
As an Element, root has a tag and a dictionary of attributes:
'''
import xml.etree.ElementTree as etree 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import time
import rdflib
import nltk
from rdflib import Namespace, URIRef, BNode, Literal
from nltk.tokenize import PunktSentenceTokenizer, word_tokenize, sent_tokenize

g = rdflib.Graph()
n = Namespace("http://www.shamroq.pcook.ttu.edu")

REG_21_CFR_11_10 = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/reg_21_cfr_11_10')
REG_21_CFR_11_30 = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/reg_21_cfr_11_30')
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
has_SECTION = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_section')
has_SECTNO = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_sectno')
has_SUBJECT = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_subject')
has_PARAGRAPH = rdflib.URIRef('http://www.shamroq.pcook.ttu.edu/has_paragraph')


'''
DBPedia
GeoNames
FOAF
Dublin Core
'''

SIMPLE = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/simple.xml'
FILEPREFIX = 'C:/Users/patcoo/git/research/PhDProject/data/'

XML_10_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_10_CFR_ALL.xml'
XML_20_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_20_CFR_ALL.xml'
XML_30_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_30_CFR_ALL.xml'
XML_46_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_46_CFR_ALL.xml'
XML_47_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_47_CFR_ALL.xml'
XML_48_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_48_CFR_ALL.xml'
XML_49_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_49_CFR_ALL.xml'
XML_50_CFR_ALL = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/XML_50_CFR_ALL.xml'

xml_21_CFR_Section_11_10 = FILEPREFIX+'xml_21_CFR_Section_11_10.xml'
xml_45_CFR_Section_11_10 = FILEPREFIX+'xml_45_CFR_Section_164_510.xml'
xml_21_CFR_Section_11_30 = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/xml_21_CFR_Section_11_30.xml'



 
def getXML(node):
    if node != None:
        try:
            if node.tag == 'FDSYS':
                print('node.tag ---------------->>> ', node.tag)
            if node.tag == 'CFRTITLE':
                print('CFRTITLE ---------------->>> ')
                CFRTITLE_Literal = rdflib.Literal(node.text)
                g.add((REG_21_CFR_11_10,has_CFRTITLE,CFRTITLE_Literal))
            if node.tag == 'CFRTITLETEXT':
                print('CFRTITLETEXT ---------------->>> ')
                CFRTITLETEXT_Literal = rdflib.Literal(node.text)
                g.add((REG_21_CFR_11_10,has_CFRTITLETEXT,CFRTITLETEXT_Literal))
            if node.tag == 'VOL':
                print('VOL FOUND ---------------->>> ')
                VOL_Literal = rdflib.Literal(node.text)
                g.add((REG_21_CFR_11_10,has_VOL,VOL_Literal))
            if node.tag == 'DATE':
                print('DATE FOUND ---------------->>> ')
                DATE_Literal = rdflib.Literal(node.text)
                g.add((REG_21_CFR_11_10,has_DATE,DATE_Literal))
            if node.tag == 'ORIGINALDATE':
                print('ORIGINALDATE FOUND ---------------->>> ')
                ORIGINALDATE_Literal = rdflib.Literal(node.text)
                g.add((REG_21_CFR_11_10,has_ORIGINALDATE,ORIGINALDATE_Literal))
            if node.tag == 'COVERONLY':
                print('COVERONLY FOUND ---------------->>> ')
                COVERONLY_Literal = rdflib.Literal(node.text)
                g.add((REG_21_CFR_11_10,has_COVERONLY,COVERONLY_Literal))
            if node.tag == 'TITLE':
                print('TITLE FOUND ---------------->>> (please REMOVE period ')
                TITLE_Literal = rdflib.Literal(node.text)
                g.add((REG_21_CFR_11_10,has_TITLE,TITLE_Literal))
            if node.tag == 'GRANULENUM':
                print('GRANULENUM FOUND ---------------->>> ')
                GRANULENUM_Literal = rdflib.Literal(node.text)
                g.add((REG_21_CFR_11_10,has_GRANULENUM,GRANULENUM_Literal))
            if node.tag == 'HEADING':
                print('HEADING FOUND ---------------->>> ')
                HEADING_Literal = rdflib.Literal(node.text)
                g.add((REG_21_CFR_11_10,has_HEADING,HEADING_Literal))
            if node.tag == 'ANCESTORS':
                print('ANCESTORS FOUND ---->>> ')
            if node.tag == 'PARENT':
                print('PARENT FOUND ---------------->>> ')                           
                PARENT_HEADING_ATTRIBUTE = rdflib.Literal(node.attrib)
                g.add((REG_21_CFR_11_10,has_PARENT_HEADING,PARENT_HEADING_ATTRIBUTE))
                PARENT_HEADING_Literal = rdflib.Literal(node.text)                
                g.add((REG_21_CFR_11_10,has_PARENT_HEADING,PARENT_HEADING_Literal))
            if node.tag == 'SECTION':
                print('SECTION FOUND ---------------->>> ')
            if node.tag == 'SECTNO':
                print('SECTNO FOUND ---------------->>> ')
                SECTNO = rdflib.Literal(node.text)
                g.add((REG_21_CFR_11_10,has_SECTNO,SECTNO))
            if node.tag == 'SUBJECT':
                print('SUBJECT FOUND ---------------->>> ')
                SUBJECT = rdflib.Literal(node.text)
                g.add((REG_21_CFR_11_10,has_SUBJECT,SUBJECT))
            if node.tag == 'P':
                print('PARAGRAPH FOUND ---------------->>> ')
                PARAGRAPH = rdflib.Literal(node.text)                
                print(node.text)
                time.sleep(1)
                g.add((REG_21_CFR_11_10,has_PARAGRAPH,PARAGRAPH))
        except:
            print('--------------------->>>> could not print text')
        for item in node:
            getXML(item)
    else:
        return 0
    
    
def preProcessor(text):

    tokenized = sent_tokenize(text)
    try:
        for i in tokenized:
            words = nltk.word_tokenize(i)
            tagged = nltk.pos_tag(words)
            '''
                Examples - 
                (1)  has a right to
                (2)  has the right to
                (3)  retains the right to
                
            '''
            
            chunkGram = r"""Chunk: {<RB.?>*<VB.?>*<NNP>}"""
            chunkParser = nltk.RegexpParser(chunkGram)

            chunked = chunkParser.parse(tagged)
            print(chunked)
            #chunked.draw()
            

    except Exception as e:
        print(str(e))   

def main(): 
    tree = etree.parse(xml_45_CFR_Section_11_10)
    root = tree.getroot()
    getXML(root)
    
    #text = 'Persons who use closed systems to create, modify, maintain, or transmit electronic records shall employ procedures and controls designed to ensure the authenticity, integrity, and, when appropriate, the confidentiality of electronic records, and to ensure that the signer cannot readily repudiate the signed record as not genuine. Such procedures and controls shall include the following:'
    #preProcessor(text)
    
    
    print('Triples in graph after add: ', len(g))
    # display the graph in RDF/XML
    print(g.serialize(format="nt"))
    
    '''
    
    print("--- printing raw triples ---")
    for subj, pred, obj in g:
        print (subj, pred, obj)
    
        # Serialize as XML
    print("--- start: rdf-xml ---")
    print(g.serialize(format="pretty-xml"))
    print("--- end: rdf-xml ---\n")

    # Serialize as Turtle
    print("--- start: turtle ---")
    print(g.serialize(format="turtle"))
    print("--- end: turtle ---\n")

    # Serialize as NTriples
    print("--- start: ntriples ---")
    print(g.serialize(format="nt"))
    print("--- end: ntriples ---\n")
    
     # close when done, otherwise sleepycat will leak lock entries.
    g.close()
    '''
    
if __name__ == "__main__": 
    # calling main function 
    main() 


