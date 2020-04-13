"""

When the texts of a corpus are divided into several categories,
by genre, topic, author, etc, we can maintain separate frequency
distributions for each category. This will allow us to study
systematic differences between the categories.

This is relevant for checking modal verbs in different Legal Context.
For Example, Department of Energy vs. Health and Human Services vs. 

"""
import nltk
from nltk.corpus import brown

def condFreqDist():
    cfd = nltk.ConditionalFreqDist((genre, word)
        for genre in brown.categories()
            for word in brown.words(categories=genre))

    cfd.plot()
    

"""
---------------------- MAIN()-------------------
"""

def main():
    _myText = ["to", "be", "or", "not", "to", "be", "that", "is", "the", "question"]
    _myText2 = ["Call", "me", "Ishmael", "."]
    print(_myText);
    condFreqDist()
    
    
if __name__ == "__main__": 
    # calling main function 
    main()













    
