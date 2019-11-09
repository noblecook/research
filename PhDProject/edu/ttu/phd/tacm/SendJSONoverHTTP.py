'''
Created on Apr 19, 2019

using httpbin for testing here --> https://httpbin.org/

@author: patcoo
'''
import requests
import uuid
from cryptography.fernet import Fernet
from datetime import datetime  
from datetime import timedelta  


wolfgangJSON =    """{
    "WOLFGANG_v1_TOKEN":
        {
            "SECURITY_OBJECT":
                {
                    "CUSTOMER_ID": "RU456TYREE",
                    "AUTHENTICATION_TOKEN": "fjlejf384930",
                    "HASH_VALUE": "fdjad0343jfjo3jj343j4r234j23j;ldjf;dljfa;j",
                    "PUBLIC_KEY": "JFELJVRJKE43L4J32L4J32RQER33JVVKJJRE3",
                    "LIBRARY": null 
                },
            "PRIME_ATTRIBUTES": 
                {
                    "Benefits": "WOLFGANG_v1_ELIGIBLE",
                    "INVITED": true              
                },
            "POLICY_OBJECT":
                   {
                       "Administration_Policy": 
                           {
                            "SUBJECT": "TRIAL_MEMBERS", 
                            "OBJECT": "PII",
                            "MARKETPLANCE": "NA",
                            "ACTION": "REGISTRATION"
                        },                    
                    "Regulatory_Policy":
                        {
                            "PROVISION": "45 CFR 164.510"
                        }
                }
        }
}"""

def getHTTPBinoverPost():

    postRequest = requests.post('https://httpbin.org/post', data=wolfgangJSON)
    print (postRequest.text)
    
def getUUID():
    INVITE_TOKEN = uuid.uuid4();
    print ("<><><><><>------->> ", INVITE_TOKEN)
    
def getHTTPBinoverGet():

    GUID = uuid.uuid4();
    DATE_TIME_GROUP = datetime.now() + timedelta(days=30) ;
    token = {'INVITE_TOKEN': GUID, 'EXPIRY': DATE_TIME_GROUP}
    print(type(token))
    getRequest = requests.get('https://httpbin.org/get', params=token)
    print (getRequest.text)

def generateKey():
    key = Fernet.generate_key()
    file = open('key.key', 'wb')
    file.write(key)
    file.close()

def getKey():
    file = open('key.key', 'rb')
    key = file.read()
    file.close()
    return key
    
    
def encryptToken():
    publicKey = getKey()
    f = Fernet(publicKey)
    message = wolfgangJSON.encode()
    encrypted = f.encrypt(message)
    print(encrypted)
    """
    Now Decrypt the message
    """
    decrypted = f.decrypt(encrypted)
    print(decrypted)
    return encrypted

    
def main(): 

    getHTTPBinoverPost()
    #getHTTPBinoverGet()
    #getUUID()
    #generateKey()
    #encryptToken()
    
if __name__ == "__main__": 
    # calling main function 
    main() 