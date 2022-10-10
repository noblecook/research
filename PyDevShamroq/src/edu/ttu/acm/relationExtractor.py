'''
Created on Feb 21, 2021

@author: patri
https://spacy.io/usage/linguistic-features
Open up a terminal 
python -m spacy download en_core_web_sm
Word wrap "Alt+Shift+Y
'''

import time
import spacy
from spacy import displacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher

nlp = spacy.load("en_core_web_sm")

regText164_510 = '''A covered entity may use or disclose protected health information, provided that the individual is informed in advance of the use or disclosure and has the opportunity to agree to or prohibit or restrict the use or disclosure, in accordance with the applicable requirements of this section. 

The covered entity may orally inform the individual of and obtain the individual's oral agreement or objection to a use or disclosure permitted by this section. 

(a)Standard: Use and disclosure for facility directories(1)Permitted uses and disclosure. Except when an objection is expressed in accordance with paragraphs (a)(2) or (3) of this section, a covered health care provider may:
    (i) Use the following protected health information to maintain a directory of individuals in its facility:
    (A) The individual's name;
    (B) The individual's location in the covered health care provider's facility;
    (C) The individual's condition described in general terms that does not communicate specific medical information about the individual; and
    (D) The individual's religious affiliation; and
    (ii) Use or disclose for directory purposes such information:
    (A) To members of the clergy; or
    (B) Except for religious affiliation, to other persons who ask for the individual by name.
    (2) Opportunity to object.A covered health care provider must inform an individual of the protected health information that it may include in a directory and the persons to whom it may disclose such information (including disclosures to clergy of information regarding religious affiliation) and provide the individual with the opportunity to restrict or prohibit some or all of the uses or disclosures permitted by paragraph (a)(1) of this section.
    (3) Emergency circumstances.(i) If the opportunity to object to uses or disclosures required by paragraph (a)(2) of this section cannot practicably be provided because of the individual's incapacity or an emergency treatment circumstance, a covered health care provider may use or disclose some or all of the protected health information permitted by paragraph (a)(1) of this section for the facility's directory, if such disclosure is:
    (A) Consistent with a prior expressed preference of the individual, if any, that is known to the covered health care provider; and
    (B) In the individual's best interest as determined by the covered health care provider, in the exercise of professional judgment.
    (ii) The covered health care provider must inform the individual and provide an opportunity to object to uses or disclosures for directory purposes as required by paragraph (a)(2) of this section when it becomes practicable to do so.
    (b) Standard: Uses and disclosures for involvement in the individual's care and notification purposes(1) Permitted uses and disclosures.(i) A covered entity may, in accordance with paragraphs (b)(2), (b)(3), or (b)(5) of this section, disclose to a family member, other relative, or a close personal friend of the individual, or any other person identified by the individual, the protected <PRTPAGE P="567"/>health information directly relevant to such person's involvement with the individual's health care or payment related to the individual's health care.
    (ii) A covered entity may use or disclose protected health information to notify, or assist in the notification of (including identifying or locating), a family member, a personal representative of the individual, or another person responsible for the care of the individual of the individual's location, general condition, or death. Any such use or disclosure of protected health information for such notification purposes must be in accordance with paragraphs (b)(2), (b)(3), (b)(4), or (b)(5) of this section, as applicable.
    (2) Uses and disclosures with the individual present.If the individual is present for, or otherwise available prior to, a use or disclosure permitted by paragraph (b)(1) of this section and has the capacity to make health care decisions, the covered entity may use or disclose the protected health information if it:
    (i) Obtains the individual's agreement;
    (ii) Provides the individual with the opportunity to object to the disclosure, and the individual does not express an objection; or
    (iii) Reasonably infers from the circumstances, based on the exercise of professional judgment, that the individual does not object to the disclosure.
    (3) Limited uses and disclosures when the individual is not present.If the individual is not present, or the opportunity to agree or object to the use or disclosure cannot practicably be provided because of the individual's incapacity or an emergency circumstance, the covered entity may, in the exercise of professional judgment, determine whether the disclosure is in the best interests of the individual and, if so, disclose only the protected health information that is directly relevant to the person's involvement with the individual's care or payment related to the individual's health care or needed for notification purposes. A covered entity may use professional judgment and its experience with common practice to make reasonable inferences of the individual's best interest in allowing a person to act on behalf of the individual to pick up filled prescriptions, medical supplies, X-rays, or other similar forms of protected health information.
    (4) Uses and disclosures for disaster relief purposes.A covered entity may use or disclose protected health information to a public or private entity authorized by law or by its charter to assist in disaster relief efforts, for the purpose of coordinating with such entities the uses or disclosures permitted by paragraph (b)(1)(ii) of this section. The requirements in paragraphs (b)(2), (b)(3), or (b)(5) of this section apply to such uses and disclosures to the extent that the covered entity, in the exercise of professional judgment, determines that the requirements do not interfere with the ability to respond to the emergency circumstances.
    (5) Uses and disclosures when the individual is deceased.If the individual is deceased, a covered entity may disclose to a family member, or other persons identified in paragraph (b)(1) of this section who were involved in the individual's care or payment for health care prior to the individual's death, protected health information of the individual that is relevant to such person's involvement, unless doing so is inconsistent with any prior expressed preference of the individual that is known to the covered entity.'''

