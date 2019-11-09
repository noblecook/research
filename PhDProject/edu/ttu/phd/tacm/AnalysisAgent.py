'''
Created on Dec 8, 2018
@author: Patrick Cook
Analysis Agent 

This files parses a sentence. 
'''
import nltk
from nltk.tokenize import PunktSentenceTokenizer

#this data has special characters in it. 

reg = "Persons who use open systems to create, modify, maintain, or transmit electronic records shall employ procedures and controls designed to ensure the authenticity, integrity, and, as appropriate, the confidentiality of electronic records from the point of their creation to the point of their receipt. Such procedures and controls shall include those identified in 11.10, as appropriate, and additional measures such as document encryption and use of appropriate digital signature standards to ensure, as necessary under the circumstances, record authenticity, integrity, and confidentiality."
reg1= "Except when an objection is expressed in accordance with paragraphs (a)(2) or (3) of this section, a covered health care provider may: (i) Use the following protected health information to maintain a directory of individuals in its facility: The individual's name;"


def tokenizeWords (words):
    tokenized = nltk.sent_tokenize(str) 
    print(tokenized);   
    
def partOfSpeechTagging (text):
    tokenized = nltk.sent_tokenize(str) 
    print(tokenized);   
        
def chunkingNamedEntities (str):
    tokenized = nltk.sent_tokenize(str) 
    print("--------preProcessor:  nltk.word_tokenize & TAGGED--------\n", tokenized);   
    
    #take the text through the NLP pipeline
def preProcessor (str):
    tokenized = nltk.word_tokenize(str) 
    tagged = nltk.pos_tag(tokenized);
    print("--------preProcessor:  nltk.word_tokenize & TAGGED--------\n", tagged);

def tokenizeSentences (sents):
    trainingSet = PunktSentenceTokenizer()
    print("--------tokenizeSentences: PunktSentenceTokenizer--------\n", trainingSet.tokenize(sents));
    

def main(): 
    # load regulations from file 
    tokenizeSentences(reg1) 
    print(" ");
    preProcessor(reg1)
    print(" ");
    chunkingNamedEntities (reg1)

      
      
if __name__ == "__main__": 
    # calling main function 
    main() 
