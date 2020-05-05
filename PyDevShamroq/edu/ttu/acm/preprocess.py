import uuid
regulatoryText = []
dict = {}
import time

def getText(node):
    innerText = ''
    
    if node != None:
        try:
            if (node.tag == 'P'):
                innerText = ''.join(node.itertext())
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

def processData(node, reg):
    dict["Regulation"] = reg
    if node != None:
        try:
            getText(node)
        except Exception as e:
            print(str(e))
        for item in node:
            #getXMLData(item, reg)
            processData(item, reg)
    else:
        return 0
    return dict;

def init(node, reg):
    print("... starting preprocess")
    time.sleep(1)
    result = processData(node, reg) 
    contentDict = {"Content": regulatoryText}
    result.update(contentDict)
    return result
    
    
    


