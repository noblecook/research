'''
Created on Dec 8, 2018
@author: Patrick Cook
Analysis Agent 
'''
import nltk
from nltk.tokenize import PunktSentenceTokenizer

#this data has special characters in it. 

reg = "Persons who use open systems to create, modify, maintain, or transmit electronic records shall employ procedures and controls designed to ensure the authenticity, integrity, and, as appropriate, the confidentiality of electronic records from the point of their creation to the point of their receipt. Such procedures and controls shall include those identified in 11.10, as appropriate, and additional measures such as document encryption and use of appropriate digital signature standards to ensure, as necessary under the circumstances, record authenticity, integrity, and confidentiality."

  
def tokenizeSentences (sents):
    trainingSet = PunktSentenceTokenizer()
    print(trainingSet);
    
def tokenizeWords (words):
    tokenized = nltk.sent_tokenize(str) 
    print(tokenized);   
    
def partOfSpeechTagging (text):
    tokenized = nltk.sent_tokenize(str) 
    print(tokenized);   
        
def chunkingNamedEntities (nounPhrases):
    tokenized = nltk.sent_tokenize(str) 
    print(tokenized);   
    
    #take the text through the NLP pipeline
def preProcessor (str):
    tokenized = nltk.word_tokenize(str) 
    tagged = nltk.pos_tag(tokenized);
    print(tagged);


def main(): 
    # load regulations from file 
    tokenizeSentences(reg) 

      
      
if __name__ == "__main__": 
    # calling main function 
    main() 
