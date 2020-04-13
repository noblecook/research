"""

Pandas - what are the libraries in here?


"""
from nltk.book import *

def section01():
    text3.generate()

def lexical_diversity(someText):
    '''
     lexical diversity = (lenth of the set) /(length of text)
     (1) the set(obj) function return distinct tokens
     (2) the len(obj) function returns all tokens
     
    '''
    return len(set(someText)) / len(someText) 
    
def countingVocabulary(textToCount):
    _lenthOftheSet = len(set(textToCount))
    _lenthOfText  = len(textToCount)
    
    print("this is len of the set() ", _lenthOftheSet);
    print("this is len() ", _lenthOfText );    
    print("the value" , lexical_diversity(textToCount));


def frequencyDistributions(someText):
    _freqDist = FreqDist(someText)
    
    print (_freqDist);
    print ('\n')
    print ("Most Common" , _freqDist.most_common());

"""
    print (_freqDist);
    print (_freqDist);
---------------------- MAIN()
"""

def main():
    _myText = ["to", "be", "or", "not", "to", "be", "that", "is", "the", "question"]
    _myText2 = ["Call", "me", "Ishmael", "."]
    frequencyDistributions(_myText)
    
    
if __name__ == "__main__": 
    # calling main function 
    main()













    
