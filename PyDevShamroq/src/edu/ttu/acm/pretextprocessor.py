import time
import spacy
import hashlib
import pandas as pd
import openai
import os

MODEL_LOCATION = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/shamroq.training-TRAINING.jsonl"

# key reference - https://docs.pinecone.io/docs/openai
# completion example in python - https://beta.openai.com/docs/api-reference/completions/create?lang=python
# completion "create" API - https://beta.openai.com/docs/api-reference/completions/create


def initializeModel():
    openai.api_key = os.environ["OPENAI_API_KEY"]
    openai.organization = os.environ["OPENAI_API_ORGANIZATION"]

    # prints the list of models
    # print("openai.Model.list() Type --> ", type(openai.Model.list()))
    # print(openai.Model.list())
    return openai


def getResponse(openaiModel, regPrompt):
    response = openaiModel.Completion.create(
        model="text-davinci-003",
        prompt=regPrompt,
        temperature=.8,
        max_tokens=1024,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    return response


def main():
    print("/------------------------------------------/")
    print("... starting main()")
    print("/------------------------------------------/")
    print("\n")

    context = "I want you to act as an attorney. I will give you a section of a regulation. "
    openaigoal = "You will split and rephrase each regulation into multiple shorter if/then statements that express one idea. "
    supplementalInfo = "You will express each if/then statement in the simple present tense. "

    inputTag = "Regulation: "
    text = "An operator must obtain verifiable parental consent before any collection, use, or disclosure of personal information from children, including consent to any material change in the collection, use, or disclosure practices to which the parent has previously consented. "
    regPrompt = context + openaigoal + supplementalInfo + inputTag + text

    myOpenai = initializeModel()
    myResponse = getResponse(myOpenai, regPrompt)
    weiredResponseString = myResponse["choices"][0]["text"]
    lines = weiredResponseString.strip().split("\n")

    print("Open AI myResponse ", type(myResponse))
    print("Open AI myResponse ", myResponse)
    print("PROMPT: ", regPrompt, "\n")
    print("RESPONSE :", weiredResponseString, "\n")

    # (1) Now remove all the spaces at front and end of the weired formatted string with strip()
    # (2) Then remove the newline characters with split(\n) because the openai response returns lines
    # and the result is stored in a python list
    print("RESPONSE (SPLIT) :", lines)
    print("<<<<------------------------------------>>>>>\n\n")

    # Change the display options to show more text
    pd.set_option('max_colwidth', 80)

    # Load the list of lines into a DataFrame
    df = pd.DataFrame()



    # Create a hash object
    hash_object = hashlib.md5()

    # Hash the string
    hash_object.update(regPrompt.encode())

    # Get the hexadecimal representation of the hash
    hash_value = hash_object.hexdigest()

    for lineItem in lines:
        new_row_data = [{
            'promptID': hash_value,
            'promptText': regPrompt,
            'completion': lineItem,
            'changes': None,
            'comments': None,
            'open1': None,
            'open2': None
        }]
        temp = pd.DataFrame(new_row_data)
        df = pd.concat([df, temp], ignore_index=True)

    # Remove the empty string
    #df.dropna(inplace=True)

    # Print the DataFrame
    # print("DataFrame ", df)

    # Remove the empty string
    df = df[df.completion != ""]

    # Print a specific column
    print(df[["promptID", "completion"]])

    print("/------------------------------------------/")
    print("... completing main()")
    print("/------------------------------------------/")


if __name__ == '__main__':
    main()
