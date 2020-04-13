'''
Created on Apr 12, 2020

@author: patri
                #listOfTokens = tokenizeTheNode(innerText)
                #tagPartsOfSpeech(listOfTokens)
                #print('node.itertext(): ' + innerText)


def tokenizeTheNode(regulatoryText):
    _tokens = sent_tokenize(regulatoryText)
    print(len(_tokens), ' Tokens (Sentences) : ' ,_tokens)
    return _tokens

def tagPartsOfSpeech(listOfSentences):
    try:
        for legalSentence in listOfSentences:
            words = nltk.word_tokenize(legalSentence)
            #frequencyDistributions(words)
            _posTags = nltk.pos_tag(words)
            print('TAGS------------>  ', _posTags)
    except Exception as e:
        print(str(e))
    return _posTags
'''