import time
import datetime
import uuid
import re


def printResults(dictionaryResult):
    print("\n")
    print("Printing Semi-Structured Data of the CFR - as a python dictionary")
    time.sleep(0);
    for key, value in dictionaryResult.items():
        print("Key:", key)       
        for nestedCategory in value:
            print ('   ' + nestedCategory + ' : ', value[nestedCategory])

def rinseCycle(inputDataSet):
    cfr = inputDataSet['CFRTITLE']
    sectionNo = inputDataSet['SECTNO']
    title =  cfr + sectionNo
    
    #note this can be a properties file
    jsonResult = {
        "Metadata": {
            "uniqueID" :  uuid.uuid4(),
            "category":  "some category",
            "title":  title,
            "priority":  100,
            "degreeOfNecessisty": "Explain"
            },
        "Header": {
            "cfrtitle" :  inputDataSet['CFRTITLE'],
            "cfrtitletext":  inputDataSet['CFRTITLETEXT'],
            "vol":  inputDataSet['VOL'],
            "date":  inputDataSet['DATE'],
            "originalDate":  inputDataSet['ORIGINALDATE'],
            "coverOnly":  inputDataSet['COVERONLY'],
            "title":  inputDataSet['TITLE'],
            "granulenum":  inputDataSet['GRANULENUM'],
            "heading":  inputDataSet['HEADING'],
            "parent":  inputDataSet['PARENT'],         
            },
        "Body": {
            "sectno":  inputDataSet['SECTNO'],
            "subject":  inputDataSet['SUBJECT'], 
            "content" :  inputDataSet['Content'],
            "cita" :  inputDataSet['CITA']
            }
        }
 
    return jsonResult


''''
The input 
The clean result returns a semi structured set of the regulations stored
in a nested dictionary with three components: Metadata, Header, and Body.
The dictionary data structured is returned back to the caller.
''' 

def sanitize(regulatoryDataSet):
    print("... starting Analyze.clean()")
    time.sleep(0)
    cleanResults = rinseCycle(regulatoryDataSet);
    printResults(cleanResults)
    #time.sleep(5)
    return cleanResults

