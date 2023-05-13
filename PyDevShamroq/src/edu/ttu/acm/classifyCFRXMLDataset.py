import time
import pandas as pd
import spacy
from spacy.matcher import PhraseMatcher
from datetime import datetime


CFR_16_HOME_BASE = "C:/Users/patri/OneDrive/Documents/20 PhD/seke-conference/"
CFR_SEKE_FOLDER = "IJSEKE - Submission Guidelines/2023-IJSEKE-manuscript/govinfo.gov.16CFR.Volumes/"
CSV_FILE = "eCFR_48_ALL-eCFR_48_ALL2023-04-27_00-16-30.csv"
result_csv_folder = CFR_16_HOME_BASE + CFR_SEKE_FOLDER

CFR_48_HOME_BASE = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/far/"
TITLE_48_CSV_FILE_BEFORE = "eCFR_48_ALL_2023-05-06_21-39-14_BACKUP.csv"
TITLE_48_CSV_FILE_TEMP = "eCFR_48_ALL_2023-05-06_21-39-14.csv"
TITLE_48_CSV_FILE = "eCFR_48_ALL_2023.csv"
TITLE_48_CSV_FILE_VOL_01 = "eCFR_48_VOL_01_2023-05-13_12-17-55.csv"
csv_file_path1 = CFR_48_HOME_BASE + TITLE_48_CSV_FILE_BEFORE
csv_file_path2 = CFR_48_HOME_BASE + TITLE_48_CSV_FILE_TEMP
csv_file_path3 = CFR_48_HOME_BASE + TITLE_48_CSV_FILE
csv_file_path4 = CFR_48_HOME_BASE + TITLE_48_CSV_FILE_VOL_01

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



def extract_modality(sentence):
    modality = None
    deontic_operator = None

    for token in sentence:
        if token.dep_ in {"aux", "auxpass"}:
            if token.text.lower() in {"can", "could", "may", "might", "must", "shall", "should", "will", "would"}:
                modality = token.text.lower()
                # -------------------
                # pattern for rights #
                # -------------------
                if modality in {"can", "may", "could", "might"}:
                    deontic_operator = "right"
                # -------------------
                # pattern for obligations
                # -------------------
                if modality in {"should", "must", "shall"}:
                    deontic_operator = "obligation"
                # -------------------
                # pattern for privilege
                # -------------------
                if modality in {"can not", "may not", "could not", "might not"}:
                    deontic_operator = "privilege"
                # -------------------
                # pattern for no-rights
                # -------------------
                if modality in {"should not", "must not", "shall not"}:
                    deontic_operator = "no right"

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


def get_deontic_operator(modality):
    deontic_operation = None

    # print("inside get_deontic_operator. modality = ", modality)


    # Deontic operations
    if modality:
        # Permissions
        if any(phrase in modality for phrase in {"permits", "does not restrict", "does not require"}):
            deontic_operation = "permission"
        elif modality in {"can", "may", "could", "might"}:
            deontic_operation = "permission"

        # Obligations
        if any(phrase in modality for phrase in {"is required to", "may not", "is prohibited to", "is subject to"}):
            deontic_operation = "obligation"
        elif modality in {"should", "must", "shall"}:
            deontic_operation = "obligation"

        # Privileges
        if any(phrase in modality for phrase in {"may elect not to", "is not required to", "requirements do not apply", "is permitted to", "at the election of", "is not subject to"}):
            deontic_operation = "privilege"
        elif modality in {"cannot", "may not", "could not", "might not"}:
            deontic_operation = "dispensation"

        # No right
        if any(phrase in modality for phrase in {"should not", "must not", "shall not"}):
            deontic_operation = "prohibition"

        # Powers
        if any(phrase in modality for phrase in {"authorize termination of", "must obtain an authorization", "may revoke", "may terminate"}):
            deontic_operation = "power"

    # print("result = ", deontic_operation)

    return deontic_operation