sampleRegulation = '''Hello World. My name is Patrick. Except when an objection is expressed in accordance with paragraphs (a)(2) or (3) of this section, a covered health care provider may: (i) Use the following protected health information to maintain a directory of individuals in its facility:(A) The individual's name;(B) The individual's location in the covered health care provider's facility;(C) The individual's condition described in general terms that does not communicate specific medical information about the individual; and (D) The individual's religious affiliation; and (ii) Use or disclose for directory purposes such information: (A) To members of the clergy; or (B) Except for religious affiliation, to other persons who ask for the individual by name. This is true.'''
sample = "Hello my name is Patrick Cook."

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






def test01(spacyDoc):
    '''print Document type and attributes'''
    print("Type ", type(spacyDoc))
    print(iter(spacyDoc))


def test02(spacyDoc):
    '''print Token type and attributes'''
    token = spacyDoc[0]
    print(type(token))
    print(token.text, token.lemma_, token.pos_, token.tag_, token.dep_,
          token.shape_, token.is_alpha, token.is_stop)


def test03_DepencyGraph(spacyDoc):
    '''print Token type and attributes'''
    displacy.serve(spacyDoc, style="dep")


def test04(spacyDoc):
    '''
        print Token type and attributes
        http://localhost:5000
    '''
    displacy.serve(spacyDoc, style="ent")


def test05_SentenceSegmentation(spacyDoc):
    '''
      CFR45 164.510 
      Sentence Segmentation or 
      Boundary Detection
      -- note the default use-case is a "dependency parser"
    '''
    for number, sent in enumerate(spacyDoc.sents):
        print(number, sent)


def test06_Dependecy_Parser(spacyDoc):
    '''
      CFR45 164.510 
      Sentence Segmentation or 
      Boundary Detection
      -- note the default use-case is a "dependency parser"
    '''
    for number, sent in enumerate(spacyDoc.sents):
        print(number, sent)


def test07_Rule_Based_Matching(spacyDoc):
    '''
     Using the Matcher object in SpaCy
     When finding an anomaly or outlier, take the sentence
     and view the tokens.  A view of the tokens will help 
     identify how to improve the matcher - If time permits
     dive deeper to see how the matcher is implemented
     https://explosion.ai/demos/matcher

    '''

    shamroqMatcher = Matcher(nlp.vocab)

    shamroqMatcher.add("RIGHT01", None, right_pattern_01)
    shamroqMatcher.add("RIGHT02", None, right_pattern_02)
    shamroqMatcher.add("RIGHT03", None, right_pattern_03)

    shamroqMatcher.add("OBLIGATION01", None, obligation_pattern_01)
    shamroqMatcher.add("OBLIGATION02", None, obligation_pattern_02)
    shamroqMatcher.add("OBLIGATION03", None, obligation_pattern_03)
    shamroqMatcher.add("OBLIGATION04", None, obligation_pattern_04)
    shamroqMatcher.add("OBLIGATION05", None, obligation_pattern_05)
    shamroqMatcher.add("OBLIGATION06", None, obligation_pattern_06)

    shamroqMatcher.add("PRIVILEGE01", None, priv_pattern_01)
    shamroqMatcher.add("PRIVILEGE02", None, priv_pattern_02)
    shamroqMatcher.add("PRIVILEGE03", None, priv_pattern_03)
    shamroqMatcher.add("PRIVILEGE04", None, priv_pattern_04)
    shamroqMatcher.add("PRIVILEGE05", None, priv_pattern_05)
    shamroqMatcher.add("PRIVILEGE06", None, priv_pattern_06)
    shamroqMatcher.add("PRIVILEGE07", None, priv_pattern_07)
    i = 1
    for match_id, start, end in shamroqMatcher(spacyDoc):
        string_id = nlp.vocab.strings[match_id]
        span = spacyDoc[start:end]
        print(i, "  ", string_id, "  ", span.text)
        i = i + 1;
        # time.sleep(2)


