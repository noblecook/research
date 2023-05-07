import time
from datetime import datetime
import pandas as pd
import xml.etree.ElementTree as eTree
import spacy
from spacy.matcher import Matcher

CFR_48_HOME_BASE = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/far/"
CFR_48_VOLUME_01 = "CFR-2020-title48-vol1.xml"
CFR_48_VOLUME_02 = "CFR-2020-title48-vol2.xml"
CFR_48_VOLUME_03 = "CFR-2020-title48-vol3.xml"
CFR_48_VOLUME_04 = "CFR-2020-title48-vol4.xml"
CFR_48_VOLUME_05 = "CFR-2020-title48-vol5.xml"
CFR_48_VOLUME_06 = "CFR-2020-title48-vol6.xml"
CFR_48_VOLUME_07 = "CFR-2020-title48-vol7.xml"

eCFR_48_DATASET_VOL_01 = CFR_48_HOME_BASE + CFR_48_VOLUME_01
eCFR_48_DATASET_VOL_02 = CFR_48_HOME_BASE + CFR_48_VOLUME_02
eCFR_48_DATASET_VOL_03 = CFR_48_HOME_BASE + CFR_48_VOLUME_03
eCFR_48_DATASET_VOL_04 = CFR_48_HOME_BASE + CFR_48_VOLUME_04
eCFR_48_DATASET_VOL_05 = CFR_48_HOME_BASE + CFR_48_VOLUME_05
eCFR_48_DATASET_VOL_06 = CFR_48_HOME_BASE + CFR_48_VOLUME_06
eCFR_48_DATASET_VOL_07 = CFR_48_HOME_BASE + CFR_48_VOLUME_07

eCFR_48_ALL = [eCFR_48_DATASET_VOL_01, eCFR_48_DATASET_VOL_02, eCFR_48_DATASET_VOL_03, eCFR_48_DATASET_VOL_04,
               eCFR_48_DATASET_VOL_05, eCFR_48_DATASET_VOL_06, eCFR_48_DATASET_VOL_07]

CFR_16_HOME_BASE = "C:/Users/patri/OneDrive/Documents/20 PhD/seke-conference/IJSEKE - Submission Guidelines/2023-IJSEKE-manuscript/govinfo.gov.16CFR.Volumes/"
CFR_16_VOLUME_01 = "CFR-2022-title16-vol1.xml"
CFR_16_VOLUME_02 = "CFR-2022-title16-vol2.xml"
eCFR_16_DATASET_VOL_01 = CFR_16_HOME_BASE + CFR_16_VOLUME_01
eCFR_16_DATASET_VOL_02 = CFR_16_HOME_BASE + CFR_16_VOLUME_02

eCFR_16_ALL = [eCFR_16_DATASET_VOL_01, eCFR_16_DATASET_VOL_02]


def extract_text(text):
    nlp = spacy.load("en_core_web_lg")
    doc = nlp(text)
    matcher = Matcher(nlp.vocab)

    # Define the pattern for subparts like (a)
    pattern_alpha = [
        {"TEXT": "(", "OP": "+", "IS_SENT_START": True},
        {"IS_ALPHA": True, "LENGTH": 1},
        {"TEXT": ")", "OP": "+"},
        {"IS_TITLE": True}
    ]

    # Define the pattern for subparts like (1)
    pattern_numeric = [
        {"TEXT": "(", "OP": "+", "IS_SENT_START": True},
        {"IS_DIGIT": True},
        {"TEXT": ")", "OP": "+"},
        {"IS_TITLE": True}
    ]

    # Add the patterns to the matcher
    matcher.add("subpart_pattern_alpha", [pattern_alpha])
    matcher.add("subpart_pattern_numeric", [pattern_numeric])
    matches = matcher(doc)

    results = []
    for i in range(len(matches)):
        match_id, start, end = matches[i]

        # Get the start of the next match or the end of the document
        next_start = matches[i + 1][1] if i + 1 < len(matches) else len(doc)

        # Get the subpart and the corresponding text
        subpart = doc[start:end].text
        text_after_subpart = doc[end:next_start].text.strip()

        # Store the result as a complete sentence in the list
        results.append(f"{subpart} {text_after_subpart}")

    return results


