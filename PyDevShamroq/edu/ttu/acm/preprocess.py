regulatoryText = []
import uuid
dict = {}

def getText(node):
    innerText = ''
    
    if node != None:
        try:
            if (node.tag == 'P'):
                innerText = ''.join(node.itertext())
                regulatoryText.append(innerText)
                dict[uuid.uuid4()] = innerText
                
#                 print('node.tag: ', node.tag)
#                 print('node.attrib: ', node.attrib) 
#                 print('Text ---> : '+  innerText) 
#                 print('<><> ------ DICTIONRY----text     <><>' , dict);
#                 print('\n')
                
            else:
                innerText = node.text
                regulatoryText.append(innerText)
                dict[node.tag] = innerText
            
#                 print('node.tag: ', node.tag)
#                 print('node.attrib: ', node.attrib) 
#                 print('Meta Data <><><><><>: ' + innerText) 
#                 print('<><> DICTIONRY <><>' , dict);                
        except Exception as e:
            print(str(e) + '\n')           
    else:
        innerText = 'NONE' 
    return innerText

def getXMLData(node, reg):
    dict["Regulation"] = reg
    if node != None:
        try:
            getText(node)
        except Exception as e:
            print(str(e))
        for item in node:
            getXMLData(item, reg)
    else:
        return 0
    
    #print('<><> DICTIONRY <><>' , dict); 
    #return regulatoryText
    return dict
    
    
    


