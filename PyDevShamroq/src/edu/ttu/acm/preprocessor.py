import uuid
from nltk.tokenize import sent_tokenize
import pandas as pd

regulatoryText = []
dict = {}
import time


def printDictionary(input):
    for k, v, in input.items():
        print(k, " = ", v)
        time.sleep(3)


'''
The getText method is where the heavy lifting of parsing the tree and loading the 
dictionary with specific keys value pairs.  Since the tree contains the Paragraph Tag
once we find it, we get the corresponding text, create a unique key, and store the value
of the regulation.  

Why do I need a key, since I am using a dictionary, there must be unique keys.  I am using 
the uuid to generate unique keys so that I can have access to all the text on each line

NOTE - instead of using the UUID, I must consider using the regulation as the key.
i.e 45CFR SECTION 1ABii (something to this affect)

I don't like the idea of the global dictionary, I must create a method to append and return, or
do it all in the same method
'''


def getText(node):
    innerText = ''
    if node != None:
        try:
            if (node.tag == 'P'):
                innerText = ''.join(node.itertext())
                if (len(sent_tokenize(innerText)) > 1):
                    for stmt in sent_tokenize(innerText):
                        regulatoryText.append(stmt)
                        dict[uuid.uuid4()] = stmt
                else:
                    regulatoryText.append(innerText)
                    dict[uuid.uuid4()] = innerText
            else:
                innerText = node.text
                dict[node.tag] = innerText
        except Exception as e:
            print(str(e) + '\n')
    else:
        innerText = 'NONE'

    return innerText


'''
The processData method takes a node and string.  The node is the tree and the string is the regulatory text.
Nthe getText method is called, provided that the node is not empty, and recursively iterate through each node and leaves.. 

This can probably be made more efficient.  I will revisit once I have a completely working 
code base 
'''


def processData(node, reg):
    dict["Regulation"] = reg
    if node != None:
        try:
            getText(node)
        except Exception as e:
            print(str(e))
        for item in node:
            processData(item, reg)
    else:
        return 0
    return dict;


'''
The init method takes a tree data structure and a string.  The tree contains the 
root and children nodes of the CFR - initially represented as an xml structure.  The 
tree and string are passed to the processData method to populate and return a dictionary
data structure with the Regulation name and the contents 
'''


def init(node, reg):
    print("... Starting preprocessor.init()")
    time.sleep(0)
    result = processData(node, reg)

    # print("printDictionary(result) ........\n\n\n\n")
    contentDict = {"Content": regulatoryText}
    result.update(contentDict)


    '''
    To view the contents of the dictionary, uncomment this code
    Need to convert this dictionary into something else... thinking a data frame.. then return..
    
    df = pd.DataFrame.from_dict(result, orient='index', columns=['col_1'])
    print("\n\n ------->   start data frame ")
    for i, row in df.iterrows():
        print("Key ", i)
        print("Value ", f"{row[0]}")

    print("\n\nstop data frame here --------------- ")

    time.sleep(5)
    '''
    return result



'''
    # is this needed? ----------------
    #contentDict = {"Content": regulatoryText}
    # is this needed? ----------------
    #result.update(contentDict)
    #print("result update")
    #print(result)
    #time.sleep(60)
'''