def extract_modality_with_meta_model(sentence):
    sent = sentence
    subject = None
    modality = None
    action_verb = None
    obj = None
    target = None
    instrument = None
    purpose = None
    deontic_operator = None

    for token in sentence:
        print("-----------------> ", token)


        if token.dep_ == "nsubj":
            subject = token
        elif token.dep_ in {"aux", "auxpass"}:
            modality = token.text.lower()
            print("FOUND IT! ", modality)

            if modality:
                deontic_operator = get_deontic_operator(modality)
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
        return sent, subject, modality, action_verb, obj, target, instrument, purpose, deontic_operator

    return None


def getMetaModel(deontic_operator, sentence):
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
            if deontic_operator is None:
                if modality:
                    # print("inside getMetaModel for loop:  modality = ", modality)
                    deontic_operator = get_deontic_operator(modality)
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

    return sent, subject, modality, action_verb, obj, target, instrument, purpose, deontic_operator


def extract_phrase_modality_with_meta_model(nlp, sentence):
    sent = sentence
    subject = None
    modality = None
    action_verb = None
    obj = None
    target = None
    instrument = None
    purpose = None
    deontic_operator = None

    matcher = PhraseMatcher(nlp.vocab)
    phrases = [
        "is required to",
        "may not",
        "could not",
        "might not",
        "cannot",
        "should not",
        "must not",
        "shall not",
        "is prohibited to",
        "is subject to",
        "may elect not to",
        "is not required to",
        "requirements do not apply",
        "is permitted to",
        "at the election of",
        "is not subject to",
        "authorize termination of",
        "must obtain an authorization",
        "may revoke",
        "may terminate",
    ]

    patterns = [nlp.make_doc(phrase) for phrase in phrases]
    matcher.add("MODALITY_PHRASES", patterns)

    matches = matcher(sentence)
    matched_phrases = [sentence[start:end].text.lower() for match_id, start, end in matches]
    if matched_phrases:
        matched_phrase = matched_phrases[0]
        # print("---------->  ", matched_phrase)
        modality = matched_phrase
        deontic_operator = get_deontic_operator(modality)
        phrase_result = getMetaModel(deontic_operator, sentence)
    else:
        phrase_result = getMetaModel(deontic_operator, sentence)

    return phrase_result


def extract_phrase_modality_with_meta_model3(nlp, sentence):
    sent = sentence
    subject = None
    modality = None
    action_verb = None
    obj = None
    target = None
    instrument = None
    purpose = None
    deontic_operator = None

    matcher = PhraseMatcher(nlp.vocab)
    phrases = [
        "is required to",
        "may not",
        "could not",
        "might not",
        "cannot",
        "should not",
        "must not",
        "shall not",
        "is prohibited to",
        "is subject to",
        "may elect not to",
        "is not required to",
        "requirements do not apply",
        "is permitted to",
        "at the election of",
        "is not subject to",
        "authorize termination of",
        "must obtain an authorization",
        "may revoke",
        "may terminate",
    ]

    patterns = [nlp.make_doc(phrase) for phrase in phrases]
    matcher.add("MODALITY_PHRASES", patterns)

    matches = matcher(sentence)
    for match_id, start, end in matches:
        matched_phrase = sentence[start:end].text.lower()
        print("---------->  ", matched_phrase)

        if get_deontic_operator(matched_phrase) is not None:
            modality = matched_phrase

            deontic_operator = get_deontic_operator(modality)
            # print("deontic operator ---------->  ", deontic_operator)
            # print("sentence ---------->  ", sentence)
            phrase_result = getMetaModel(deontic_operator, sentence)
            break

    if not modality:
        my_result = getMetaModel(deontic_operator, sentence)
        # print(my_result)
        return my_result

    return phrase_result


