import time
import spacy
import pandas as pd
import srsly
from spacy.matcher import Matcher
from datetime import datetime


CFR_48_HOME_BASE = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/far/"
TITLE_48_SHAMROQ_FILE = "SHAMROQ_TEST.csv"
TITLE_48_INPUT_TEST = "eCFR_48_TEST.csv"
TITLE_48_VOLUME_01_OLD = "eCFR_48_VOL_01_2023-05-13_12-17-55.csv"
TITLE_48_VOLUME_01 = "eCFR_48_VOL_01.csv"
csv_shamroq_test = CFR_48_HOME_BASE + TITLE_48_SHAMROQ_FILE
csv_cfr_test = CFR_48_HOME_BASE + TITLE_48_VOLUME_01
csv_cfr_input_test = CFR_48_HOME_BASE + TITLE_48_INPUT_TEST

linguisticFeatures = ['TEXT', 'PATTERN', 'SPAN', 'SUBJ', 'VERB', 'OBJECT']
df = pd.DataFrame(columns=linguisticFeatures)
nlp = spacy.load("en_core_web_lg")
patternCfg = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/patterns.jsonl"
shamroqCfg = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/shamroq-patterns-rules.jsonl"
patternMMCfg = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/patterns-meta-model.jsonl"
patternPrepPhrCfg = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/patterns-prep-phrases.jsonl"
pattern_Joshi_Rules = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/patterns-johsi-rules.jsonl"
pattern_modal_verbs = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/modal_verbs_rules.jsonl"
'''
Adding items to the nlp pipeline
https://spacy.io/usage/processing-pipelines
'''


def getTimeNow():
    t = time.localtime()
    current_time = time.strftime("%c", t)
    print("Current Time =", current_time)
    return t


# https://demos.explosion.ai/matcher
def classifySpan(text):
    doc = nlp(text)
    predication = None
    # SpanRule - https://spacy.io/api/spanruler | https://spacy.io/usage/rule-based-matching#spanruler
    for span in doc.spans["ruler"]:
        predication = span.label_, span.text
    return predication


def init():
    patterns = srsly.read_jsonl(pattern_modal_verbs)
    matcher = Matcher(nlp.vocab)
    for pattern in patterns:
        for key, value in pattern.items():
            print(key, ":", value)
            time.sleep(0)
        matcher.add("custom_pattern", pattern)

    time.sleep(55)
    nlp.add_pipe(matcher)
    return matcher

def main():
    init()
    getTimeNow()

    # read the csv file into a "dataframe"

    # Joshi's four sentence
    df_of_regulations = pd.read_csv(csv_cfr_input_test)

    # df_of_regulations = pd.read_csv(csv_cfr_test)

    list_of_results = []
    result_df = pd.DataFrame(
        columns=["SECTNO", "CFRSubject", "Original_sentence", "Matched_Label", "Matched_Text"])

    # Iterate through each row of the DataFrame
    for index, row in df_of_regulations.iterrows():
        # print(f"Processing row {index}:")
        section_no = row["SECTNO"]
        cfr_subj = row["SUBJECT"]
        for col_name in df_of_regulations.columns:
            if col_name == "TEXT":
                paragraph = row[col_name]
                if isinstance(paragraph, str):
                    doc = nlp(paragraph)
                    for sent in doc.sents:
                        # print("Original Sentence: ", sent.text)
                        # time.sleep(0)
                        components = classifySpan(sent.text)
                        if components:
                            print("")
                            print("FOUND MATCH - sentence ", sent.text)
                            print("Printing Components", components)
                            print("")
                            new_row = {
                                "SECTNO": section_no,
                                "CFRSubject": cfr_subj,
                                "Original_sentence": sent,
                                "Matched_Label": components[0],
                                "Matched_Text": components[1]
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
    MATCHED_PREFIX = "MATCHED"
    eCFR_48 = "_eCFR_48_RESULTS_"
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    fileExt = ".csv"
    result_csv_file = CFR_48_HOME_BASE + MATCHED_PREFIX + eCFR_48 + now + fileExt
    result_df.to_csv(result_csv_file, index=False)
    print(result_csv_file)
    getTimeNow()


if __name__ == '__main__':
    main()
