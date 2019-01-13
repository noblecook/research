'''
Created on Dec 20, 2018
@author: patcoo

/*
    Main application to read the government regulations from the website.
*/
'''
import urllib.request 
import datetime

website = 'https://www.govinfo.gov/bulkdata/ECFR/title-27/ECFR-title27.xml'


XML_50_CFR_ALL = 'https://www.govinfo.gov/bulkdata/ECFR/title-50/ECFR-title50.xml'
XML_49_CFR_ALL = 'https://www.govinfo.gov/bulkdata/ECFR/title-49/ECFR-title49.xml'
XML_48_CFR_ALL = 'https://www.govinfo.gov/bulkdata/ECFR/title-48/ECFR-title48.xml'
XML_47_CFR_ALL = 'https://www.govinfo.gov/bulkdata/ECFR/title-47/ECFR-title47.xml'
XML_46_CFR_ALL = 'https://www.govinfo.gov/bulkdata/ECFR/title-46/ECFR-title46.xml'
XML_40_CFR_ALL = 'https://www.govinfo.gov/bulkdata/ECFR/title-40/ECFR-title40.xml'
XML_30_CFR_ALL = 'https://www.govinfo.gov/bulkdata/ECFR/title-30/ECFR-title30.xml'
XML_20_CFR_ALL = 'https://www.govinfo.gov/bulkdata/ECFR/title-20/ECFR-title20.xml'
XML_10_CFR_ALL = 'https://www.govinfo.gov/bulkdata/ECFR/title-10/ECFR-title10.xml'
xml_45_CFR_Section_164_522 = 'https://www.govinfo.gov/content/pkg/CFR-2018-title45-vol1/xml/CFR-2018-title45-vol1-sec164-522.xml'
xml_45_CFR_Section_164_510 = 'https://www.govinfo.gov/content/pkg/CFR-2018-title45-vol1/xml/CFR-2018-title45-vol1-sec164-510.xml'


def getRegulations(url, fileName):
    a = datetime.datetime.now()
    request = urllib.request.Request(url)
    response = urllib.request.urlopen(request)
    the_page = response.read()
    theText = the_page.decode()
    b = datetime.datetime.now()
    directory = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/'+fileName+'.xml'
    c = b-a
    print(directory)
    print(c.seconds)
    f = open(directory,'w', encoding='utf8')
    f.write(theText)
    f.close()
    

def main():
    #getRegulations(XML_50_CFR_ALL,'XML_50_CFR_ALL')
    #getRegulations(XML_49_CFR_ALL,'XML_49_CFR_ALL')
    #getRegulations(XML_48_CFR_ALL,'XML_48_CFR_ALL')
    #getRegulations(XML_47_CFR_ALL,'XML_47_CFR_ALL')
    #getRegulations(XML_46_CFR_ALL,'XML_46_CFR_ALL')
    #getRegulations(XML_40_CFR_ALL,'XML_40_CFR_ALL')
    #getRegulations(XML_30_CFR_ALL,'XML_30_CFR_ALL')
    #getRegulations(XML_20_CFR_ALL,'XML_20_CFR_ALL')
    #getRegulations(XML_10_CFR_ALL,'XML_10_CFR_ALL')
    #getRegulations(xml_45_CFR_Section_164_522,'xml_45_CFR_Section_164_522')
    getRegulations(xml_45_CFR_Section_164_510,'xml_45_CFR_Section_164_510')
    
      
     
if __name__ == "__main__": 
    # calling main function 
    main() 
