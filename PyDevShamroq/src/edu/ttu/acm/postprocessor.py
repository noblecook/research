from owlready2 import *
from owlready2.namespace import onto_path
'''
This example comes from - https://stackoverflow.com/questions/62800690/how-do-i-assimilate-to-an-individual-the-same-data-property-n-times/62800943#62800943

An ontology has the following attributes:

.base_iri : base IRI for the ontology
.imported_ontologies : the list of imported ontologies (see below)
and the following methods:

.classes() : returns a generator for the Classes defined in the ontology (see Classes and Individuals (Instances))
.individuals() : returns a generator for the individuals (or instances) defined in the ontology (see Classes and Individuals (Instances))
.object_properties() : returns a generator for ObjectProperties defined in the ontology (see Properties)
.data_properties() : returns a generator for DataProperties defined in the ontology (see Properties)
.annotation_properties() : returns a generator for AnnotationProperties defined in the ontology (see Annotations)
.properties() : returns a generator for all Properties (object-, data- and annotation-) defined in the ontology
.disjoint_classes() : returns a generator for AllDisjoint constructs for Classes defined in the ontology (see Disjointness, open and local closed world reasoning)
.disjoint_properties() : returns a generator for AllDisjoint constructs for Properties defined in the ontology (see Disjointness, open and local closed world reasoning)
.disjoints() : returns a generator for AllDisjoint constructs (for Classes and Properties) defined in the ontology
.different_individuals() : returns a generator for AllDifferent constructs for individuals defined in the ontology (see Disjointness, open and local closed world reasoning)
.get_namepace(base_iri) : returns a namespace for the ontology and the given base IRI (see namespaces below, in the next section)

    class Regulation(Thing): pass
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
'''

file1 = "file://C:/projects/phd/sekeConf/src/archive/seke-shamroq.owl"
file2 = "C:/projects/phd/sekeConf/src/archive/seke-shamroq-out.owl"
onto = get_ontology(file1).load()

        
with onto:
    # A simple model:

    class HelloWorldClass(Thing):
        pass
    
    class SoftwareEngineer(Thing):
        pass
    
    class hasFirstName(DataProperty):
        domain = [SoftwareEngineer]
        range = [str]
    
    class hasLastName(DataProperty):
        domain = [SoftwareEngineer]
        range = [str]


    # you have to define the `hasName` property
    # when creating the individual:
    #cone = onto.IceCream('Chocolate', hasFlavor=[])
    
    # you can now append to this list:
    #for line in list_flavors:
        #cone.hasFlavor.append(line['name']) # resuts in name4
    
    
def main():
    print ("Hello World")

    '''
    myList = list(onto.classes())
    for var in myList:
        print (var)
    print (hasSubSection.domain)
    print (hasSubSection.range)
    '''

    '''
    To create a relationship (Sub, predicate, obj), the Subj and Obj
    must be defined FIRST, then bind them together
    class hasUniqueID (DataProperty): pass

    Looking for (CFR45 --> hasUniqueID --> 1559988)
    
    HELLO_WORLD = Regulation("HELLO_WORLD")
    HELLO_WORLD.hasUniqueID = ["Hello Patrick Cook"]
    print (onto.HELLO_WORLD.hasUniqueID)
    
        
    onto.save(file2, format = "rdfxml")
    onto.graph.dump()
    time.sleep(2)
    '''


    print ("----------------------")
    print ("Classes")
    print ("----------------------")
    #time.sleep(1)
    myClasses = list(onto.classes())
    for cls in myClasses:
        print (cls)
        time.sleep(1)


    print ("----------------------")
    print ("Object Properties")
    print ("----------------------")
    myObjProperties = list(onto.object_properties())
    for objProps in myObjProperties:
        print (objProps)
        time.sleep(1)
        
    print ("----------------------")
    print ("Data Properties")
    print ("----------------------")
    myDataProperties = list(onto.data_properties())
    for dataProps in myDataProperties:
        print (dataProps)
        time.sleep(1)
        
        
    print ("----------------------")
    print ("Individuals")
    print ("----------------------")
    myIndividuals = list(onto.individuals())
    for indiv in myIndividuals:
        print (indiv)
        time.sleep(3)

    '''
    onto.save(file2, format = "ntriples")
    time.sleep(5)
    all_triples = onto.get_triples(None, None, None)
    print(list(all_triples))
    
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
    print ("All Properties")
    print ("----------------------")
    time.sleep(1)      
    allProperties = list(onto.properties())
    for prop in allProperties:
        print (prop)

    print ("----------------------")
    print ("Intances")
    print ("----------------------")
    time.sleep(3)      
    myInstances = list(onto.individuals())
    for instan in myInstances:
        print (instan)

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
