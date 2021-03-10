import time
import spacy
nlp = spacy.load("en_core_web_sm")
text =  '''A covered entity may use or disclose protected health information, provided that the individual is informed in advance of the use or disclosure and has the opportunity to agree to or prohibit or restrict the use or disclosure, in accordance with the applicable requirements of this section.', "The covered entity may orally inform the individual of and obtain the individual's oral agreement or objection to a use or disclosure permitted by this section.", '(a) Standard: Use and disclosure for facility directories—(1) Permitted uses and disclosure.', 'Except when an objection is expressed in accordance with paragraphs (a)(2) or (3) of this section, a covered health care provider may:', '(i) Use the following protected health information to maintain a directory of individuals in its facility:', "(A) The individual's name;", "(B) The individual's location in the covered health care provider's facility;", "(C) The individual's condition described in general terms that does not communicate specific medical information about the individual; and", "(D) The individual's religious affiliation; and", '(ii) Use or disclose for directory purposes such information:', '(A) To members of the clergy; or', '(B) Except for religious affiliation, to other persons who ask for the individual by name.', '(2) Opportunity to object.', 'A covered health care provider must inform an individual of the protected health information that it may include in a directory and the persons to whom it may disclose such information (including disclosures to clergy of information regarding religious affiliation) and provide the individual with the opportunity to restrict or prohibit some or all of the uses or disclosures permitted by paragraph (a)(1) of this section.', '(3) Emergency circumstances.', "(i) If the opportunity to object to uses or disclosures required by paragraph (a)(2) of this section cannot practicably be provided because of the individual's incapacity or an emergency treatment circumstance, a covered health care provider may use or disclose some or all of the protected health information permitted by paragraph (a)(1) of this section for the facility's directory, if such disclosure is:", '(A) Consistent with a prior expressed preference of the individual, if any, that is known to the covered health care provider; and', "(B) In the individual's best interest as determined by the covered health care provider, in the exercise of professional judgment.", '(ii) The covered health care provider must inform the individual and provide an opportunity to object to uses or disclosures for directory purposes as required by paragraph (a)(2) of this section when it becomes practicable to do so.', "(b) Standard: Uses and disclosures for involvement in the individual's care and notification purposes—(1) Permitted uses and disclosures.", "(i) A covered entity may, in accordance with paragraphs (b)(2), (b)(3), or (b)(5) of this section, disclose to a family member, other relative, or a close personal friend of the individual, or any other person identified by the individual, the protected health information directly relevant to such person's involvement with the individual's health care or payment related to the individual's health care.", "(ii) A covered entity may use or disclose protected health information to notify, or assist in the notification of (including identifying or locating), a family member, a personal representative of the individual, or another person responsible for the care of the individual of the individual's location, general condition, or death.", 'Any such use or disclosure of protected health information for such notification purposes must be in accordance with paragraphs (b)(2), (b)(3), (b)(4), or (b)(5) of this section, as applicable.', '(2) Uses and disclosures with the individual present.', 'If the individual is present for, or otherwise available prior to, a use or disclosure permitted by paragraph (b)(1) of this section and has the capacity to make health care decisions, the covered entity may use or disclose the protected health information if it:', "(i) Obtains the individual's agreement;", '(ii) Provides the individual with the opportunity to object to the disclosure, and the individual does not express an objection; or', '(iii) Reasonably infers from the circumstances, based on the exercise of professional judgment, that the individual does not object to the disclosure.', '(3) Limited uses and disclosures when the individual is not present.', "If the individual is not present, or the opportunity to agree or object to the use or disclosure cannot practicably be provided because of the individual's incapacity or an emergency circumstance, the covered entity may, in the exercise of professional judgment, determine whether the disclosure is in the best interests of the individual and, if so, disclose only the protected health information that is directly relevant to the person's involvement with the individual's care or payment related to the individual's health care or needed for notification purposes.", "A covered entity may use professional judgment and its experience with common practice to make reasonable inferences of the individual's best interest in allowing a person to act on behalf of the individual to pick up filled prescriptions, medical supplies, X-rays, or other similar forms of protected health information.", '(4) Uses and disclosures for disaster relief purposes.', 'A covered entity may use or disclose protected health information to a public or private entity authorized by law or by its charter to assist in disaster relief efforts, for the purpose of coordinating with such entities the uses or disclosures permitted by paragraph (b)(1)(ii) of this section.', 'The requirements in paragraphs (b)(2), (b)(3), or (b)(5) of this section apply to such uses and disclosures to the extent that the covered entity, in the exercise of professional judgment, determines that the requirements do not interfere with the ability to respond to the emergency circumstances.', '(5) Uses and disclosures when the individual is deceased.', "If the individual is deceased, a covered entity may disclose to a family member, or other persons identified in paragraph (b)(1) of this section who were involved in the individual's care or payment for health care prior to the individual's death, protected health information of the individual that is relevant to such person's involvement, unless doing so is inconsistent with any prior expressed preference of the individual that is known to the covered entity."], 'cita': '[65 FR 82802, Dec. 28, 2000, as amended at 67 FR 53270, Aug. 14, 2002; 78 FR 5699, Jan. 25, 2013'''



