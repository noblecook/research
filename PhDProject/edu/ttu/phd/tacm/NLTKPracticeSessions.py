'''
Created on Dec 16, 2018
@author: patcoo
https://towardsdatascience.com/multi-class-text-classification-with-scikit-learn-12f1e60e0a9f

'''

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import names, movie_reviews, brown
import random
import time

legalParagraph = "A writ of habeas corpus directs a person, usually a prison warden, to produce the prisoner and justify the prisoner's detention. If the prisoner argues successfully that the incarceration is in violation of a constitutional right, the court may order the prisoner's release. Habeas corpus relief also may be used to obtain custody of a child or to gain the release of a detained person who is insane, is a drug addict, or has an infectious disease. Usually, however, it is a response to imprisonment by the criminal justice system."
legalSentences = sent_tokenize(legalParagraph)


def getInputFromFile():
    print("There are ", len(legalSentences), " sentences in this legal text.")
    i = 1
    for sentence in legalSentences:
        '''
         --- This is where each sentence has to be addressed---
        '''
        print ("The sentence is  ---> ", sentence)
        word = word_tokenize(sentence)
        posTag = nltk.pos_tag(word)
        print ("part of Speech Tag --> ", posTag)

def pythonClassifierExample ():
    labeled_names = ([(name, 'male') for name in names.words('male.txt')] +  [(name, 'female') for name in names.words('female.txt')])
    random.shuffle(labeled_names)
    for name in labeled_names:        
        print (name)
        
    print (type(labeled_names))
    print (type(names.words('male.txt')))

def myClassifierExample ():
    labeled_names = ([(name, 'male') for name in names.words('male.txt')] +  [(name, 'female') for name in names.words('female.txt')])
    name = "Patrick"
    age = 49
    gender = "male"
    birthlocation = "Alabama"
    statement1 = 'statement1', 'verb', 'predicate'
    statement2 = 'subject', 'verb', 'statement2'
    statement3 = 'subject', 'verb', 'object'
    statement4 = '', 'verb', 'object'
    statement5 = 'subject', 'verb', 'adv'
    statement6 = 'subject', 'verb', 'object'
    statement7 = 'subject', 'verb', 'object'
    statement8 = 'subject', 'verb', 'object'
    
    #myLabeled_names = [name, age, gender, birthlocation, 'Cook']
    myLabeled_names=[(name, age, gender, birthlocation, 'male'), (age, 'male')]
    exampleList =[(statement1), (statement2)]

    print("Type labeled_names ", type(labeled_names))    
    random.shuffle(labeled_names)
    for element in labeled_names:        
        print (element)
    print("\n")
            
    print("Type myLabeled_names", type(myLabeled_names))    
    random.shuffle(myLabeled_names)
    for element in myLabeled_names:        
        print (element)
    print("\n")
    
    print("Type exampleList ", type(exampleList))    
    random.shuffle(exampleList)
    for element in exampleList:        
        print (element)
        
    print("<><><><><> " , gender)
    
def shamroq_features(phrase): 
    if phrase == "hello world - United States":
        shamroq = {
        "geolocation": "US",
        "region": "North America"
        }
    elif phrase == "hello world - London":
        shamroq = {
        "geolocation": "UK",
        "region": "Great Britain"
        }
    elif phrase == "hello world - Germany":
        shamroq = {
        "geolocation": "GE",
        "region": "Europe"
        }
    elif phrase == "hello world - Paris":
        shamroq = {
        "geolocation": "PA",
        "region": "Europe"
        }
    elif phrase == "hello world - Saudi Arabia":
        shamroq = {
        "geolocation": "SA",
        "region": "Middle East"
        }
    else:
        print("------------>  UNDEFINED")
        shamroq = {
        "geolocation": "ROLL TIDE",
        "key": "value"
        }
    return shamroq

'''
# this is where the magic happens between the two function.
# the objective is to have a preprosseor tokenize the words, 
# then tagged them. once tagged, load in here so they can be 
# returned with multi-classification. 
'''

def new_gender_features (name):
    features = {}
    features["first_letter"] = name[0].lower()
    features["last_letter"] = name[-1].lower()
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        features["count({})".format(letter)] = name.lower().count(letter)
        features["has({})".format(letter)] = (letter in name.lower())
    return features

def gender_features (word):
    return {'last_letter': word[-1]} 

def gender_features2 (word):
    return {'suffix1': word[-1:],
            'suffix2': word[-2:]}
        
