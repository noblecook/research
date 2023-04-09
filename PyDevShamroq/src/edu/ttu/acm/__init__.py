import pandas as pdd
import analyze
import classify
import model
import relationExtractor
import scan
import preprocessor
import clean
import os
import requests
import xml.etree.ElementTree as eTree
from PyDevShamroq.src.edu.ttu.acm import classifyMetaModel
from PyDevShamroq.src.edu.ttu.acm import parseConditionals
from PyDevShamroq.src.edu.ttu.acm import modellrml
from relationExtractor import *
import time

nlp = spacy.load("en_core_web_sm")
encoding = 'utf-8'

OUTPUT = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/output/"
FILE_PREFIX_COPPA = 'C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/coppa/'
FILE_PREFIX_HIPAA = 'C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/hipaa/'
FILE_PREFIX_GLBA = 'C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/glba/'

csv_data_312_005 = OUTPUT + 'dataset-TEMPx-cfr_16_312_0051.csv'
xml_45_164_306 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-306.xml'
xml_45_164_310 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-310.xml'
xml_45_164_312 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-312.xml'
xml_45_164_510 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-510.xml'
xml_16_312_002 = FILE_PREFIX_COPPA + 'CFR-2020-title16-vol1-sec312-2.xml'
xml_16_312_004 = FILE_PREFIX_COPPA + 'CFR-2020-title16-vol1-sec312-4.xml'
xml_16_312_005 = FILE_PREFIX_COPPA + 'CFR-2020-title16-vol1-sec312-5.xml'
xml_16_312_011 = FILE_PREFIX_COPPA + 'CFR-2020-title16-vol1-sec312-11.xml'
xml_16_312_ALL = FILE_PREFIX_COPPA + 'CFR-2020-title16-vol1-part312.xml'
xml_16_313_009 = FILE_PREFIX_GLBA + 'CFR-2022-title16-vol1-sec313-9.xml'

# regList = [xml_16_312_ALL]
# regList = [xml_45_164_306, xml_45_164_310, xml_45_164_312, xml_45_164_510]
# regList = [xml_16_312_002, xml_16_132_004, xml_16_132_005, xml_16_132_011, xml_45_164_306, xml_45_164_310, xml_45_164_312, xml_45_164_510]
# regList = [xml_16_312_005, xml_16_313_009, xml_45_164_510]
regList = [xml_16_312_005]


def getTimeNow():
    t = time.localtime()
    current_time = time.strftime("%c", t)
    print("Current Time =", current_time)
    return t


def processConditionals(inputDF):
    # iterate through each row of the dataframe
    # print(inputDF.iloc[:10, :3])
    listOfDict = []
    prev_promptID = inputDF.loc[0, 'promptID']
    for index, row in inputDF.iterrows():
        if row['promptID'] == prev_promptID:
            # print('prompt ID = ', row['promptID'])
            # print('\t --> If/then = ', row['completion'])
            conditional = row['completion']
            json_file_with_conditionals = doSomethingLess(conditional)
            listOfDict.append(json_file_with_conditionals)
        else:
            # print('prompt ID = ', row['promptID'])
            # print('\t --> (NEW first row) If/then = ', row['completion'])
            conditional = row['completion']
            json_file_with_conditionals = doSomethingLess(conditional)
            listOfDict.append(json_file_with_conditionals)
        prev_promptID = row['promptID']
    return listOfDict


def doSomethingLess(if_then_stmt):
    return parseConditionals.init(if_then_stmt)


def printDataFrame(df_to_print):
    pdd.set_option('display.max_colwidth', 70)
    pdd.set_option('display.max_columns', None)
    pdd.set_option('display.width', None)
    pdd.set_option('display.colheader_justify', 'center')
    print(df_to_print[["promptID", "completion"]])
    print(df_to_print.iloc[:40, [0, 2]])
    print(df_to_print.iloc[:40, :2])
    print(df_to_print.iloc[:40, :3])


def getStatusUpdateForGPO():
    # call GPO website via Api
    pass
    # get current data stored in metadata file

    # compare the two dates

    # return boolean


def getUpdateProvision(listOfRegulations):
    classificationResults = None
    for regulation in listOfRegulations:
        # scan.init()
        # input  = "regulation", a string of the xml file location;
        # output = "scannedResults" a xml.etree.ElementTree.Element dataType;
        # ------>  10/5/22 add a debug flag to dynamically print portions if true
        # print("scannedResults is of type ", type(scannedResults));
        # time.sleep(100)

        scannedResults = scan.init(regulation)

        # preprocessor.init()
        # input 1 = "scannedResults", an xml.etree.ElementTree.Element dataType
        # input 2 = "regulation", a string of the file location;
        # output = "preProcessedResults" a dictionary of the CFR regulation
        # print("preProcessedResults is of type ", python Dictionary );
        # print("regulation is of type ", String);

        preProcessedResults = preprocessor.init(scannedResults, regulation)

        # clean.init() returns a structured dictionary
        # input = "preProcessedResults", a dictionary of the CFR regulation
        # output = "cleanedResults" a dictionary of the CFR regulation with metadata

        cleanedResults = clean.init(preProcessedResults)

        # classify.init()
        # Todo:  Must classify "Grounding" - Permission, Obligation, Prohibition
        # Todo:  Must classify "The MetaModel" - Subject, Verb, Object, Target
        # Todo:  We want to use SPACY here!!!
        # input => dictionary of x;
        # output => list
        # Option 1) use nltk, work tokenized, POS tagging, and chunking [ CURRENT ]
        # Option 2) use spacy and textacy
        # List the pros and cons of each; then what I used and why
        # ----- THIS IS REALLY ANALYZE ------
        # ----- Build another class to use Spacy and Textacy ------

        classificationResults = classifyMetaModel.init(cleanedResults)

    return classificationResults


