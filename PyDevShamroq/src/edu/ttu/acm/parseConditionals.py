import time

import spacy


def processConditional(if_then_statement):

    # Initialize Rules
    ruleList = {}
    cond_Antecedent = {}
    cond_Consequent = {}

    # Load the spaCy model
    nlp = spacy.load("en_core_web_lg")

    # Initialize the variables for the antecedent and consequent
    antecedent = ""
    consequent = ""

    # Process the sentence with spaCy
    doc = nlp(if_then_statement)
    # print(doc)

    # Iterate through the tokens in the sentence
    for token in doc:
        # Check if the token is the "if" word
        if token.text.lower() == "if":
            # Iterate through the next tokens until "then"
            for next_token in token.doc[token.i + 1:]:
                if next_token.text.lower() == "then":
                    # print("\n")
                    break
                # -------------------
                #  Load Dictionary
                # -------------------
                antecedent += next_token.text + " "
                # print(antecedent)

                if next_token.dep_ in ['nsubj', 'nsubjpass']:
                    subjList = [str(t) for t in next_token.subtree]
                    subtree_string = ' '.join(subjList)

                    subj_key = 'subject'
                    subj_value = subtree_string
                    cond_Antecedent[subj_key] = subj_value

                    # print("Subject = ", subtree_string)
                elif next_token.dep_ == 'advcl':
                    advcl_predicate_string = next_token.text

                    advcl_key = 'predicate'
                    advcl_value = advcl_predicate_string
                    cond_Antecedent[advcl_key] = advcl_value

                    # print("Predicate = ", advcl_predicate_string)
                elif next_token.dep_ == 'iobj':
                    iobjList = [str(t) for t in next_token.subtree]
                    iobj_string = ' '.join(iobjList)

                    iobj_key = 'iobj'
                    iobj_value = iobj_string
                    cond_Antecedent[iobj_key] = iobj_value

                    # print("Indirect object = ", iobj_string)
                elif next_token.dep_ == 'dobj':
                    dobjList = [str(t) for t in next_token.subtree]
                    dobj_string = ' '.join(dobjList)

                    dobj_key = 'dobj'
                    dobj_value = dobj_string
                    cond_Antecedent[dobj_key] = dobj_value

                    # print("Direct object = ", dobj_string)
                elif next_token.dep_ == 'prep':
                    prepList = [str(t) for t in next_token.subtree]
                    prep_string = ' '.join(prepList)

                    pobj_key = 'pObj'
                    pobj_value = prep_string
                    cond_Antecedent[pobj_key] = pobj_value

                    # print("Preposition object = ", prep_string)

        # Check if the token is the "then" word
        elif token.text.lower() == "then":
            # Iterate through the next tokens until end of sentence
            for next_token in token.doc[token.i + 1:]:
                # -------------------
                #  Load Dictionary
                # -------------------
                # consequent += next_token.text + " "
                # print(consequent)

                if next_token.dep_ in ['nsubj', 'nsubjpass']:
                    subjList = [str(t) for t in next_token.subtree]
                    subtree_string = ' '.join(subjList)

                    subj_key = 'subject'
                    subj_value = subtree_string
                    cond_Consequent[subj_key] = subj_value

                    # print("Subject = ", subtree_string)
                elif next_token.dep_ == 'aux' and next_token.tag_ == 'MD':
                    modality = next_token.text

                    md_key = 'modality'
                    md_value = modality
                    cond_Consequent[md_key] = md_value

                    # print("Modal Verb = ", modality)
                elif next_token.dep_ == 'ROOT':
                    consequent_predicate = next_token.lemma_

                    root_key = 'root'
                    root_value = consequent_predicate
                    cond_Consequent[root_key] = root_value

                    # print("ROOT Predicate = ", consequent_predicate)
                elif next_token.dep_ == 'iobj':
                    iobjList = [str(t) for t in next_token.subtree]
                    iobj_string = ' '.join(iobjList)

                    iobj_key = 'iobj'
                    iobj_value = iobj_string
                    cond_Consequent[iobj_key] = iobj_value

                    # print("Indirect object = ", iobj_string)
                elif next_token.dep_ == 'dobj':
                    dobjList = [str(t) for t in next_token.subtree]
                    dobj_string = ' '.join(dobjList)

                    dobj_key = 'dobj'
                    dobj_value = dobj_string
                    cond_Consequent[dobj_key] = dobj_value

                    # print("Direct object = ", dobj_string)
                else:
                    pass
                consequent += next_token.text + " "
                time.sleep(0)

    # Print the antecedent and consequent
    # print("Antecedent:", antecedent)
    # print("Consequent:", consequent)

    ruleList['antecedent'] = cond_Antecedent
    ruleList['consequent'] = cond_Consequent

    # print("\n")
    # print(ruleList)
    # time.sleep(10)
    return ruleList


# THIS CAN BE REMOVED
def processStatement(stmt):
    rule = processConditional(stmt)
    return rule


def init(input_text):
    result = processStatement(input_text)
    return result
