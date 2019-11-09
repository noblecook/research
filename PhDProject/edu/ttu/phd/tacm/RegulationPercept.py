'''
Created on Dec 8, 2018
@author: Patrick Cook
Model Agent 
As an Element, root has a tag and a dictionary of attributes:
'''
import urllib.request 
import xml.etree.ElementTree as etree 
import time
import unicodedata


FILEPREFIX = 'C:/Users/patcoo/git/research/PhDProject/data/'
xml_21_CFR_Section_11_10 = FILEPREFIX+'xml_21_CFR_Section_11_10.xml'
xml_45_CFR_Section_11_10 = FILEPREFIX+'xml_45_CFR_Section_164_510.xml'

XML_FILE_REGULATION_21_CFR_Sections_11_10  = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/xml_21_CFR_Section_11_10.xml'
XML_FILE_REGULATION_21_CFR_Sections_11_30  = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/xml_21_CFR_Section_11_30.xml'
XML_FILE_REGULATION_21_CFR_Sections_11_200 = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/xml_21_CFR_Section_11_200.xml'
XML_FILE_REGULATION_21_CFR_Sections_11_300 = 'C:/Users/patcoo/eclipse-workspace/PhDProject/data/xml_21_CFR_Section_11_300.xml'


xml_21_CFR_Section_11_10 = FILEPREFIX+'xml_21_CFR_Section_11_10.xml'
xml_45_CFR_Section_11_10 = FILEPREFIX+'xml_45_CFR_Section_164_510.xml'

def getInputFromFile(inputFile):
    tree = etree.parse(inputFile)
    root = tree.getroot()
    print("root -->", root)
    for element in root:
        print(" child-tag -->", element.tag)
        print(" child-attrib -->", element.attrib)
        print(" child-content -->", element.text)
        for sublement in element:
            print("  element-tag -->", sublement.tag)
            print("  element-attrib -->", sublement.attrib)
            print("  element-content -->", sublement.text)
            for leaf in sublement:
                print("   leaf-tag -->", leaf.tag)
                print("   leaf-attrib -->", leaf.attrib)
                print("   leaf-content -->", leaf.text)
                        

def getChildNodes(element):
    
    if not element:
        getChildNodes(element) 
    else:
        print("   getChildNodes: leaf-tag -->", element.tag)
        print("   getChildNodes: leaf-attrib -->", element.attrib)
        print("   getChildNodes: leaf-content -->", element.text) 
        
           
def main(): 
    # load regulations from file

    getInputFromFile(xml_45_CFR_Section_11_10)
     
    '''
    getInputFromFile(XML_FILE_REGULATION_21_CFR_Sections_11_10)
    print('\n')
    getInputFromFile(XML_FILE_REGULATION_21_CFR_Sections_11_30)
    print('\n')
    getInputFromFile(XML_FILE_REGULATION_21_CFR_Sections_11_200)
    print('\n')
    getInputFromFile(XML_FILE_REGULATION_21_CFR_Sections_11_300) 
    '''
      
      
if __name__ == "__main__": 
    # calling main function 
    main() 


