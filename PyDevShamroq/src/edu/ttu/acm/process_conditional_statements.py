import pandas as pd
import spacy

def getNormativeStatements(doc):
    antecedent = ""
    consequent = ""
    # Iterate through the tokens in the sentence
    for token in doc:
        # Check if the token is the "if" word
        if token.text.lower() == "if":
            print("<><><><><>   IF .....")
            # Iterate through the next tokens until "then"
            for next_token in token.doc[token.i+1:]:
                '''
                Remove Later
                '''
                # START

                print(next_token.text, " = ", next_token.dep_)
                if next_token.dep_ in ['nsubj', 'nsubjpass', 'dobj', 'pobj']:
                    print("Subtree: ", list(next_token.subtree))

                # STOP
                if next_token.text.lower() == "then":
                    break
                antecedent += next_token.text + " "
        # Check if the token is the "then" word
        elif token.text.lower() == "then":
            # Iterate through the next tokens until end of sentence
            print("<><><><><>   THEN .....")
            for next_token in token.doc[token.i+1:]:
                '''
                                Remove Later
                                '''
                # START

                print(next_token.text, " = ", next_token.dep_)
                if next_token.dep_ in ['nsubj', 'nsubjpass', 'dobj', 'pobj']:
                    print("Subtree: ", list(next_token.subtree))

                # STOP
                consequent += next_token.text + " "

    print("antecedent:", antecedent)
    print("consequent:", consequent)

    conditional_dict = {
        "antecedent": antecedent,
        "consequent": consequent
    }
    return conditional_dict


def init(conditional):
    nlp = spacy.load("en_core_web_lg")
    # Process the sentence with spaCy
    doc = nlp(conditional)
    rule = getNormativeStatements(doc)
    return rule


def main():
    # Read the Excel file and store the data in a dataframe
    # df = pd.read_excel('file.xlsx')

    fileName = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/src/edu/ttu/acm/gold-data-set/dataset-TEMP-cfr_16_312_005.csv"
    df = pd.read_csv(fileName)

    # Retrieve a completion column and store the values in a list
    column_name = 'completion'
    column_values = df[column_name].tolist()
    for line in column_values:
        init(line)


if __name__ == '__main__':
    main()
