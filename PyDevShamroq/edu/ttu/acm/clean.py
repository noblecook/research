import time
import datetime
import uuid
import re


def rinseCycle(inputDataSet):
    cfr = inputDataSet['CFRTITLE']
    sectionNo = inputDataSet['SECTNO']
    title =  cfr + sectionNo
    
    #note this can be a properties file or read from a database
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
    cleanResults = rinseCycle(regulatoryDataSet);
    return cleanResults

