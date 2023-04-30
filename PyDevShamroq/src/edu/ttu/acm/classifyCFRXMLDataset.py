import time
import pandas as pd
import spacy

from datetime import datetime
import re
import xml.etree.ElementTree as eTree

from spacy.pipeline import EntityRuler
CFR_16_HOME_BASE = "C:/Users/patri/OneDrive/Documents/20 PhD/seke-conference/"
CFR_SEKE_FOLDER = "IJSEKE - Submission Guidelines/2023-IJSEKE-manuscript/govinfo.gov.16CFR.Volumes/"
CSV_FILE = "eCFR_48_ALL-eCFR_48_ALL2023-04-27_00-16-30.csv"
csv_file_path = CFR_16_HOME_BASE + CFR_SEKE_FOLDER + CSV_FILE


# I've used this concept more than once, time to break out
# Then use a json or xml file to create the column names dynamically
# also can set options dynamically through the file as well.
def initializeDataFrame():
    # Define the column names
    column_names = ["section_no", "subject", "text", "modal_verb", "deontic_operator", "antecedent", "consequent"]
    # Load the list of lines into a DataFrame
    iDF = pd.DataFrame(columns=column_names)
    # Change the display options to show more text
    pd.set_option('max_colwidth', 80)
    return iDF


def getTimeNow():
    t = time.localtime()
    current_time = time.strftime("%c", t)
    print("Current Time =", current_time)
    return t


def extractMetaModel(paragraph):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(paragraph)

    # Initialize an empty list to store information dictionaries
    information_list = []

    # Extract information for each sentence in the document
    for sent in doc.sents:
        # Initialize empty sets for each information type
        subjects = set()
        objects = set()
        targets = set()
        purposes = set()
        instruments = set()
        places = set()

        # Extract information from the sentence
        for token in sent:
            # Subjects (who)
            if "subj" in token.dep_:
                subjects.add(token.text)

            # Objects (what)
            if "obj" in token.dep_:
                objects.add(token.text)

            # Targets (whom)
            if "dobj" in token.dep_:
                targets.add(token.text)

            # Purposes (why)
            if "advcl" in token.dep_:
                purposes.add(token.head.text)

            # Instruments (how)
            if "prep" in token.dep_ and token.text == "with":
                instruments.add(token.head.text)

            # Places (where)
            if token.ent_type_ == "GPE":
                places.add(token.text)

        # Store the extracted information in a dictionary
        info_dict = {
            "subjects": subjects,
            "objects": objects,
            "targets": targets,
            "purposes": purposes,
            "instruments": instruments,
            "places": places,
        }

        # Add the dictionary to the information list
        information_list.append(info_dict)

        # Print the information list
        for index, info in enumerate(information_list):
            print(f"Sentence {index + 1}:")
            for key, value in info.items():
                print(f"  {key.capitalize()}: {value}")
            print()
    time.sleep(1)


def extract_modality(sentence):
    modality = None
    deontic_operator = None

    for token in sentence:
        if token.dep_ in {"aux", "auxpass"}:
            if token.text.lower() in {"can", "could", "may", "might", "must", "shall", "should", "will", "would"}:
                modality = token.text.lower()
                # pattern for rights
                if modality in {"should", "may", "can", "could", "permits", "does not restrict", "does not require"}:
                    deontic_operator = "has a right to", "has the right to"
                if modality in {"must", "is required to", "shall", "may not", "is prohibited to", "is subject to"}:
                    deontic_operator = "obligation"
                if modality in {"ma", "may elect not to ", "is not required to", "requirements does not apply", "is permitted to", "at the election of", "is not subject to"}:
                    deontic_operator = "privilege"
                if modality in {"does not have a right to"}:
                    deontic_operator = "no right"
                if modality in {"authorize termination of", "must obtain an authorization", "may revoke", "may terminate"}:
                    deontic_operator = "power"
                '''
                if modality in {"must", "shall", "should"}:
                    deontic_operator = modality
                '''
                break

    return modality, deontic_operator


def extract_modality_and_deontic_operators(sentence):
    modality = None
    deontic_operator = None

    for token in sentence:
        token_text_lower = token.text.lower()
        if token.dep_ in {"aux", "auxpass"} or token_text_lower in {"is", "does"}:
            if token_text_lower in {"can", "could", "may", "might", "must", "shall", "should", "will", "would", "is",
                                    "does"}:
                modality = token_text_lower

                # Rights
                if any(phrase in sentence.text.lower() for phrase in
                       {"permits", "does not restrict", "does not require"}):
                    deontic_operator = "has a right to"
                elif modality in {"should", "may", "can", "could"}:
                    deontic_operator = "has a right to"

                # Obligation
                if any(phrase in sentence.text.lower() for phrase in
                       {"is required to", "may not", "is prohibited to", "is subject to"}):
                    deontic_operator = "obligation"
                elif modality in {"must", "shall"}:
                    deontic_operator = "obligation"

                # Privilege
                if any(phrase in sentence.text.lower() for phrase in
                       {"may elect not to", "is not required to", "requirements do not apply", "is permitted to",
                        "at the election of", "is not subject to"}):
                    deontic_operator = "privilege"
                elif modality in {"may"}:
                    deontic_operator = "privilege"

                # No right
                if "does not have a right to" in sentence.text.lower():
                    deontic_operator = "no right"

                # Power
                if any(phrase in sentence.text.lower() for phrase in
                       {"authorize termination of", "must obtain an authorization", "may revoke", "may terminate"}):
                    deontic_operator = "power"

                break

    return modality, deontic_operator
