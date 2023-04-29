import time
import pandas as pd
from datetime import datetime
import re
import xml.etree.ElementTree as eTree
import spacy
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


def main():
    df_of_regulations = pd.read_csv(csv_file_path)
    # Iterate through each row of the DataFrame
    for index, row in df_of_regulations.iterrows():
        print(f"Processing row {index}:")
        for col_name in df_of_regulations.columns:
            print(f"\t{col_name}: {row[col_name]}")

            # ------------------------------------------- #
            # Here we need to process the information
            # Then reload into a data frame and stored as a csv with results
            # ------------------------------------------- #


        time.sleep(3)



if __name__ == '__main__':
    main()


    '''
        for key, value in df_of_regulations.iterrows():
        # Access and process the data in each column of the row
        print(f"Processing row {key}:")
        print(f"  Column 1: {value['SECTNO']}")
        print(f"  Column 2: {value['SUBJECT']}")
        print(f"  Column 3: {value['TEXT']}")
        time.sleep(5)
        getTimeNow()
    
    '''