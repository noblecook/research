import spacy


def getNormativeStatements(doc):
    antecedent = ""
    consequent = ""
    # Iterate through the tokens in the sentence
    for token in doc:
        # Check if the token is the "if" word
        if token.text.lower() == "if":
            # Iterate through the next tokens until "then"
            for next_token in token.doc[token.i+1:]:
                if next_token.text.lower() == "then":
                    break
                antecedent += next_token.text + " "
        # Check if the token is the "then" word
        elif token.text.lower() == "then":
            # Iterate through the next tokens until end of sentence
            for next_token in token.doc[token.i+1:]:
                consequent += next_token.text + " "

    # print("antecedent:", antecedent)
    # print("consequent:", consequent)

    conditional_dict = {
        "antecedent": antecedent,
        "consequent": consequent
    }
    return conditional_dict


def init(conditional):
    nlp = spacy.load("en_core_web_lg")
    # Process the sentence with spaCy
    doc = nlp(conditional)
    rule = getNormativeStatements(doc)
    return rule


