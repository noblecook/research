from owlready2 import *
from owlready2.namespace import onto_path
'''
This example comes from - https://stackoverflow.com/questions/62800690/how-do-i-assimilate-to-an-individual-the-same-data-property-n-times/62800943#62800943
'''


onto = get_ontology("file://C:/projects/phd/sekeConf/src/shamroq.owl").load()

list_flavors = [
    {'name': 'name1'},
    {'name': 'name2'},
    {'name': 'name3'},
]
        
with onto:
    # A simple model:
    class Regulation(Thing): pass
    class hasFlavor(DataProperty): pass
    class hasUniqueID (DataProperty):
        domain = [Regulation]
        range = [str]
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
    
    #can you have multiple of these?
    class hasSubSection (ObjectProperty):
        domain = [Regulation]
        range = [onto.Basic_ACTIVITY_with_Modality]
    

    # you have to define the `hasName` property
    # when creating the individual:
    #cone = onto.IceCream('Chocolate', hasFlavor=[])
    
    # you can now append to this list:
    #for line in list_flavors:
        #cone.hasFlavor.append(line['name']) # resuts in name4
    
    
def main():
    print ("Hello World")
    print (onto.search(hasUniqueID = "*"))
    time.sleep(1)
    '''
    myList = list(onto.classes())
    for var in myList:
        print (var)
    print (hasSubSection.domain)
    print (hasSubSection.range)
    '''

    '''
    To create a relationship (Subj, Pred, Obj), the Subj and Obj
    must be defined FIRST, then bind them together
    class hasUniqueID (DataProperty): pass

    Looking for (CFR45 --> hasUniqueID --> 1559988)
    '''
    cfr45 = Regulation("_CFR_45_164_510")
    uniqueID = '1559988'
    cfr45.hasUniqueID = [uniqueID]
    print (cfr45.hasUniqueID)
    print (onto.graph.dump)


    '''
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
    

if __name__ == '__main__':
    main()












'''
Legal Source (e.g.  45§ 164.510)
    1. has Unique ID -----> Literal
    2. has Category -----> Literal
    3. has Title Section -----> Literal
    4. has Priority -----> Literal
    5. has Degree Of Necessity -----> Literal
    6. has CFR Title -----> Literal
    7. has CFR Title Text -----> Literal
    8. has Volume -----> Literal
    9. has Date -----> Literal
    10. has Original Date -----> Literal
    11. has Cover Only -----> Literal
    12. has Title -----> Literal
    13. has Granulenum-----> Literal
    14. has Heading -----> Literal
    15. has Parent -----> Literal
    16. has Section Number ---->
    17. has Sub Section ----> Object

    
class LegalSource:
    pass
class x:
    def a():
        print ("Hello World")

with x:
    a
'''
