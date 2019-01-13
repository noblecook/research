'''
Created on Dec 18, 2018
@author: patcoo
'''
from sklearn.naive_bayes import MultinomialNB
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer, CountVectorizer
from sklearn.feature_selection import chi2
from sklearn.model_selection import train_test_split
from sklearn import decomposition, ensemble, tree
import numpy as np
import pandas as pd
import pandas, numpy, string
import time

'''
Oposing Legal Concepts
Right --> No Right
Duty  --> Privilege
Power --> Disability
Liabiliity --> Immunity

'''





def initialize (statement):
    data = {'modality': 
            ['has a right to',
             'has the right to',
             'may',
             'may deny',
             'may require',
             'does not have a right to',
             'must',
             'must deny',
             'must permit',
             'must request',
             'retains the right to',
             'is not required to',
             'may not require',
             'retains the right to'
            ],'hohfeldian':
            ['right',
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
             'anti-obligation'
            ] }
                     
    df = pd.DataFrame(data)   
    df = df[pd.notnull(df['modality'])]
    
        
    '''
    /*
        Is this truly required.  After commenting this out... the same results were delivered.
        So it seems as if not needed.  But more to follow here. 
        df.columns = ['modality', 'hohfeldian']
    */
    '''
    
    '''
    /*
    
    */
    '''
         
    df['category_id'] = df['hohfeldian'].factorize()[0]
    category_id_df = df[['hohfeldian', 'category_id']].drop_duplicates().sort_values('category_id')
    category_to_id = dict(category_id_df.values)
    id_to_category = dict(category_id_df[['category_id', 'hohfeldian']].values)
    
    
    '''
    /*
        Here is the focal point for today.... the correlation should be 14 to 3, however, based
        on the article, the resutl is 14 to 1.. obviously this is not correct, but let's explore
        <><><><> THIS IS NOT CORRECT .... Please REVISE <><><><>
    */
    '''
    #tfidf = TfidfVectorizer(sublinear_tf=True, min_df=3, norm='l2', encoding='latin-1', ngram_range=(1, 2), stop_words='english')
    tfidf = TfidfVectorizer()
    features = tfidf.fit_transform(df.modality).toarray()
    #print("_____<><> tfidf.get_feature_names() ")
    #print(tfidf.get_feature_names())
    #time.sleep(1000)
    
    
    labels = df.category_id 
    N = 2
    for hohfeldian, category_id in sorted(category_to_id.items()):
        features_chi2 = chi2(features, labels == category_id)
        indices = np.argsort(features_chi2[0])
        feature_names = np.array(tfidf.get_feature_names())[indices]
        unigrams = [v for v in feature_names if len(v.split(' ')) == 1]
        bigrams = [v for v in feature_names if len(v.split(' ')) == 2]
        print("# '{}':".format(hohfeldian))
        print("  . Most correlated unigrams:\n. {}".format('\n. '.join(unigrams[-N:])))
        print("  . Most correlated bigrams:\n. {}".format('\n. '.join(bigrams[-N:])))
        #time.sleep (7)  
        
#    time.sleep (1000)       
    X_train, X_test, y_train, y_test = train_test_split(df['modality'], df['hohfeldian'], random_state = 0)
    count_vect = CountVectorizer()
    X_train_counts = count_vect.fit_transform(X_train)
    tfidf_transformer = TfidfTransformer()
    X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)
    clf = MultinomialNB().fit(X_train_tfidf, y_train)        
    print(clf.predict(count_vect.transform([statement])))
    

    
def main(): 
    legalStatement1 = "A covered entity that agrees to a restriction may not use or disclose protected health information, except if the individual who requested the restriction is in need of emergency treatment"
    legalStatement2 = "TA CE may disclose PHI to a person."
    legalStatement3 = "The CE must provide notice to the individual (a)."
    # load regulations from file 
    initialize(legalStatement3) 

      
if __name__ == "__main__": 
    # calling main function 
    main() 