def test02():
    bucket = [(col01, col02) for col01 in range(100) for col02 in range (100)]
    for i in bucket:
        print("Bucket", type(bucket), size(bucket));
        print("Hello World")

def test01():
    doc = nlp(text)
    for chunk in doc.noun_chunks:
        print(chunk)
        time.sleep(3);
    
def main():
    bucket = [(col01, col02) for col01 in range(10) for col02 in range (10)]
    for i in bucket:
        print("Bucket", i);
    


    

if __name__ == '__main__':
    main()














    '''

from owlready2 import *
from owlready2.namespace import onto_path
import uuid

This example comes from - https://stackoverflow.com/questions/62800690/how-do-i-assimilate-to-an-individual-the-same-data-property-n-times/62800943#62800943
onto = get_ontology("file://C:/projects/phd/sekeConf/src/shamroq.owl").load()
     
with onto:
    # A simple model:
    class hasFlavor(DataProperty): pass
    class hasUniqueID (DataProperty):pass
    class hasCategory (DataProperty): pass
    class hasTitleSection (DataProperty): pass
    class hasPriority  (DataProperty): pass
    class hasDegreeOfNecessity (DataProperty): pass
    class hasCFRTitle (DataProperty): pass
    class hasCFRTitleText (DataProperty): pass
    class hasVolume  (DataProperty): pass
    class hasDate  (DataProperty): pass
    class hasOriginalDate (DataProperty): pass
    class hasCoverOnly (DataProperty): pass
    class hasTitle  (DataProperty): pass
    class hasGranulenum (DataProperty): pass
    class hasHeading  (DataProperty): pass
    class hasParent  (DataProperty): pass
    class hasSectionNumber (DataProperty): pass
    

    
    To create a relationship (Subj, Pred, Obj), the Subj and Obj
    must be defined FIRST, then bind them together
    class hasUniqueID (DataProperty): pass

    Looking for (CFR45 --> hasUniqueID --> 1559988)
    
    cfr45 = onto.Legal_Source("CFR45_164.510")
    print (cfr45.name)
    print (cfr45.iri)
    for i in onto.Legal_Source.instances(): print (i)
    cfr45.hasUniqueID = [uuid.uuid1() ]
    print (cfr45.hasUniqueID)
    print (onto.graph.dump)


    
    print ("----------------------")
    print ("Triple Store")
    print ("----------------------")
    myTriples = list(onto.get_triples())
    for trips in myTriples:
        print (trips)

        
    print ("----------------------")
    print ("All Properties")
    print ("----------------------")
    time.sleep(1)      
    allProperties = list(onto.properties())
    for prop in allProperties:
        print (prop)


    

    
    print ("----------------------")
    print ("Triple Store")
    print ("----------------------")
    myTriples = list(onto.get_triples())
    for trips in myTriples:
        print (trips)
    
    print ("----------------------")
    print ("Classes")
    print ("----------------------")
    time.sleep(1)
    myClasses = list(onto.classes())
    for cls in myClasses:
        print (cls)

    print ("----------------------")
    print ("Object Properties")
    print ("----------------------")
    time.sleep(1)      
    myObjProperties = list(onto.object_properties())
    for objP in myObjProperties:
        print (objP)

    print ("----------------------")
    print ("Data Properties")
    print ("----------------------")
    time.sleep(1)      
    myDataProperties = list(onto.data_properties())
    for objD in myDataProperties:
        print (objD)



    print ("----------------------")
    print ("Intances")
    print ("----------------------")
    time.sleep(3)      
    myInstances = list(onto.individuals())
    for instan in myInstances:
        print (instan)

    print ("----------------------")
    print ("Default World")
    print ("----------------------")
    myWorld = list(default_world.get_triples())
    myWorld = list(default_world.get_ontology(onto))
    for trips in myWorld:
        onto.unabbreviate('4S')
        subj = trips[0]
        pred = trips[1]
        obj = trips[2]
        print (subj,pred,obj)
        time.sleep(5)

    '''