def extract_phrase_modality_with_meta_model2(nlp, sentence):
    sent = sentence
    subject = None
    modality = None
    action_verb = None
    obj = None
    target = None
    instrument = None
    purpose = None
    deontic_operator = None

    matcher = PhraseMatcher(nlp.vocab)
    phrases = [
        "is required to",
        "may",
        "could",
        "might",
        "should",
        "must",
        "shall",
        "may not",
        "could not",
        "might not",
        "should not",
        "must not",
        "cannot",
        "shall not",
        "is prohibited to",
        "is subject to",
        "may elect not to",
        "is not required to",
        "requirements do not apply",
        "is permitted to",
        "at the election of",
        "is not subject to",
        "authorize termination of",
        "must obtain an authorization",
        "may revoke",
        "may terminate",
    ]

    patterns = [nlp.make_doc(phrase) for phrase in phrases]
    matcher.add("MODALITY_PHRASES", patterns)

    matches = matcher(sentence)
    for match_id, start, end in matches:
        matched_phrase = sentence[start:end].text.lower()
        print("---------->  ", matched_phrase)

        if get_deontic_operator(matched_phrase) is not None:
            modality = matched_phrase
            deontic_operator = get_deontic_operator(modality)
            print("deontic operator ---------->  ", deontic_operator)
            # print("sentence ---------->  ", sentence)
            break

    if not modality:
        for token in sentence:
            print("NOT Modality ------!!!", token)


            if token.dep_ == "nsubj":
                subject = token
            elif token.dep_ in {"aux", "auxpass"}:
                modality = token.text.lower()
                print("FOUND IT! ", modality)

                if modality:
                    deontic_operator = get_deontic_operator(modality)
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
        return sent, subject, modality, action_verb, obj, target, instrument, purpose, deontic_operator

    return None


def main():
    getTimeNow()
    nlp = spacy.load("en_core_web_lg")
    # nlp.tokenizer.rules["cannot"] = cannot_exception

    # read the csv file into a "dataframe"
    df_of_regulations = pd.read_csv(csv_file_path4)

    list_of_results = []
    result_df = pd.DataFrame(columns=["Original_sentence", "Subject", "Modality", "Action_verb", "Object",
                                      "Target", "Instrument", "Purpose", "Hohfeldian_Incident"])

    # Iterate through each row of the DataFrame
    for index, row in df_of_regulations.iterrows():
        # print(f"Processing row {index}:")
        for col_name in df_of_regulations.columns:
            if col_name == "TEXT":
                paragraph = row[col_name]
                if isinstance(paragraph, str):
                    doc = nlp(paragraph)
                    # print(f"\t{col_name}: {row[col_name]}")
                    for sent in doc.sents:
                        # print("::---> ", sent)
                        # components = extract_modality_with_meta_model(nlp, sent)
                        components = extract_phrase_modality_with_meta_model(nlp, sent)

                        # print(components[0])
                        # print(components[8])
                        # print("")

                        if components:
                            new_row = {
                                "Original_sentence": sent,
                                "Subject": components[1],
                                "Modality": components[2],
                                "Action_verb": components[3],
                                "Object": components[4],
                                "Target": components[5],
                                "Instrument": components[6],
                                "Purpose": components[7],
                                "Hohfeldian_Incident": components[8]
                            }
                            new_row_df = pd.DataFrame([new_row], columns=result_df.columns)
                            result_df = pd.concat([result_df, new_row_df], ignore_index=True)
                            list_of_results.append(result_df)

                else:
                    pass
                    # print(f"\t{col_name}: Invalid value (not a string)")
            else:
                pass
                # print(f"\t{col_name}: {row[col_name]}")
    SHAMROQ_PREFIX = "SHAMROQ"
    eCFR_48 = "_eCFR_48_RESULTS_"
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    fileExt = ".csv"
    result_csv_file = CFR_48_HOME_BASE + SHAMROQ_PREFIX + eCFR_48 + now + fileExt
    result_df.to_csv(result_csv_file, index=False)
    print(result_csv_file)


    '''
    for row in list_of_results:
        print(row)
        
        # print(list_of_results)
    '''
    getTimeNow()


if __name__ == '__main__':
    main()
