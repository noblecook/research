import time
import datetime
import uuid
import re


def printResults(dictionaryResult):
    for key, value in dictionaryResult.items():
        print("Key:", key)       
        for nestedCategory in value:
            print ('   ' + nestedCategory + ' : ', value[nestedCategory])
            time.sleep(0)

def cleanData(input):
    cfr = input['CFRTITLE']
    sectionNo = input['SECTNO']
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
            "cfrtitle" :  input['CFRTITLE'],
            "cfrtitletext":  input['CFRTITLETEXT'],
            "vol":  input['VOL'],
            "date":  input['DATE'],
            "originalDate":  input['ORIGINALDATE'],
            "coverOnly":  input['COVERONLY'],
            "title":  input['TITLE'],
            "granulenum":  input['GRANULENUM'],
            "heading":  input['HEADING'],
            "parent":  input['PARENT'],         
            },
        "Body": {
            "sectno":  input['SECTNO'],
            "subject":  input['SUBJECT'], 
            "content" :  input['Content'],
            "cita" :  input['CITA']
            }
        }
 
    return jsonResult

def init(input):
    print("... starting clean")
    time.sleep(1)
    cleanResults = cleanData(input);
    return cleanResults

