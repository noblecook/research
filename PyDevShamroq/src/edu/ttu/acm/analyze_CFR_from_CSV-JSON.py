import os
import logging
import time
import spacy
import pandas as pd
import srsly
from datetime import datetime
nlp = spacy.load("en_core_web_lg")

#Todo put this code in a json config file.

CFR_48_HOME_BASE = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/far/vol_01_to_07_ALL/2019/"
TITLE_48_ALL = "output/CFR_48_20192023-07-13_20-46-11.csv"
csv_cfr_input_all = CFR_48_HOME_BASE + TITLE_48_ALL

CFR_48_HOME_BASE_TEST = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/far/vol_01_to_07_ALL/"
TITLE_48_TEST = "Josh-Saha-Test-File/eCFR_48_TEST.csv"
csv_cfr_input_test = CFR_48_HOME_BASE_TEST + TITLE_48_TEST

linguisticFeatures = ['TEXT', 'PATTERN', 'SPAN', 'SUBJ', 'VERB', 'OBJECT']
df = pd.DataFrame(columns=linguisticFeatures)
shamroqCfg = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/shamroq-patterns-rules.jsonl"


'''
Adding items to the nlp pipeline
https://spacy.io/usage/processing-pipelines
'''
patterns = srsly.read_jsonl(shamroqCfg)
ruler = nlp.add_pipe("span_ruler")
ruler.add_patterns(patterns)


def getTimeNow():
    t = time.localtime()
    current_time = time.strftime("%c", t)
    print("Current Time =", current_time)
    return t


# https://demos.explosion.ai/matcher
def classifySpan(text):
    try:
        doc = nlp(text)
        predication = None
        for span in doc.spans["ruler"]:
            predication = span.label_, span.text
        return predication
    except Exception as e:
        # Handle the exception here (e.g., log the error)
        logging.error("Error in classifySpan: %s", str(e))
        raise


def process_regulations(df_of_regulations):
    result_df = pd.DataFrame(
        columns=["SECTNO", "CFRSubject", "Original_sentence", "Matched_Label", "Matched_Text"])

    for index, row in df_of_regulations.iterrows():
        section_no = row["SECTNO"]
        cfr_subj = row["SUBJECT"]
        for col_name in df_of_regulations.columns:
            if col_name == "TEXT":
                paragraph = row[col_name]
                if isinstance(paragraph, str):
                    doc = nlp(paragraph)
                    try:
                        result_df = process_sentences(doc, section_no, cfr_subj, result_df)
                    except Exception as e:
                        # Handle the exception here (e.g., log the error)
                        logging.error("Error processing sentences: %s", str(e))
                else:
                    pass
            else:
                pass
    return result_df


def process_sentences(doc, section_no, cfr_subj, result_df):
    for sent in doc.sents:
        try:
            components = classifySpan(sent.text)
            if components:
                new_row = {
                    "SECTNO": section_no,
                    "CFRSubject": cfr_subj,
                    "Original_sentence": sent,
                    "Matched_Label": components[0],
                    "Matched_Text": components[1]
                }
                new_row_df = pd.DataFrame([new_row], columns=result_df.columns)
                result_df = pd.concat([result_df, new_row_df], ignore_index=True)

        except ValueError as e:
            # Handle the ValueError
            logging.error("ValueError occurred: %s", str(e))

        except TypeError as e:
            # Handle the TypeError
            logging.error("TypeError occurred: %s", str(e))

        except AttributeError as e:
            # Handle the AttributeError
            logging.error("AttributeError occurred: %s", str(e))

        except Exception as e:
            # Handle any other unexpected exceptions
            logging.error("Unexpected Exception occurred: %s", str(e))

    return result_df


def generate_csv_file(result_df):
    try:
        now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
        fileExt = ".csv"
        results = "results/"
        CLASSIFIED_PREFIX = "CLASSIFIED"
        eCFR_48 = "_eCFR_48_ALL_"

        # Define the file name and path
        result_csv_file = CFR_48_HOME_BASE + results + CLASSIFIED_PREFIX + eCFR_48 + now + fileExt

        # Create the output directory if it doesn't exist
        output_dir = os.path.dirname(result_csv_file)
        os.makedirs(output_dir, exist_ok=True)

        result_df.to_csv(result_csv_file, index=False)
        return result_csv_file
    except Exception as e:
        logging.error("An error occurred during CSV file generation: %s", str(e))
        raise


def read_csv_file(csv_file):
    try:
        absolute_path = os.path.abspath(csv_file)
        # Extract filename and size
        filename = os.path.basename(absolute_path)
        file_size = os.path.getsize(absolute_path)

        # Log filename and size
        logging.info("Reading CSV file: %s (Size: %d bytes)", filename, file_size)
        df_of_regulations = pd.read_csv(csv_file)
        return df_of_regulations
    except FileNotFoundError as e:
        logging.error("CSV file not found: %s", str(e))
        raise
    except pd.errors.ParserError as e:
        logging.error("Error parsing CSV file: %s", str(e))
        raise


def init():
    logging.basicConfig(filename='app.shamroq.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')


def main(input_csv):
    getTimeNow()
    init()
    df_of_regulations = read_csv_file(input_csv)
    result_df = process_regulations(df_of_regulations)
    result_csv_file = generate_csv_file(result_df)
    # Log filename and size
    logging.info("resulting file: %s", result_csv_file)

    print(result_csv_file)
    getTimeNow()


# -------------------------------------
# @Author Patrick Cook
# @Date: circa 2021 initial release
# ANALYZE:  analyze_CFR_from_CSV.py
# The module read the CSV file (i.e., the output from the PREPROCESSING module)
# into a data frame.  The main function iterates through each row and
# processes the "TEXT" column by invoking the “classifySpan” function. The output
# is a .csv file that contains each statement and associated deontic expression
# -------------------------------------
if __name__ == '__main__':
    main(csv_cfr_input_test)