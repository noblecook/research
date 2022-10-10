import requests
import spacy
import time
from spacy.matcher import Matcher
nlp = spacy.load("en_core_web_sm")
encoding = 'utf-8'
'''
    print(response)
    print(response.text)
    print(type(response.text))
    time.sleep(1000)
'''
XML_HEADER = [{'TEXT': "<?xml version=\"1.0\" encoding=\"UTF-8\"?"},
              {'TEXT': "<DIV8 N=\"312.5\" TYPE=\"SECTION\" VOLUME=\"1\">"}]
right_pattern_01 = [{'LOWER': 'has'},
                    {'LOWER': 'a'},
                    {'LOWER': 'right'},
                    {'LOWER': 'to'},
                    {'POS': 'VERB'}]
right_pattern_02 = [{'LOWER': 'has'},
                    {'LOWER': 'the'},
                    {'LOWER': 'right'},
                    {'LOWER': 'to'},
                    {'POS': 'VERB'}]
right_pattern_03 = [{'LOWER': 'retains'},
                    {'LOWER': 'the'},
                    {'LOWER': 'right'},
                    {'LOWER': 'to'},
                    {'POS': 'VERB'}]

obligation_pattern_01 = [{'LOWER': 'must'},
                         {'POS': 'VERB'}]
obligation_pattern_02 = [{'LOWER': 'is'},
                         {'LOWER': 'required'},
                         {'LOWER': 'to'},
                         {'POS': 'VERB'}]
obligation_pattern_03 = [{'LOWER': 'shall'},
                         {'POS': 'VERB'}, ]
obligation_pattern_04 = [{'LOWER': 'may'},
                         {'LOWER': 'not'}]
obligation_pattern_05 = [{'LOWER': 'is'},
                         {'LOWER': 'prohibited'}]
obligation_pattern_06 = [{'LOWER': 'is'},
                         {'LOWER': 'subject'},
                         {'LOWER': 'to'},
                         {'POS': 'VERB'}]
priv_pattern_00 = [{'LOWER': 'may'},
                   {'IS_PUNCT': True, 'OP': '?'}]

priv_pattern_01 = [{'LOWER': 'may'},
                   {'POS': 'ADV', 'OP': '?'},
                   {'IS_PUNCT': True, 'OP': '?'},
                   {'POS': 'VERB'}]
priv_pattern_02 = [{'LOWER': 'may'},
                   {'LOWER': 'elect'},
                   {'LOWER': 'not'},
                   {'LOWER': 'to'}]
priv_pattern_03 = [{'LOWER': 'is'},
                   {'LOWER': 'not'},
                   {'LOWER': 'required'},
                   {'LOWER': 'to'},
                   {'POS': 'VERB'}]
priv_pattern_04 = [{'LOWER': 'requirement'},
                   {'LOWER': 'does'},
                   {'LOWER': 'not'},
                   {'LOWER': 'apply'},
                   {'LOWER': 'to'},
                   {'POS': 'VERB'}]
priv_pattern_05 = [{'LOWER': 'is'},
                   {'LOWER': 'permitted'},
                   {'LOWER': 'to'},
                   {'POS': 'VERB'}]
priv_pattern_06 = [{'LOWER': 'at'},
                   {'LOWER': 'the'},
                   {'LOWER': 'election'},
                   {'LOWER': 'of'},
                   {'POS': 'NOUN'}]
priv_pattern_07 = [{'LOWER': 'is'},
                   {'LOWER': 'not'},
                   {'LOWER': 'subject'},
                   {'LOWER': 'to'},
                   {'POS': 'VERB'}]

shamroqMatcher = Matcher(nlp.vocab)

shamroqMatcher.add("?XML Version", [XML_HEADER])
shamroqMatcher.add("RIGHT01", [right_pattern_01])
shamroqMatcher.add("RIGHT02", [right_pattern_02])
shamroqMatcher.add("RIGHT03", [right_pattern_03])

shamroqMatcher.add("OBLIGATION01", [obligation_pattern_01])
shamroqMatcher.add("OBLIGATION02", [obligation_pattern_02])
shamroqMatcher.add("OBLIGATION03", [obligation_pattern_03])
shamroqMatcher.add("OBLIGATION04", [obligation_pattern_04])
shamroqMatcher.add("OBLIGATION05", [obligation_pattern_05])
shamroqMatcher.add("OBLIGATION06", [obligation_pattern_06])

shamroqMatcher.add("PRIVILEGE01", [priv_pattern_01])
shamroqMatcher.add("PRIVILEGE02", [priv_pattern_02])
shamroqMatcher.add("PRIVILEGE03", [priv_pattern_03])
shamroqMatcher.add("PRIVILEGE04", [priv_pattern_04])
shamroqMatcher.add("PRIVILEGE05", [priv_pattern_05])
shamroqMatcher.add("PRIVILEGE06", [priv_pattern_06])
shamroqMatcher.add("PRIVILEGE07", [priv_pattern_07])


def shamroq(regText):

    for line in regText.iter_lines():
        myContent = str(line, encoding)
        doc = nlp(myContent)
        assert doc.has_annotation("SENT_START")
        for sent in doc.sents:
            print(sent)
            #time.sleep(3)
            #store each sentence in a data structure, then stop
            '''
            for match_id, start, end in shamroqMatcher(doc2):
                print("---------- inside Matcher ------\n")
                print(doc2)
                time.sleep(5)
                string_id = nlp.vocab.strings[match_id]  # Get string representation
                span = doc2[start:end]  # The matched span
                # print(match_id, string_id, start, end, span.text)
                print(string_id, span.text)
                time.sleep(5)
            '''
        print("---------- FINISHED SENTENCE ROUND for sent in doc.sents:------\n")
        time.sleep(2)



def main():
    print("/------------------------------------------/")
    print("... starting main()")
    print("/------------------------------------------/")
    print("\n")
    test2 = "https://www.ecfr.gov/api/versioner/v1/full/2020-01-01/title-16.xml?chapter=I&subchapter=C&part=312&section=312.5"
    response = requests.get(test2)
    shamroq(response)

    print("\n")
    print("/------------------------------------------/")
    print("... completing main()")
    print("/------------------------------------------/")


if __name__ == '__main__':
    main()


"""
 for nc in doc.noun_chunks:
                print(nc)
                time.sleep(2)
            time.sleep(3)
"""