def test08_Phrase_Matcher_01(spacyDoc):
    shamroqPhraseMatcher = PhraseMatcher(nlp.vocab)
    privilege_terms = ["may"]
    privilege_patterns = [nlp.make_doc(text) for text in privilege_terms]
    shamroqPhraseMatcher.add("PRIVILEGE", privilege_patterns)
    shamroqMatches = shamroqPhraseMatcher(spacyDoc);

    i = 1
    for match_id, start, end in shamroqMatches:
        span = spacyDoc[start:end]
        print(i, "  ", span.text)
        i = i + 1;
        time.sleep(1)


def test08_Phrase_Matcher_02(spacyDoc):
    shamroqPhraseMatcher = PhraseMatcher(nlp.vocab)
    privilege_terms = ["may"]
    privilege_patterns = [nlp.make_doc(text) for text in privilege_terms]
    shamroqPhraseMatcher.add("PRIVILEGE", privilege_patterns)
    shamroqMatches = shamroqPhraseMatcher(spacyDoc);

    i = 1
    for match_id, start, end in shamroqMatches:
        span = spacyDoc[start:end]
        print(i, "  ", span.text)
        i = i + 1;
        time.sleep(1)


def test09_RBM_with_CALLBACK(spacyDoc):
    testString = '''I may decide to work with you.  Or, I may elect not to work with you. A covered entity may orally inform the person on file.  For some unknown obligatory reason, I may not eat, workout, or study.  However, under the following circumstances, I may:  eat; workout; study; or sleep. In the event, you do not follow instructions, the constable may revoke your power.  On the other hand, the constable may terminate your license.  Finally, if all goes well, we may not authorize the constable to disable you in that manner.'''

    spacyDoc = nlp(testString)

    print("Rule Based Matching (RBM)")
    print("test09_RBM_with_CALLBACK")

    shamroqMatcher = Matcher(nlp.vocab)
    shamroqMatcher.add("RIGHT", None, right_pattern_01, right_pattern_02, right_pattern_03)
    shamroqMatcher.add("OBLIGATION", None, obligation_pattern_01, obligation_pattern_02, obligation_pattern_03,
                       obligation_pattern_04, obligation_pattern_05, obligation_pattern_06)
    shamroqMatcher.add("PRIVILEGE", None, priv_pattern_00, priv_pattern_01, priv_pattern_02, priv_pattern_03,
                       priv_pattern_04, priv_pattern_05, priv_pattern_06, priv_pattern_07)

    i = 1
    for match_id, start, end in shamroqMatcher(spacyDoc):
        string_id = nlp.vocab.strings[match_id]
        span = spacyDoc[start:end]
        print(i, "  ", string_id, "  ", span.text)
        i = i + 1;
        # time.sleep(2)


def test10_RBM_filter_OVERLAPPING_Matches(spacyDoc):
    testString = '''I may decide to work with you.  Or, I may elect not to work with you. A covered entity may orally inform the person on file.  For some unknown obligatory reason, I may not eat, workout, or study.  However, under the following circumstances, I may:  eat; workout; study; or sleep. In the event, you do not follow instructions, the constable may revoke your power.  On the other hand, the constable may terminate your license.  Finally, if all goes well, we may not authorize the constable to disable you in that manner.'''

    # spacyDoc = nlp(testString)

    print("Rule Based Matching (RBM)")
    print("test09_RBM_with_CALLBACK")

    shamroqMatcher = Matcher(nlp.vocab)
    shamroqMatcher.add("RIGHT", None, right_pattern_01, right_pattern_02, right_pattern_03)
    shamroqMatcher.add("OBLIGATION", None, obligation_pattern_01, obligation_pattern_02, obligation_pattern_03,
                       obligation_pattern_04, obligation_pattern_05, obligation_pattern_06)
    shamroqMatcher.add("PRIVILEGE", None, priv_pattern_00, priv_pattern_01, priv_pattern_02, priv_pattern_03,
                       priv_pattern_04, priv_pattern_05, priv_pattern_06, priv_pattern_07)

    matches = shamroqMatcher(spacyDoc)
    spans = [spacyDoc[start:end] for match_id, start, end in matches]
    noDuplicates = filter_spans(spans)
    i = 1;
    for span in noDuplicates:
        print(type(span))
        print("----------------------------")
        print("Modality & Action: --> ", span.text)
        print("----------------------------")
        print(i, span.sent)
        for spanToken in span.sent:
            if (spanToken.dep_ == 'nsubj'):
                print("Subject --> ", spanToken.text)
        print("\n\n")
        i = i + 1


