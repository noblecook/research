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
    
    
def preProcessorRights():

    right01 = word_tokenize('has a right to')
    right02 = word_tokenize('has the right to')
    right03 = word_tokenize('retains the right to')
    r1Tagged = nltk.pos_tag(right01)
    print (r1Tagged)
    r2Tagged = nltk.pos_tag(right02)
    print (r2Tagged)
    r3Tagged = nltk.pos_tag(right03)
    print (r3Tagged)

def preProcessorObligations():

    obligation01 = word_tokenize('must')
    obligation02 = word_tokenize('is required to')
    obligation03 = word_tokenize('shall')
    obligation04 = word_tokenize('may not')
    obligation05 = word_tokenize('is prohibited')
    obligation06 = word_tokenize('is subject to')
    
    obj1Tagged = nltk.pos_tag(obligation01)
    print (obj1Tagged)
    obj2Tagged = nltk.pos_tag(obligation02)
    print (obj2Tagged)
    obj3Tagged = nltk.pos_tag(obligation03)
    print (obj3Tagged)
    obj4Tagged = nltk.pos_tag(obligation04)
    print (obj4Tagged)
    obj5Tagged = nltk.pos_tag(obligation05)
    print (obj5Tagged)
    obj6Tagged = nltk.pos_tag(obligation06)
    print (obj6Tagged)



def main():
    preProcessorObligations()
        
if __name__ == "__main__": 
    # calling main function 
    main() 


