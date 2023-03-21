from owlready2 import *
ONTOLOGY_BASE_LOCATION = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/ontologies/"
file = "shamroq.owl"
ONTOLOGY_BASE_URL = "http://shamroq.phd.edu.ttu/shamroq.owl"
ontology_file = ONTOLOGY_BASE_LOCATION + file
onto = get_ontology(ONTOLOGY_BASE_URL)

'''
    If an operator collects personal information from children, 
    then they must obtain verifiable parental consent.
'''
with onto:
    class Operator(Thing):
        pass

    class PersonalInformation(Thing):
        pass

    class Child(Thing):
        pass

    class VerifiableParentalConsent(Thing):
        pass

    class collects(ObjectProperty):
        domain = [Operator]
        range = [PersonalInformation]

    class obtains(ObjectProperty):
        domain = [Operator]
        range = [VerifiableParentalConsent]


    # Save the ontology to a file
    onto.save(file="shamroq.coppa.owl", format="rdfxml")


def main():
    print("done")


if __name__ == '__main__':
    main()

