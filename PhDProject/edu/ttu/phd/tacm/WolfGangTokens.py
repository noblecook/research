'''
Created on Apr 18, 2019

@author: patcoo
'''
import json
import hashlib
from OpenSSL import crypto

'''
NOTE: JSON data (i.e. JSON text file or a string) is converted to a dictionary in Python.
The idea here is to understand how to manipulate a dictionary so that CRUD operations
are performed on the object. 
'''
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



def printJSON(jsonString):
    if jsonString != None:
        try:
            token = json.loads(jsonString);
            print(token)
            print('\n')
            print(type(token))
        except:
            print('--------------------->>>> could not print text')
    else:
        return 0
    
    
def getJSONElement(elment):
    if elment != None:
        try:
            token = json.loads(elment);
            print("hello world")
            print(token)
            print('\n')
            print(type(token))
        except:
            print('--------------------->>>> could not print text')
    else:
        return 0
    

def encryptToken(self):
    if self != None:
        try:
            # Basic setup stuff to generate a certificate
            self.pkey = PKey()
            self.pkey.generate_key(TYPE_RSA, 384)
            self.req = X509Req()
            self.req.set_pubkey(self.pkey)
            # Authority good you have.
            self.req.get_subject().commonName = "Yoda root CA"
            self.x509 = X509()
            self.subject = self.x509.get_subject()
            self.subject.commonName = self.req.get_subject().commonName
            self.x509.set_issuer(self.subject)
            self.x509.set_pubkey(self.pkey)
            now = datetime.now().strftime("%Y%m%d%H%M%SZ")
            expire  = (datetime.now() + timedelta(days=100)).strftime("%Y%m%d%H%M%SZ")
            self.x509.set_notBefore(now)
            self.x509.set_notAfter(expire) 
        except:
            print('--------------------->>>> could not print text')
    else:
        return 0
    
    
    
def main(): 

    #printJSON(wolfgangJSON)
    getJSONElement(wolfgangJSON)


    
if __name__ == "__main__": 
    # calling main function 
    main() 