def initializeDataFrame():
    # Define the column names
    column_names = ["section_no", "subject", "text", "modal_verb", "deontic_operator", "antecedent", "consequent"]
    # Load the list of lines into a DataFrame
    iDF = pd.DataFrame(columns=column_names)
    # Change the display options to show more text
    pd.set_option('max_colwidth', 80)
    return iDF


def print_list_of_provisions(cfr_metadata_list):
    df = initializeDataFrame()
    my_provision_list = []
    for subpart in cfr_metadata_list:
        row_data = {}
        for key, value in subpart.items():
            row_data[key] = value
        my_provision_list.append(row_data)
        df = pd.DataFrame(my_provision_list)
    return df


def print_list_of_provisions_BACKUP(cfr_metadata_list):
    df = initializeDataFrame()
    my_provision_list = []

    for subpart in cfr_metadata_list:
        row_data = {}
        for key, value in subpart.items():
            if key == "TEXT":
                subparts = extract_text(value)
                if subparts:
                    print(f'{key}: {value}')
                    row_data[key] = value
                    # print(".\n.\n.\n")
                    for sent in subparts:
                        pass
                        # print(sent)
                else:
                    pass
                    print(f'{key}: {value}')
                    row_data[key] = value
            else:
                pass
                print(f'{key}: {value}')
                row_data[key] = value

        my_provision_list.append(row_data)
        df = pd.DataFrame(my_provision_list)
    return df


def getCFRMetaData(reg_xml_file_location):
    # use XSLT to get only two important elements
    # store the results and return
    tree = eTree.parse(reg_xml_file_location)
    root = tree.getroot()
    cfrMetaDataList = []

    for subpart_element in root.findall('.//SECTION'):
        subpart_meta_data = {
            'SECTNO': '',
            'SUBJECT': '',
            'TEXT': ''
        }

        sectno_elements = subpart_element.findall('.//SECTNO')
        if len(sectno_elements) > 0:
            subpart_meta_data['SECTNO'] = ", ".join(
                [element.text for element in sectno_elements if element.text is not None])

        subject_elements = subpart_element.findall('.//SUBJECT')
        if len(subject_elements) > 0:
            subpart_meta_data['SUBJECT'] = ", ".join(
                [element.text for element in subject_elements if element.text is not None])

        text_elements = subpart_element.findall('.//P')
        if len(text_elements) > 0:
            text = ""
            for element in text_elements:
                text_fragments = [text_fragment.strip() for text_fragment in element.itertext()]
                text += " ".join(text_fragments) + " "
            text = " ".join(text.split())  # remove extra whitespace
            subpart_meta_data['TEXT'] = text

        cfrMetaDataList.append(subpart_meta_data)

    return cfrMetaDataList


def createCSV(dff, dataSetName):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    fileExt = ".csv"

    # Define the file name and path
    file_name = CFR_48_HOME_BASE + dataSetName + now + fileExt

    # Write the DataFrame to a CSV file
    dff.to_csv(file_name, index=False)
    return file_name


def getTimeNow():
    t = time.localtime()
    current_time = time.strftime("%c", t)
    print("Current Time =", current_time)
    return t


def main():
    getTimeNow()
    df_all_regulations = pd.DataFrame()
    for regulation in eCFR_48_ALL:
        metadata = getCFRMetaData(regulation)
        df_regulation = print_list_of_provisions(metadata)
        df_all_regulations = pd.concat([df_all_regulations, df_regulation], ignore_index=True)

    # print(df_all_regulations)
    cfr_extracted_csv_file = createCSV(df_all_regulations, "eCFR_48_ALL_")
    print(cfr_extracted_csv_file)
    getTimeNow()


if __name__ == '__main__':
    main()

