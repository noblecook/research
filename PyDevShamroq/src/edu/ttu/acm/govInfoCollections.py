import os
import time
from datetime import datetime
import requests

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
    govinfo_api_endpoint = f"https://api.govinfo.gov/packages/{govinfo_api_package_id}/granules/" \
                           f"{govinfo_api_granule_id}/summary?api_key=" \
                           f"{govinfo_api_key}"

    response = requests.get(govinfo_api_endpoint)
    if response.status_code == 200:
        data = response.json()
    else:
        print('Message in account ', govinfo_api_account)
        print('Error:', response.status_code)
    return data


# Retrieve new or updated packages for a collection given a start date and time
# returns a dictionary
def getCollectionsLastModifiedStartDate(givenDate):
    collectionData = None
    govinfo_api_key = os.environ["GOVINFO_API_KEY"]
    lastModifiedStartDate = givenDate
    collectionType = "CFR"
    govinfo_api_endpoint = f"https://api.govinfo.gov/collections/{collectionType}/{lastModifiedStartDate}"
    attributes = {
        "pageSize": 1000,
        "offsetMark": "*",
        "api_key": govinfo_api_key
    }
    response = requests.get(govinfo_api_endpoint, params=attributes)
    # print("Request URL:", response.url)
    # time.sleep(100)
    if response.status_code == 200:
        collectionData = response.json()
        # print(collectionData)
    else:
        print(f"Error: {response.status_code} - {response.reason}")
    return collectionData


# input is a dictionary of collections
# filters the dictionary for (e.g. Seven (7) "Commercial Practices")
# returns a list dataType with dictionaries of CFR Text Titles
def getFilterCollectionsData(collections_dict, cfr_text_title):
    cleanCollectionsData = []
    # Iterate through the dictionary and look for the value 4
    for key, value in collections_dict.items():
        if key == "packages":
            for collections in value:
                # print(collections)
                for colKey, colValue in collections.items():
                    # print(f'{colKey}: {colValue}')
                    if colKey == 'title' and colValue == cfr_text_title:
                        colMetaData = {
                            'packageId': collections["packageId"],
                            'lastModified': collections["lastModified"],
                            'packageLink': collections["packageLink"],
                            'docClass': collections["docClass"],
                            'title': collections["title"],
                            'congress': collections["congress"],
                            'dateIssued': collections["dateIssued"]
                        }
                        cleanCollectionsData.append(colMetaData)
    return cleanCollectionsData


# take a subset of the collections
# parses and find the most recent packageID
# returns packageID
def getPackageID(sublist_collections_cfr_text_title):
    packageID = None
    # print(sublist_collections_cfr_text_title)
    # time.sleep(10)
    cfr_text_title = "CFR-2022-title16-vol1"
    for packages in sublist_collections_cfr_text_title:
        for colKey, colValue in packages.items():
            if colKey == 'packageId' and colValue == cfr_text_title:
                packageID = colValue
                break
    return packageID


def getPackageIDGranules(package_ID):
    package_ID_granules = None
    govinfo_api_key = os.environ["GOVINFO_API_KEY"]
    packageType = "packages"
    granulesType = "granules"
    govinfo_api_endpoint = f"https://api.govinfo.gov/{packageType}/{package_ID}/{granulesType}"
    attributes = {
        "pageSize": 1000,
        "offsetMark": "*",
        "api_key": govinfo_api_key
    }
    response = requests.get(govinfo_api_endpoint, params=attributes)
    # print("Request URL:", response.url)
    # time.sleep(100)
    if response.status_code == 200:
        package_ID_granules = response.json()
        # print(package_ID_granules)
    else:
        print(f"Error: {response.status_code} - {response.reason}")

    return package_ID_granules


def filterPackageIDGranules(results_package_ID_granules, cfr_text_title):
    packageGranules = []
    # Iterate through the dictionary and look for the value 4
    for key, value in results_package_ID_granules.items():
        if key == "granules":
            for packages in value:
                # print(packages)
                # time.sleep(3)
                for colKey, colValue in packages.items():
                    # print(f'{colKey}: {colValue}')
                    if colKey == 'title' and colValue == cfr_text_title:
                        # print("-----------------------> FOUND IT! ")
                        colMetaData = {
                            'title': packages["title"],
                            'granuleId': packages["granuleId"],
                            'granuleLink': packages["granuleLink"],
                            'granuleClass': packages["granuleClass"]
                        }
                        packageGranules.append(colMetaData)
    return packageGranules


def getPackageIDGranulesIDSummary(package_ID, granule_ID):
    # Set the API endpoint and parameters
    gpoResults = None
    govinfo_api_key = os.environ["GOVINFO_API_KEY"]
    packages = "packages"
    granules = "granules"
    summary = "summary"
    govinfo_api_endpoint = f"https://api.govinfo.gov/{packages}/{package_ID}/{granules}/{granule_ID}/{summary}"
    attributes = {
        "api_key": govinfo_api_key
    }
    response = requests.get(govinfo_api_endpoint, params=attributes)
    # Check the status code of the response
    if response.status_code == 200:
        # Parse the response as JSON
        gpoResults = response.json()
    else:
        print(f"Error: {response.status_code} - {response.reason}")
    return gpoResults


def convertDateStringToZulu(cfrXmlTimeString):
    # Convert the input date string to a datetime object
    date_obj = datetime.strptime(cfrXmlTimeString, '%Y-%m-%d')
    # Format the datetime object in the desired output format
    output_str = date_obj.strftime('%Y-%m-%dT%H:%M:%SZ')
    # Print the output string
    return output_str


def getCurrentCFRDateFromGPO(pName, pDate):
    # make an api call to govinfo.gov/api - get provision number and date
    # compare the two, if same, return True, else False
    # first get the collections - https://api.govinfo.gov/collections/CFR?offset=0&pageSize=100&api_key=XscpbIdvZDJpCuXJ985qn3TN8ELoav5gdTSw3ryH
    # getCollectionsInfo()
    queryGovInfoApi()

    pass


def main():
    print("Number of regulations -->", len(regList))
    print("/------------------------------------------/")
    print("... starting main()")
    print("/------------------------------------------/")
    print("\n")
    cfrXMLTextTitle = "Commercial Practices"
    cfrXMLTitle = "Parental consent."
    cfrXMLDate = "2020-01-01"
    zuluDate = convertDateStringToZulu(cfrXMLDate)
    queryDate = zuluDate

    # input is a list datatype which contains 1 or more xml file locations
    # of the regulation
    for regulation in regList:
        # shamroq(regList)
        # getCFRMetaData(regulation)
        # filterCollections =
        collections = getCollectionsLastModifiedStartDate(queryDate)
        filterCollections = getFilterCollectionsData(collections, cfrXMLTextTitle)
        packageID = getPackageID(filterCollections)
        granules = getPackageIDGranules(packageID)
        granuleID = filterPackageIDGranules(granules, cfrXMLTitle)
        gid = granuleID[0]['granuleId']
        gpoResult = getPackageIDGranulesIDSummary(packageID, gid)

        for colKey, colValue in gpoResult.items():
            print(f'{colKey}: {colValue}')
            time.sleep(2)


    print("\n")
    print("/------------------------------------------/")
    print("... completing main()")
    print("/------------------------------------------/")


if __name__ == '__main__':
    main()

