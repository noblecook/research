from owlready2 import *
from owlready2.namespace import onto_path
import uuid 
'''
This example comes from - https://stackoverflow.com/questions/62800690/how-do-i-assimilate-to-an-individual-the-same-data-property-n-times/62800943#62800943
'''
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
    
    
def main():

    '''
    To create a relationship (Subj, Pred, Obj), the Subj and Obj
    must be defined FIRST, then bind them together
    class hasUniqueID (DataProperty): pass

    Looking for (CFR45 --> hasUniqueID --> 1559988)
    '''
    cfr45 = onto.Legal_Source("CFR45_164.510")
    print (cfr45.name)
    print (cfr45.iri)
    for i in onto.Legal_Source.instances(): print (i)
    



    

if __name__ == '__main__':
    main()






    '''

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