'''
    "subjects": subjects,
    "objects": objects,
    "targets": targets,
    "purposes": purposes,
    "instruments": instruments,
    "places": places,
'''


def extract_modality_with_meta_model2(sentence):
    subject = None
    modality = None
    action_verb = None
    deontic_operator = None

    for token in sentence:
        token_text_lower = token.text.lower()

        if token.dep_ == "nsubj":
            subject = token.text

        if token.dep_ in {"aux", "auxpass"} or token_text_lower in {"is", "does"}:
            if token_text_lower in {"can", "could", "may", "might", "must", "shall", "should", "will", "would", "is", "does"}:
                modality = token.text.lower()

        if token.pos_ == "VERB" and token.dep_ != "aux":
            action_verb = token.text.lower()

        # Deontic operators
        if modality:
            # Rights
            if any(phrase in sentence.text.lower() for phrase in {"permits", "does not restrict", "does not require"}):
                deontic_operator = "has a right to"
            elif modality in {"should", "may", "can", "could"}:
                deontic_operator = "has a right to"

            # Obligation
            if any(phrase in sentence.text.lower() for phrase in {"is required to", "may not", "is prohibited to", "is subject to"}):
                deontic_operator = "obligation"
            elif modality in {"must", "shall"}:
                deontic_operator = "obligation"

            # Privilege
            if any(phrase in sentence.text.lower() for phrase in {"may elect not to", "is not required to", "requirements do not apply", "is permitted to", "at the election of", "is not subject to"}):
                deontic_operator = "privilege"
            elif modality in {"may"}:
                deontic_operator = "privilege"

            # No right
            if "does not have a right to" in sentence.text.lower():
                deontic_operator = "no right"

            # Power
            if any(phrase in sentence.text.lower() for phrase in {"authorize termination of", "must obtain an authorization", "may revoke", "may terminate"}):
                deontic_operator = "power"

    return subject, modality, action_verb, deontic_operator


def is_legal_norm(modality):
    prescriptive_modals = {"can", "could", "may", "might", "must", "shall", "should", "will", "would", "is required to",
                           "may not", "is prohibited to", "is subject to"}
    return modality in prescriptive_modals


def extract_modality_with_meta_model(sentence):
    sent = sentence
    subject = None
    modality = None
    action_verb = None
    obj = None
    target = None
    instrument = None
    purpose = None

    for token in sentence:
        if token.dep_ == "nsubj":
            subject = token
        elif token.dep_ in {"aux", "auxpass"}:
            modality = token.text.lower()
        elif token.pos_ == "VERB" and token.dep_ != "aux":
            action_verb = token
        elif token.dep_ == "dobj":
            obj = token
        elif token.dep_ == "attr":
            target = token
        elif token.dep_ == "prep":
            if token.text.lower() in {"by", "with", "using"}:
                # instrument = token.children.__next__()
                instrument = token.children

            elif token.text.lower() in {"for", "to", "in order to"}:
                # purpose = token.children.__next__()
                purpose = token.children

    if is_legal_norm(modality):
        return sent, subject, modality, action_verb, obj, target, instrument, purpose

    return None


def main():
    getTimeNow()
    nlp = spacy.load("en_core_web_lg")

    # read the csv file into a "dataframe"
    df_of_regulations = pd.read_csv(csv_file_path)

    results = []

    # Iterate through each row of the DataFrame
    for index, row in df_of_regulations.iterrows():
        # print(f"Processing row {index}:")
        for col_name in df_of_regulations.columns:
            print(f"\t{col_name}: {row[col_name]}")

            # ------------------------------------------- #
            # Here we need to process the information
            # Then reload into a data structure - df or json
            # or stored as a csv with results
            # ------------------------------------------- #

            if col_name == "TEXT":

                # ------------------------------------------ #
                # Here we need to get the right sentence
                # otherwise the subjects are arbitrary
                # -------------------------------------------#

                # (1) extractMetaModel(row[col_name])
                # Extract information for each sentence in the document
                paragraph = row[col_name]
                doc = nlp(paragraph)
                for sent in doc.sents:
                    #subject, modality, action_verb, deontic_operator = extract_modality_with_meta_model(sent)
                    components = extract_modality_with_meta_model(sent)
                    if components:
                        # print(f"\tSentence: {sent.text}")
                        results.append(components)
                        # print("------------------------------------------")
                    '''
                    print(f"\tSentence: {sent.text}")
                    print(f"  \t\tSubject: {subject}")
                    print(f"  \t\tModal Verb: {modality}")
                    print(f"  \t\tAction Verb: {action_verb}")
                    print(f"  \t\tDeontic Operator: {deontic_operator}")
                    print()
                    '''

        print("------------------------------------------")
        for elements in results:
            sent, subject, modality, action_verb, obj, target, instrument, purpose = elements
            print(f"Original sentence: {sent}")
            print(f"Subject: {subject}")
            print(f"Modality: {modality}")
            print(f"Action verb: {action_verb}")
            print(f"Object: {obj}")
            print(f"Target: {target}")
            print(f"Instrument: {instrument}")
            print(f"Purpose: {purpose}")
            print()
            time.sleep(2)


    print(df_of_regulations.shape)
    print(df_of_regulations.info())
    getTimeNow()


if __name__ == '__main__':
    main()


'''
        print("&&&&&&&&&&&&&&&&&&&&&&&")
        print("       DONE            ")
        print("&&&&&&&&&&&&&&&&&&&&&&&")
        print()
        print()

'''