def foundThem(matcher, doc, id, matches):
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        span = doc[start:end]
        print("String id = ", string_id)
        print("Span = ", span)
        print("id = ", id)
        # print('Matched!', matches)


def shamroq(text):
    doc = nlp(text)
    '''
        Please refactor 
        1. return the matcher object
        2. Add pattern groups rights, obligations, etc.
        3. Make call back methods to support each group
    '''
    test10_RBM_filter_OVERLAPPING_Matches(doc)


def filter_spans(spans):
    # Filter a sequence of spans so they don't contain overlaps
    # For spaCy 2.1.4+: this function is available as spacy.util.filter_spans()
    get_sort_key = lambda span: (span.end - span.start, -span.start)
    sorted_spans = sorted(spans, key=get_sort_key, reverse=True)
    result = []
    seen_tokens = set()
    for span in sorted_spans:
        # Check for end - 1 here because boundaries are inclusive
        if span.start not in seen_tokens and span.end - 1 not in seen_tokens:
            result.append(span)
        seen_tokens.update(range(span.start, span.end))
    result = sorted(result, key=lambda span: span.start)
    return result


def main():
    print("Spacy Example -->", len(sampleRegulation))
    print("/------------------------------------------/")
    print("... starting main()")
    print("/------------------------------------------/")
    print()
    print()

    #shamroq(regText164_510)

    print()
    print()
    print("/------------------------------------------/")
    print("... completing main()")
    print("/------------------------------------------/")


if __name__ == '__main__':
    main()

'''

    print("Span sentence = " , spans[0].sent, 
          "Span text = ", spans[0].text, 
          "<><><> Span label = ", spans[0],
          "\nMatches Object ---> ", matches[0])
    print("------------------------------\n")
    
    
    print("Span sentence = " , spans[1].sent, 
          "Span text = ", spans[1].text, 
          "<><><> Span label = ", spans[1].ent_id,
          "\nMatches Object ---> ", matches[1])
    print("------------------------------\n")
    
    print("Span sentence = " , spans[2].sent, 
          "Span text = ", spans[2].text, 
          "<><><> Span label = ", spans[2].ent_id,
          "\nMatches Object ---> ", matches[2])
    print("------------------------------\n")

    time.sleep(10000)
    
    print("\n\n----- RESULT 03 ------")
    k = 1
    
    
print("\n\n----- RESULT 01 Matches with Duplicates------")
    for match_id, start, end in matches:
        string_id = nlp.vocab.strings[match_id]
        span = spacyDoc[start:end]
        #print(i, "  ", span.sent)
        #print(i, "  ", string_id, "  ", span.text)
        i = i+1;

    print("\n\n----- RESULT 02:  TESTING ------")
    matches = shamroqMatcher(spacyDoc)
    spans = []
    for match_id, start, end in matches:
        spans.append(spacyDoc[start:end]) 
        string_id = nlp.vocab.strings[match_id]
        print(string_id)
        
        
        
        privilege_patterns = [nlp(spacyDocument) for spacyDocument in ('may', 'may elect not to', 'is not required to', 'requirement does not apply', 'is permitted to', 'at the election of', 'is not subject to')]
def printSentenceTokens(text):
    doc = nlp(text)
    verbs = set()
    for possible_subject in doc:
        if possible_subject.dep == "nsubj" and possible_subject.head.pos == "VERB":
            verbs.add(possible_subject.head)
            print(verbs)

def printSentenceTokens3(text):
    doc = nlp(text)
    verbs = set()
    for possible_subject in doc:
        if possible_subject.dep == "nsubj" and possible_subject.head.pos == "VERB":
            verbs.add(possible_subject.head)
            print(verbs)

def printSentence(text):
    doc = nlp(text)
    n = 1;
    for sentTokens in doc.sents:
        print(sentTokens)
        print(n)
        n = n+1;
        
        
            
def printNounChunks(text):
    doc = nlp(text)
    for nc in doc.noun_chunks:
        print(nc)
        time.sleep(5)
def insideTheSentence(text):
    print("insideSentence")
    doc = nlp(text)
    for nc in doc.nonu_chunks:
        print(nc)
        time.sleep(3)
'''