# input is a string datatype of the regulation file location
def processRegulations(csv_file_location):

    # ----------- Reads the file for now ------------
    dff = pdd.read_csv(csv_file_location)

    # Initialize Rules
    # input => a dataframe of values that contain if/then statements
    # output -> a list of dictionaries that contain antecedent/consequent
    # corresponding to the input if/then statements to be used in the
    # creation of the Legal Rule ML file
    listOfDictionaries = processConditionals(dff)

    # ----- HERE WE WILL USE OWLReady2 ------
    # ----- Build another class to use Spacy and Textacy ------
    # model.init() input = list of x; output = list
    # model.init(cleanedResults, classificationResults)

    return listOfDictionaries


def getCFRMetaData(reg_xml_file_location):
    # use XSLT to get only two important elements
    # store the results and return
    tree = eTree.parse(reg_xml_file_location)
    root = tree.getroot()

    cfrMetaData = {
        'CFRTITLE': root.find('FDSYS/CFRTITLE').text,
        'CFRTITLETEXT': root.find('FDSYS/CFRTITLETEXT').text,
        'VOL': root.find('FDSYS/VOL').text,
        'DATE': root.find('FDSYS/DATE').text,
        'ORIGINALDATE': root.find('FDSYS/ORIGINALDATE').text,
        'COVERONLY': root.find('FDSYS/COVERONLY').text,
        'TITLE': root.find('FDSYS/TITLE').text,
        'GRANULENUM': root.find('FDSYS/GRANULENUM').text,
        'HEADING': root.find('FDSYS/HEADING').text
    }
    return cfrMetaData


def queryGovInfoApi():
    data = None
    govinfo_api_key = os.environ["GOVINFO_API_KEY"]
    govinfo_api_account = os.environ["GOVINFO_ACCT_ID"]
    govinfo_api_package_id = "CFR-2022-title16-vol1"
    govinfo_api_granule_id = "CFR-2022-title16-vol1-sec312-5"
    govinfo_api_endpoint = f"https://api.govinfo.gov/packages/" \
                           f"{govinfo_api_package_id}/granules/" \
                           f"{govinfo_api_granule_id}/summary?api_key=" \
                           f"{govinfo_api_key}"

    response = requests.get(govinfo_api_endpoint)
    if response.status_code == 200:
        data = response.json()
    else:
        print('Message in account ', govinfo_api_account)
        print('Error:', response.status_code)
    return data


def getCollectionsLastModifiedDate():
    pass


def getPackageIDSummary():
    pass


def getPackageIDGranules():
    pass


def getPackageIDGranulesIDSummary():
    # Set the API endpoint and parameters
    fr_endpoint = "https://api.govinfo.gov/collections/FR"
    cfr_collection = "CFR"
    api_key = os.environ["GOVINFO_API_KEY"]

    # Send the API request to retrieve the most recent Federal Register document containing the COPPA regulations
    params = {
        "offset": 0,
        "pageSize": 1,
        "fields": "lastModified",
        "sort": "lastModifiedDate:desc",
        "q": "Children's Online Privacy Protection Act",
        "api_key": api_key
    }
    response = requests.get(fr_endpoint, params=params)

    # Check the status code of the response
    if response.status_code == 200:
        # Parse the response as JSON
        data = response.json()

        # Extract the last modified start date for the CFR collection
        last_modified_start_date = data["collection"]["lastModified"]
        cfr_endpoint = f"https://api.govinfo.gov/collections/{cfr_collection}/{last_modified_start_date}"
        print("Last Modified Start Date:", last_modified_start_date)
        print("CFR Endpoint:", cfr_endpoint)
    else:
        print(f"Error: {response.status_code} - {response.reason}")


def getCurrentCFRDateFromGPO(pName, pDate):
    # make an api call to govinfo.gov/api - get provision number and date
    # compare the two, if same, return True, else False
    # first get the collections - https://api.govinfo.gov/collections/CFR?offset=0&pageSize=100&api_key=XscpbIdvZDJpCuXJ985qn3TN8ELoav5gdTSw3ryH
    # getCollectionsInfo()
    queryGovInfoApi()

    pass


def is_Provision_Up_to_Date(reg_xml_file_location):
    updateToDate = True

    # get the provision number and date from the passed in file
    getCFRMetaData(reg_xml_file_location)
    # getCurrentCFRDateFromGPO(pName, pDate)
        
    return updateToDate


def shamroq(reg_xml_file_location):
    getTimeNow()
    if is_Provision_Up_to_Date(reg_xml_file_location):
        list_Of_Conditionals = processRegulations(csv_data_312_005)
    else:
        list_Of_Conditionals = getUpdateProvision(reg_xml_file_location)

    modellrml.init(list_Of_Conditionals)
    getTimeNow()
    return list_Of_Conditionals


def main():
    print("Number of regulations -->", len(regList))
    print("/------------------------------------------/")
    print("... starting main()")
    print("/------------------------------------------/")
    print("\n")

    # input is a list datatype which contains 1 or more xml file locations
    # of the regulation
    for regulation in regList:
        shamroq(regulation)
        # getCFRMetaData(regulation)
        # getCollectionsInfo()

    print("\n")
    print("/------------------------------------------/")
    print("... completing main()")
    print("/------------------------------------------/")


if __name__ == '__main__':
    main()
