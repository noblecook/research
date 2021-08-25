'''
Created on Apr 12, 2020

@author: patri
'''

from nltk.corpus import stopwords
from nltk.collocations import TrigramCollocationFinder
from nltk.metrics import TrigramAssocMeasures

def getTriGramsLessStopWords(regulatoryText):
    '''
     ======== NOT WORKING -------
    '''
    _ignoreWords = set(stopwords.words('english'));
    _filterStopWords = [lambda w: len(w) < 3 or w in _ignoreWords]
    _findTriGrams = TrigramCollocationFinder.from_words(regulatoryText)
    _findTriGrams.apply_word_filter(_filterStopWords)
    
    _triGramTexts = _findTriGrams.nbest(TrigramAssocMeasures.likelihood_ratio, 30)
    
    print('\n')
    print("Here we go triGrams collocation ----> ", _triGramTexts)
    print('\n')
    print('\n')
    print('\n')
    return _triGramTexts

def getTriGrams(regulatoryText):
    _findTriGrams = TrigramCollocationFinder.from_words(regulatoryText)
    _triGramTexts = _findTriGrams.nbest(TrigramAssocMeasures.likelihood_ratio, 30)
    print('\n')
    print("Here we go triGrams collocation ----> ", _triGramTexts)
    print('\n')
    print('\n')
    print('\n')
    return _triGramTexts


'''
def frequencyDistributions(someText):
    V = set(someText);
    _freqDist = FreqDist(someText)
    _longWords = [w for w in V if len(w) > 3]
    _longFreqWords = [w for w in V if len(w) > 3 and _freqDist[w] > 1]
    print ('\n')
    print (_freqDist);
    print ("Most Common <<------------->>" , _freqDist.most_common());
    print ('\n')
    print ("Long Words <<------------->>" , sorted(_longWords)); 
    print ('\n')
    print ("Long FREQUENT Words <<------------->>" , sorted(_longFreqWords)); 
    print ('\n')
    #_freqDist.plot()
    pauseForTheCause(100)
'''  
    


'''
    --- Step 2 ---
     
    --- Traverse each level in the tree to look for the 
    --- tag, attributes, and text
    --- once the text is found, then call the pre-processor
'''



'''
    --- Step 1 ---
     
    --- Read the regulation from a List
    --- loop through the list and get the first file
    --- in the first file, parse the tree, and find the root
'''