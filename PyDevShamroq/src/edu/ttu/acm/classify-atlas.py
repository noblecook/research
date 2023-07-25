import logging
import os
import time

import openai
import pandas as pd
import spacy

nlp = spacy.load("en_core_web_lg")
ATLAS_HOME_BASE = "C:/Users/patri/OneDrive/Documents/20 PhD/20 ATLAS/data/"
CSV_TEST_FILE = "eCFR_48_TEST.csv"
CSV_TEST_FILE_2 = "eCFR_48_VOL_01.csv"
ATLAS_INPUT_TEST = ATLAS_HOME_BASE + CSV_TEST_FILE_2


def init():
    logging.basicConfig(filename='atlas.shamroq.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')


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


def process_regulations(df_of_regulations):
    result_df = pd.DataFrame(
        columns=["SECTNO", "SUBJECT", "ORIGINAL", "CONDITIONAL"])

    for index, row in df_of_regulations.iterrows():
        section_no = row["SECTNO"]
        cfr_subj = row["SUBJECT"]
        for col_name in df_of_regulations.columns:
            if col_name == "TEXT":
                paragraph = row[col_name]
                if isinstance(paragraph, str):
                    try:
                        logging.info("getOpenAIResponse(text): %s", paragraph)
                        getOpenAIResponse(paragraph)
                    except Exception as e:
                        # Handle the exception here (e.g., log the error)
                        logging.error("Error processing sentences: %s", str(e))
                else:
                    pass
            else:
                pass
    return result_df


# https://help.openai.com/en/articles/6897213-openai-library-error-types-guidance
def getOpenAIResponse(text):
    _openApi = initializeModel()
    context_expertise = "You are an Attorney with a deep understanding of federal laws and regulations. "
    context_specialization = "You have three Ph.D.s in linguistics, mathematics, and logic. "
    context_inquiry = "I will give you a section of a regulation. "
    context_response = "You will spit and rephrase the regulation into shorter if/then statements. "
    openaigoal = "You must express the if/then statements in the simple present tense. "
    supplementalInfo = "Each if/then statement must address each action separately. "
    inputTag = "Here is the regulation: "
    regPrompt = context_expertise + context_specialization + context_inquiry + context_response + openaigoal \
                + supplementalInfo + inputTag + text
    # regPrompt = context + openaigoal + supplementalInfo + inputTag + text
    gptModel1 = "text-davinci-003"
    logging.info("getOpenAIResponse(text): %s", regPrompt)

    response = None
    try:

        response = _openApi.Completion.create(
            model=gptModel1,
            prompt=regPrompt,
            temperature=0.1,
            max_tokens=2048,
            top_p=1.0,
            frequency_penalty=0,
            presence_penalty=0
        )
    except _openApi.error.Timeout as e:
        # Handle timeout error, e.g. retry or log
        logging.error(f"OpenAI API request timed out: {str(e)}")
        print(f"OpenAI API request timed out: {e}")
        pass
    except _openApi.error.APIError as e:
        # Handle API error, e.g. retry or log
        logging.error(f"OpenAI API returned an API Error: {str(e)}")
        print(f"OpenAI API returned an API Error: {e}")
        pass
    except _openApi.error.APIConnectionError as e:
        # Handle connection error, e.g. check network or log
        logging.error(f"OpenAI API request failed to connect: {str(e)}")
        print(f"OpenAI API request failed to connect: {e}")
        pass
    except _openApi.error.InvalidRequestError as e:
        # Handle invalid request error, e.g. validate parameters or log
        logging.error(f"OpenAI API request was invalid: {str(e)}")
        print(f"OpenAI API request was invalid: {e}")
        pass
    except _openApi.error.AuthenticationError as e:
        # Handle authentication error, e.g. check credentials or log
        logging.error(f"OpenAI API request was not authorized: {str(e)}")
        print(f"OpenAI API request was not authorized: {e}")
        pass
    except _openApi.error.PermissionError as e:
        # Handle permission error, e.g. check scope or log
        logging.error(f"OpenAI API request was not permitted: {str(e)}")
        print(f"OpenAI API request was not permitted: {e}")
        pass
    except _openApi.error.RateLimitError as e:
        # Handle rate limit error, e.g. wait or log
        logging.error(f"OpenAI API request exceeded rate limit: {str(e)}")
        print(f"OpenAI API request exceeded rate limit: {e}")
        pass

    responseText = response["choices"][0]["text"]
    logging.info("Original Text: %s", text)
    logging.info("The Open AI Response - i.e. responseText: %s", responseText)
    print("Original Text:", text)
    print("The Open AI Response - i.e. responseText:", responseText)
    print("\n")
    time.sleep(1)

    lines = responseText.strip().split("\n")
    logging.info("The response after strip() and split(\n): %s", lines)
    # print("This is lines after strip() and split(\n):  ", lines)
    # time.sleep(25)

    return lines


def initializeModel():
    try:
        openai.api_key = os.environ["OPENAI_API_KEY"]
        openai.organization = os.environ["OPENAI_API_ORGANIZATION"]
        logging.info("Successfully initialized the OpenAI model.")
        return openai
    except KeyError as e:
        logging.error(f"Environment variable not set: {str(e)}")
        return None
    except Exception as e:
        logging.error(f"An unexpected error occurred: {str(e)}")
        return None


def main():
    init()
    df_of_regulations = read_csv_file(ATLAS_INPUT_TEST)
    results = process_regulations(df_of_regulations)
    print(results)


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
    main()
