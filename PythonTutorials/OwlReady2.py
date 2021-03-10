from owlready2 import *
from owlready2.namespace import onto_path
'''
Be sure to read the ontology from a file
with shamroq_upper_onto:
    class A (Thing): pass
    class A (Thing): pass
    class A (Thing): pass
    class A (Thing): pass

    class has_property (ObejctProperty)
        domain = [Incoming]
        range = [Outgoing]
'''


shamroqOntology = "C:\projects\phd\sekeConf\src\shamroq.owl"
testOntology = "C:\projects\phd\sekeConf\src\test.owl"
onto = get_ontology(testOntology)

def driver(inputType):
    shamroq_upper_onto = get_ontology(shamroqOntology);
    shamroq_upper_onto.load()
    shamroq_upper_onto_classes = list(shamroq_upper_onto.classes())
    print ("Classes ")
    print(shamroq_upper_onto_classes)



with onto:
  class Food(Thing): pass
  class Taste(Thing): pass
 
  class has_taste(ObjectProperty):
        domain = [Food]
        range = [Taste]

apple = Food('apple')
orange = Food('orange')

apple.has_taste.append(Taste('sweet'))
apple.has_taste.append(Taste('juicy'))
orange.has_taste.append(Taste('sweet'))
orange.has_taste.append(Taste('juicy'))
print(list(onto.classes()))


    
    
    

   

def main():
    driver(shamroqOntology) 

if __name__ == '__main__':
    main()



