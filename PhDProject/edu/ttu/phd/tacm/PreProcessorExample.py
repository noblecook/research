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
import re
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
xml_21_CFR_Section_11_30 = FILEPREFIX+'xml_21_CFR_Section_11_30.xml'



 
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
                preProcessor(node.text)
                time.sleep(20)
                print('done')
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
                Rights - 
                (1)  has a right to:  [('has', 'VBZ'), ('a', 'DT'), ('right', 'NN'), ('to', 'TO')]
                (2)  has the right to: [('has', 'VBZ'), ('the', 'DT'), ('right', 'NN'), ('to', 'TO')]
                (3)  retains the right to: [('retains', 'VBZ'), ('the', 'DT'), ('right', 'NN'), ('to', 'TO')]
                
                Obligations - 
                (1) [('must', 'MD')]
                (2) [('is', 'VBZ'), ('required', 'VBN'), ('to', 'TO')]
                (3) [('shall', 'MD')]
                (4) [('may', 'MD'), ('not', 'RB')]
                (5) [('is', 'VBZ'), ('prohibited', 'VBN')]
                (6) [('is', 'VBZ'), ('subject', 'JJ'), ('to', 'TO')]

                
                regular expressions:  
                    ? = 0 or 1 repetitions
                    * = 0 or more repetitions
                    + = 1 or more repetitions
                    . = any character except a newline
            '''
            legalChunkGram1 = r"""LEGAL Chunk (RIGHT) --->: {<VBZ>+<DT>+<NN>+<TO>}"""
            
            legalChunkGram2 = r"""
                LEGAL Chunk (RIGHT) --->: {<VBZ>+<DT>+<NN>+<TO>} 
                LEGAL Chunk (OBLIGATION) --->: {<MD>+}  
                LEGAL Chunk (OBLIGATION) --->: {<VBZ>+<VBN>+<TO>} 
                LEGAL Chunk (OBLIGATION) --->: {<MD>+<RB>+} 
                LEGAL Chunk (OBLIGATION) --->: {<VBZ>+<VBN>+} 
                LEGAL Chunk (OBLIGATION) --->: {<VBZ>+<JJ>+<TO>} 
            """
            legalChunkGram3 = r"""
              NP: {<DT|PP\$>?<JJ>*<NN>}   # chunk determiner/possessive, adjectives and nouns
                  {<NNP>+}                # chunk sequences of proper nouns
            """
                
            legalChunkGram4 = r"""
              NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
              PP: {<IN><NP>}               # Chunk prepositions followed by NP
              VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
              CLAUSE: {<NP><VP>}           # Chunk NP, VP
              """
            
            
            legalChunkParser = nltk.RegexpParser(legalChunkGram4)
            legalChunked = legalChunkParser.parse(tagged)
            print(legalChunked)
            time.sleep(555)
            #chunked.draw()
            

    except Exception as e:
        print(str(e))   

def main(): 
    tree = etree.parse(xml_21_CFR_Section_11_10)
    root = tree.getroot()
    getXML(root)
    
    text = 'Persons who use closed systems to create, modify, maintain, or transmit electronic records shall employ procedures and controls designed to ensure the authenticity, integrity, and, when appropriate, the confidentiality of electronic records, and to ensure that the signer cannot readily repudiate the signed record as not genuine. Such procedures and controls shall include the following:'
    rightText = "Except as provided by paragraph (a)(2) or (3) of this section, an individual has a right to adequate notice of the uses and disclosures of protected health information that may be made by the covered entity, and of the individual's rights and the covered entity's legal duties with respect to protected health information."
    obligationText = "In accordance with 164.514(f)(1), the covered entity may contact the individual to raise funds for the covered entity and the individual has a right to opt out of receiving such communications; (B) In accordance with 164.504(f), the group health plan, or a health insurance issuer or HMO with respect to a group health plan, may disclose protected health information to the sponsor of the plan; or"
    preProcessor(obligationText)
    
    
if __name__ == "__main__": 
    # calling main function 
    main() 



