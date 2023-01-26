import time
import spacy
import hashlib
import pandas as pd
import openai
OPENAI_API_ORGANIZATION = "org-L1oXrXAuJvjt0NRH6zbtHn6kb"
OPENAI_API_KEY = "sk-Q38XucNYjFuKF4N74QS52T3BlbkFJcQISOmysCUjaE9T6lTEL"
MODEL_LOCATION = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/config/shamroq.training-TRAINING.jsonl"

# key reference - https://docs.pinecone.io/docs/openai
# completion example in python - https://beta.openai.com/docs/api-reference/completions/create?lang=python
# completion "create" API - https://beta.openai.com/docs/api-reference/completions/create


def initializeModel():
    openai.organization = OPENAI_API_ORGANIZATION
    openai.api_key = OPENAI_API_KEY
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

    context = "I want you to act as an attorney. I will give you a section of a regulation."
    openaigoal = "You will split and rephrase each regulation into multiple shorter if/then statements that express one idea."
    supplementalInfo = "You will express each if/then statement in the simple present tense."

    inputTag = "Regulation: "
    text = "An operator must obtain verifiable parental consent before any collection, use, or disclosure of personal information from children, including consent to any material change in the collection, use, or disclosure practices to which the parent has previously consented."
    regPrompt = context + openaigoal + supplementalInfo + inputTag + text

    myOpenai = initializeModel()
    myResponse = getResponse(myOpenai, regPrompt)
    responseString = myResponse["choices"][0]["text"]

    print("Open AI Response ", myResponse)
    print("PROMPT: ", regPrompt, "\n")
    print("RESPONSE :", responseString)
    print("RESPONSE (SPLIT) :", responseString.strip().split("\n"))
    print("<<<<------------------------------------>>>>>\n\n")

    # Extract the generated text from the response
    responseText = myResponse["choices"][0]["text"]
    lines = responseText.strip().split("\n")

    # Remove leading and trailing whitespace from each line
    lines = [line.strip() for line in lines]

    # Load the list of lines into a DataFrame
    df = pd.DataFrame(lines, columns=["completion"])

    # Remove the empty string
    df = df[df.completion != ""]

    # Define the string


    # Create a hash object
    hash_object = hashlib.md5()

    # Hash the string
    hash_object.update(regPrompt.encode())

    # Get the hexadecimal representation of the hash
    hash_value = hash_object.hexdigest()

    # Create additional columns
    df["promptID"] = hash_value
    df["a"] = None
    df["b"] = None
    df["x"] = None
    df["y"] = None
    df["z"] = None

    # Remove the empty string
    #df.dropna(inplace=True)

    # Change the display options to show more text
    pd.set_option('max_colwidth', 80)

    # Print the DataFrame
    # print("DataFrame ", df)

    # Print a specific column
    print(df[["promptID", "completion"]])

    print("/------------------------------------------/")
    print("... completing main()")
    print("/------------------------------------------/")


if __name__ == '__main__':
    main()
