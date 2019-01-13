from sklearn import tree


def exampleDataSet ():
    X=[[1.25, 1], [2.25, 1]]
    y=[0,1]
    clf = tree.DecisionTreeClassifier()
    clf = clf.fit(X,y)
    test = clf.predict([[2.25, 1]])
    print(test)
   



x  