import logging
import time
import pandas as pd
import spacy
from datetime import datetime

nlp = spacy.load("en_core_web_lg")

CFR_48_HOME_BASE = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/far/vol_01_to_07_ALL/2021/"
CVS_ALL = "output/CFR_48_20212023-07-12_23-53-43.csv"
csv_file_all = CFR_48_HOME_BASE + CVS_ALL
OUTPUT_FOLDER = "results/"
result_csv_folder = CFR_48_HOME_BASE + OUTPUT_FOLDER


def getTimeNow():
    t = time.localtime()
    current_time = time.strftime("%c", t)
    print("Current Time =", current_time)
    return t


def getMetaModel(sentence):
    subject = None
    action_verb = None
    obj = None
    target = None

    for token in sentence:
        if token.dep_ == "nsubj" or token.dep_ == "nsubjpass":
            subject = token
        elif token.dep_ == "ROOT":
            if token.tag_ == "VB" or token.tag_ == "VBP" or token.tag_ == "VBZ":
                action_verb = token
            elif token.tag_ == "VBN":
                action_verb = token.lemma_
        elif token.dep_ == "dobj":
            obj = token
        elif token.dep_ == "pobj":
            target = token
        else:
            pass

    return subject, action_verb, obj, target


def getModality(sentence):
    modality = None
    legal_statement = sentence.text.lower()

    # Deontic operators
    if legal_statement:
        # Permission/Right
        if any(phrase in legal_statement for phrase in {"is required to"}):
            modality = "permission"
        elif any(phrase in legal_statement for phrase in {"can", "may", "could", "might"}):
            modality = "permission"

        # Obligation
        if any(phrase in legal_statement for phrase in
               {"is required to", "may not", "is prohibited to", "is subject to"}):
            modality = "obligation"
        elif any(phrase in legal_statement for phrase in {"should", "must", "shall"}):
            modality = "obligation"

        # Privilege
        if any(phrase in legal_statement for phrase in {"may not", "could not", "might not"}):
            modality = "dispensation"
        elif any(phrase in legal_statement for phrase in {"cannot"}):
            modality = "dispensation"

        # Prohibition/No-Right
        if any(phrase in legal_statement for phrase in {"does not have a right to", "must not", "shall not"}):
            modality = "dispensation"
        elif any(phrase in legal_statement for phrase in {"should not"}):
            modality = "dispensation"

    return modality


def generate_csv_file(result_df):
    try:
        SHAMROQ_PREFIX = "SHAMROQ"
        eCFR_48 = "_eCFR_48_ALL_"
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        fileExt = ".csv"
        result_csv_file = CFR_48_HOME_BASE + SHAMROQ_PREFIX + eCFR_48 + now + fileExt
        result_df.to_csv(result_csv_file, index=False)
        return result_csv_file

    except Exception as e:
        logging.error("An error occurred during CSV file generation: %s", str(e))
        raise


def process_regulations(df_of_regulations):
    list_of_results = []
    result_df = pd.DataFrame(
        columns=["secno", "cfr_subject", "statement", "subject", "modality", "action_verb", "object", "target"])

    for index, row in df_of_regulations.iterrows():
        section_no = row["SECTNO"]
        cfr_subj = row["SUBJECT"]
        for col_name in df_of_regulations.columns:
            if col_name == "TEXT":
                paragraph = row[col_name]
                if isinstance(paragraph, str):
                    try:
                        doc = nlp(paragraph)
                        for sent in doc.sents:
                            modality = getModality(sent)
                            meta_model = getMetaModel(sent)
                            if meta_model:
                                new_row = {
                                    "secno": section_no,
                                    "cfr_subject": cfr_subj,
                                    "statement": sent,
                                    "subject": meta_model[0],
                                    "modality": modality,
                                    "action_verb": meta_model[1],
                                    "object": meta_model[2],
                                    "target": meta_model[3]
                                }
                                new_row_df = pd.DataFrame([new_row], columns=result_df.columns)
                                result_df = pd.concat([result_df, new_row_df], ignore_index=True)
                                list_of_results.append(result_df)
                    except Exception as e:
                        logging.error("An error occurred during regulations processing: %s", str(e))
                        raise

    return result_df


def read_csv_file(csv_file):
    try:
        # read the csv file into a "dataframe"
        df_of_regulations = pd.read_csv(csv_file)
        return df_of_regulations

    except FileNotFoundError as e:
        logging.error("CSV file not found: %s", str(e))
        raise

    except pd.errors.ParserError as e:
        logging.error("Error parsing CSV file: %s", str(e))
        raise


def main():
    try:
        getTimeNow()
        # Configure logging
        logging.basicConfig(filename='LF_classifyCFRXML.log', level=logging.DEBUG,
                            format='%(asctime)s - %(levelname)s - %(message)s')

        df_of_regulations = read_csv_file(csv_file_all)
        result_df = process_regulations(df_of_regulations)
        result_csv_file = generate_csv_file(result_df)
        print(result_csv_file)

        getTimeNow()

    except FileNotFoundError as e:
        logging.error("CSV file not found: %s", str(e))

    except pd.errors.ParserError as e:
        logging.error("Error parsing CSV file: %s", str(e))

    except Exception as e:
        logging.error("An error occurred: %s", str(e))


if __name__ == '__main__':
    main()
