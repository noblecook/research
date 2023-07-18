import os
import logging
import time
import json
from datetime import datetime
import pandas as pd
import xml.etree.ElementTree as eTree
import spacy
from spacy.matcher import Matcher


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

    try:
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
    except() as e:
        logging.error("Error occurred while parsing XML: %s", e)
        return []


def createCSV(dff, dataSetName, cfrHomeBase):
    now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    fileExt = ".csv"
    output = "output/"

    # Define the file name and path
    file_name = cfrHomeBase + output + dataSetName + now + fileExt

    # Create the output directory if it doesn't exist
    output_dir = os.path.dirname(file_name)
    os.makedirs(output_dir, exist_ok=True)

    try:
        # Write the DataFrame to a CSV file
        dff.to_csv(file_name, index=False)
        saved_file = file_name
    except OSError as e:
        logging.error("Cannot save file: %s", e)
        saved_file = None

    return saved_file


def save_cfr_data_to_csv(dataframe, regName):
    cfr_extracted_csv_file = createCSV(dataframe, regName)
    print(cfr_extracted_csv_file)
    return cfr_extracted_csv_file


def extract_cfr_data(regList):
    # Initialize an empty DataFrame
    df_all_regulations = pd.DataFrame()

    # Loop through the list of CFR.xml files
    for regulation in regList:
        metadata = getCFRMetaData(regulation)
        df_regulation = print_list_of_provisions(metadata)
        df_all_regulations = pd.concat([df_all_regulations, df_regulation], ignore_index=True)

    return df_all_regulations


def init(cfr_with_year):
    # Configure logging
    logging.basicConfig(filename='app.shamroq.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Set config file location
    configFile = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/config.json"
    logging.info("Location of Config File: %s", configFile)

    # Load configuration from JSON file
    try:
        # Load configuration from JSON file
        with open(configFile, 'r') as config_file:
            config = json.load(config_file)
    except FileNotFoundError as e:
        logging.error("Config file not found: %s", e)
    except json.JSONDecodeError as e:
        logging.error("Error parsing JSON file: %s", e)
    except Exception as e:
        logging.error("An error occurred while loading configuration: %s", e)

    # extract REG_NAME, BASE URL, & CFR 48 volumes 2021 from config file
    CFR_HOME_BASE = config[cfr_with_year]['HOME_BASE']
    CFR_VOLUMES = config[cfr_with_year]['VOLUMES']
    CFR_REG_NAME = config[cfr_with_year]['REG_NAME']

    CFR_DATASET = [CFR_HOME_BASE + volume for volume in CFR_VOLUMES]
    logging.info("Final dataset: %s", CFR_DATASET)
    return CFR_DATASET, CFR_REG_NAME, CFR_HOME_BASE


def getTimeNow():
    t = time.localtime()
    current_time = time.strftime("%c", t)
    print("Current Time =", current_time)
    return t


def main():
    getTimeNow()
    CFR_WITH_YEAR = "CFR_48_2019"
    dataSet, regName, homeBase = init(CFR_WITH_YEAR)
    df_regs = extract_cfr_data(dataSet)
    logging.info("List of regulations: %s", df_regs)
    cfr_extracted_csv_file = createCSV(df_regs, regName, homeBase)
    print(cfr_extracted_csv_file)
    getTimeNow()


if __name__ == '__main__':
    main()




