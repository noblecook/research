regulatoryText = []


def getText(node):
    innerText = ''
    if node != None:
        try:
            if (node.tag == 'P'):
                innerText = ''.join(node.itertext())
                regulatoryText.append(innerText)
                print('Text ---> : '+  innerText)  
            else:
                innerText = node.text
                print('Meta Data: ' + innerText)                 
        except Exception as e:
            print(str(e) + '\n')           
    else:
        innerText = 'NONE' 
    return innerText



def getXMLData(node):
    if node != None:
        try:
            print('node.tag: ', node.tag)
            print('node.attrib: ', node.attrib)       
            getText(node)
        except Exception as e:
            print(str(e))
        for item in node:
            getXMLData(item)
    else:
        return 0
    
    return regulatoryText
    
    
    


