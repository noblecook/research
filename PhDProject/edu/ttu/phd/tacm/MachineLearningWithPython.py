'''
Created on Dec 9, 2018

@author: patcoo
'''

import nltk
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
from nltk.corpus import names
from sklearn import tree
from sklearn.datasets import load_iris
import numpy as np


'''
This is just creating a data set to a list.  
Equivalent to this reserach loading in word phases
and saying Right or Obligation.
'''
def exampleDataSet():
    style.use('ggplot')
    start = datetime.datetime(2010, 1, 1)
    end   = datetime.datetime(2018, 1, 1)
    df = web.DataReader("XOM", "yahoo", start, end)
    print(df.head())
    df['Adj Close'].plot()
    plt.show();

def examplePandaDataFrame():
    web_stats = {'Day':[1,2,3,4,5],
                 'Visits':[5,16,22,12,44],
                 'Bounce':[9,3,5,4,1]}
    df = pd.DataFrame(web_stats)
    print('print df only\n', df);
    print('\n\n')
    print('print df.set_index("Day") to be first column\n\n', df.set_index('Day'));
    #print(df);

def exampleNumpyArrayList():
    web_stats = {'Day':[1,2,3,4,5],
                 'Visits':[5,16,22,12,44],
                 'Bounce':[9,3,5,4,1]}
    df = pd.DataFrame(web_stats)
    print(df)
    print(np.array(df[['Visits','Bounce']]))
   
    
def trainDecisionTreeClassifier():
    
    statement1 = ['subject', 'verb', 'predicate']
    statement2 = ['subject', 'verb', '']
    statement3 = ['subject', 'verb', 'object']
    statement4 = ['', 'verb', 'object']
    statement5 = ['subject', 'verb', 'adv']
    statement6 = ['subject', 'verb', 'object']
    statement7 = ['subject', 'verb', 'object']
    statement8 = ['subject', 'verb', 'object']
    '''
    The features are an ARRAY of Arrays (2-dimensional array)
    '''
    features = [['hello world', 'hello world', 'hello world', 'hello world', 'hello world', 'hello world', 'hello world', 'hello world']]
    '''
    This linear single array signifies the label of the training set. 
    '''
    labels   = ['Right', 'Obligation', 'Privilege', 'No Right', 'Liability', 'Power', 'Disability', 'Immunity']
    
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(features,labels) 
    
    print(clf.predict([['hello world', 'hello world', 'hello world']]));
            
def main(): 
    trainDecisionTreeClassifier()
      
      
if __name__ == "__main__": 
    # calling main function 
    main() 



