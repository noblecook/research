'''
Created on Dec 17, 2018
@author: patcoo
'''
import nltk
import random
import time
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import names, movie_reviews, brown
'''
def movieReviews():
    documents = [(list(movie_reviews.words(fileid)), category)
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    random.shuffle(documents)
    return documents

def hohfeldian(legalStatement):
    myDataset = [
        ('has a right to', 'right'),
        ('may', 'right'),
        ('may deny', 'right'),
        ('may require', 'right'),
        ('does not have a right to', 'anti-right'),
        ('must', 'obligation'),
        ('must deny', 'obligation'),
        ('must permit.', 'obligation'),
        ('must request', 'obligation'),
        ('retains the right to', 'obligation'),
        ('is not required to', 'anti-obligation'),
        ('may not require', 'anti-obligation'),
        ('retains the right to', 'anti-obligation')
    ]

    
    test = [
        ('The beer was good.', 'pos'),
        ('I do not enjoy my job', 'neg'),
        ("I ain't feeling dandy today.", 'neg'),
        ("I feel amazing!", 'pos'),
        ('Gary is a friend of mine.', 'pos'),
        ("I can't believe I'm doing this.", 'neg')
    ]
    classifier = nltk.NaiveBayesClassifier.train(train)
    result = classifier.classify(legalStatement)
    print("RESULT --> ", result)
    time.sleep(55)
    #print(nltk.classify.accuracy(classifier, test_set))
    #classifier.show_most_informative_features(5)

def hohfeld_class(legalStatement):
    featuresets = [
        'has a right to',
        'may',
        'may deny',
        'may require',
        'does not have a right to',
        'must',
        'must deny',
        'must permit.',
        'must request',
        'retains the right to',
        'is not required to',
        'may not require',
        'retains the right to']
    
    labels = [
        'right',
        'right',
        'right',
        'right',
        'anti-right',
        'obligation',
        'obligation',
        'obligation',
        'obligation',
        'obligation',
        'anti-obligation',
        'anti-obligation',
        'anti-obligation']
    
    train_set, test_set = featuresets [5:], featuresets[:5]        
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    result = classifier.classify(legalStatement)
    print("RESULT --> ", result)
    time.sleep(555)
    print(nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(5)
    
'''

def hohfeldian(legalStatement):
    featuresets = [
        ('has a right to', 'right'),
        ('may', 'right'),
        ('may deny', 'right'),
        ('may require', 'right'),
        ('does not have a right to', 'anti-right'),
        ('must', 'obligation'),
        ('must deny', 'obligation'),
        ('must permit.', 'obligation'),
        ('must request', 'obligation'),
        ('retains the right to', 'obligation'),
        ('is not required to', 'anti-obligation'),
        ('may not require', 'anti-obligation'),
        ('retains the right to', 'anti-obligation')
    ]
    
    features = ({"female" , 1}, "male" , 2)
    
    classifier = nltk.NaiveBayesClassifier.train(features)
    result = classifier.classify(legalStatement)
    print("RESULT --> ", result)
    time.sleep(555)
    print(nltk.classify.accuracy(classifier, features))
    classifier.show_most_informative_features(5)

            
def main():
    legalStatement = 'A covered entity that agrees to a restriction may not use or disclose protected health information, except if the individual who requested the restriction is in need of emergency treatment'
    #hohfeldian(legalStatement)
    hohfeldian(legalStatement)
      
      
if __name__ == "__main__": 
    # calling main function 
    main()
