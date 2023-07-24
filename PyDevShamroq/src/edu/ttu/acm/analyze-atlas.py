import spacy
import logging


def init():
    nlp = None
    nlp_coref = None
    logging.basicConfig(filename='atlas.shamroq.log', level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

    # Load the large language model
    try:
        nlp = spacy.load("en_core_web_sm")
    except Exception as e:
        logging.error("Failed to load module: nlp.add_pipe(experimental_coref)", e)

    # Load the co-reference Language Model
    try:
        nlp_coref = spacy.load("en_coreference_web_trf")
        nlp_coref.replace_listeners("transformer", "coref", ["model.tok2vec"])
        nlp_coref.replace_listeners("transformer", "span_resolver", ["model.tok2vec"])
    except Exception as e:
        logging.error("Failed to load module: nlp.add_pipe(experimental_coref)", e)

    # Load the co-reference Language Model
    try:
        nlp.add_pipe("coref", source=nlp_coref)
        nlp.add_pipe("span_resolver", source=nlp_coref)
        logging.info("Pipe Names: %s", nlp.pipe_names)
    except Exception as e:
        logging.error("Failed to load module: nlp.add_pipe(experimental_coref)", e)
    return nlp


def perform_ner(doc):
    named_entities = None
    # Extract named entities from the processed text
    try:
        named_entities = [(ent.text, ent.label_) for ent in doc.ents]
        logging.info("Named Entities: %s", named_entities)
    except Exception as e:
        logging.error("Failed to get named entities", e)
    return named_entities


def perform_pos_tags(doc):
    pos_tags = None
    # Extract parts of speech tags from doc
    try:
        pos_tags = [(token.text, token.pos_) for token in doc]
        logging.info("POS Tags : %s", pos_tags)
    except Exception as e:
        logging.error("Failed to get POS tags", e)
    return pos_tags


def perform_dependency_parsing(doc):
    # Extract dependency parse information from the processed text
    dependency_info = []
    try:
        for token in doc:
            dependency_info.append((token.text, token.dep_, token.head.text))

        logging.info("DEP Tags : %s", dependency_info)
    except Exception as e:
        logging.error("Failed to get DEP tags", e)

    return dependency_info


def perform_coref_resolution(doc):
    # Extract co-reference resolution in doc.spans
    try:
        print(doc.spans)
        logging.info("DEP Tags : %s", doc.spans)
    except Exception as e:
        logging.error("Failed to get doc.spans", e)
    return doc.spans


def normalize_variant_forms(doc):
    normalized_tokens = None
    try:
        normalized_tokens = [(token.text, token.lemma_) for token in doc]
        logging.info("Normalized Tokens (Lemma): %s", normalized_tokens)
    except Exception as e:
        logging.error("Failed to get Normalized Tokens", e)
    return normalized_tokens


def main():
    # Process the text
    text = "Mary drove her car to the store. She bought some milk."
    nlp = init()
    doc = nlp(text)
    norm_tokens = normalize_variant_forms(doc)
    print(norm_tokens)






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