def pythonFeatureSets ():
    '''
    /*
        labeled_names is a <class 'list'> that is populated with [name, gender] from the male.txt file.
        Since the male.txt file contains all male names, the second parameter, gender, is a constant string.
        As an example, [Patrick, 'male'], [Wm. Patrick, 'male'].  Once the male.txt file completely loads, 
        then labeled_names <class 'list'> is populated with [name, gender] from the female.txt file. In
        this file, all the names are female names and the second parameter is 'female'
    */
    '''
    labeled_names = ([(name, 'male') for name in names.words('male.txt')] +  [(name, 'female') for name in names.words('female.txt')])

    
    '''
    /*  labeled_names list is randomly shuffled. */
    '''
    random.shuffle(labeled_names)

    '''
    /*
        At this point, featuresets, another type <class 'list'>, is populated with the NEW randome results 
        of labeled_names. In particular, the statement "for (n, gender) in labeled_names" loops through 
        the list from [0..n] and loads the featuresets.  The featureset list will contain the results of 
        gender_features(n) in the first slot, and contain results of gender in the second slot.  As a result
        featuresets = [{'last_letter': word[-1]}, gender].  In short, featuresets is used to build 
        the training set.  There are 7,944 entries in the featuresets list.
        Another example - https://www.cs.bgu.ac.il/~elhadad/nlp17/Classification.html
        Consider the rule of if {key:value} = TRUE, then GENDER) for the training set
    */
    '''
    featuresets = [(gender_features(n), gender) for (n, gender) in labeled_names]
    for stuff in featuresets:
        print ("my stuff", stuff)
        time.sleep(10)

    '''
    /*
        create a training/test set SPLIT. 
    */
    '''
    train_set, test_set = featuresets [500:], featuresets[:500]        
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    result = classifier.classify(gender_features("Jema"))
    print("RESULT --> ", result)
    print(nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(5)
    

def myPythonFeatureSets ():
    '''
    /*
        labeled_names is a <class 'list'> that is populated with [name, gender] from the male.txt file.
        Since the male.txt file contains all male names, the second parameter, gender, is a constant string.
        As an example, [Patrick, 'male'], [Wm. Patrick, 'male'].  Once the male.txt file completely loads, 
        then labeled_names <class 'list'> is populated with [name, gender] from the female.txt file. In
        this file, all the names are female names and the second parameter is 'female'
    */
    '''
    labeled_names = ([(name, 'male') for name in names.words('C:/Users/patcoo/male.txt')] +  [(name, 'female') for name in names.words('female.txt')])
    '''
    /*  labeled_names list is randomly shuffled. */
    '''
    random.shuffle(labeled_names)

    '''
    /*
        At this point, featuresets, another type <class 'list'>, is populated with the NEW randome results 
        of labeled_names. In particular, the statement "for (n, gender) in labeled_names" loops through 
        the list from [0..n] and loads the featuresets. The featureset list will contain the results of 
        gender_features(n) in the first slot, and contain results of gender in the second slot.  As a result
        featuresets = [{'last_letter': word[-1]}, gender].  
        
        In short, featuresets is used to build the training set.  There are 7,944 entries in the featuresets 
        list.  Another example - https://www.cs.bgu.ac.il/~elhadad/nlp17/Classification.html  Consider the 
        rule of if {key:value && key:value} = TRUE, then GENDER) for the training set... so in my case, 
        everything that represents a right or an obligation needs to be together for && condition 
    */
    '''
    featuresets = [(gender_features2(n), gender) for (n, gender) in labeled_names]

    '''
    /*
        create a training/test set SPLIT. 
    */
    '''
    train_set, test_set = featuresets [500:], featuresets[:500]        
    classifier = nltk.NaiveBayesClassifier.train(train_set)
    result = classifier.classify(gender_features("Jema"))
    print("RESULT --> ", result)
    print(nltk.classify.accuracy(classifier, test_set))
    classifier.show_most_informative_features(5)
    
def pythonMovieReviews ():
    documents = [(list(movie_reviews.words(fileid)), category) 
                 for category in movie_reviews.categories()
                 for fileid in movie_reviews.fileids(category)]
    
    random.shuffle(documents)
    print("Start mySet")
    time.sleep(3)
    for words in documents:    
        print ("document type ", type(documents))
        print ("words type ", type(words))
        time.sleep(5)
        print ("<><><><-----> \n", words)
        print ('\n')
        time.sleep(20)
    
    
def pythonPartOfSpeechTagging ():
    suffix_dist = nltk.FreqDist
    posTag = nltk.pos_tag(brown.words())
    print ("part of Speech Tag --> ", posTag)
    time.sleep(555)
  
        
        
def plainOlDictionaries ():
    '''
    /*
      A dictionary is a list of key:value pairs
    */
    '''
    hohfeldian_legal_concepts = {"does not have a right to" : "anti-right", 
            "has a right to" : "right", 
            "is not required to" : "anti-obligation",
            "may" : "right",
            "may deny" : "right",
            "may not" : "obligation",
            "may not require" : "anti-obligation",
            "may require" : "right",
            "must" : "obligation",
            "must deny" : "obligation",
            "must permit" : "obligation",
            "must request" : "obligation",
            "retains the right to" : "anti-obligation"
    }
    training_set = {"does not have a right to" : "anti-right", 
            "has a right to" : "right", 
            "is not required to" : "anti-obligation",
            "may" : "right",
            "may deny" : "right",
            "may not" : "obligation",
            "may not require" : "anti-obligation",
            "may require" : "right",
            "must" : "obligation",
            "must deny" : "obligation",
            "must permit" : "obligation",
            "must request" : "obligation",
            "retains the right to" : "anti-obligation"
    }
    test_set = {"does not have a right to" : "anti-right", 
            "has a right to" : "right", 
            "is not required to" : "anti-obligation",
            "may" : "right",
            "may deny" : "right",
            "may not" : "obligation",
            "may not require" : "anti-obligation",
            "may require" : "right",
            "must" : "obligation",
            "must deny" : "obligation",
            "must permit" : "obligation",
            "must request" : "obligation",
            "retains the right to" : "anti-obligation"
    }
    
    myList = [hohfeldian_legal_concepts, 'hello', 12]
    for stuff in myList:
        print(stuff)
        
    

    
def main(): 
    # load regulations from file 
    #pythonClassifierExample()
    #pythonMovieRevies ()
    myPythonFeatureSets() 

    


      
      
if __name__ == "__main__": 
    # calling main function 
    main() 
