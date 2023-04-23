import time
import xml.etree.ElementTree as eTree
HOME_BASE = "C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/far/"
CFR_VOLUME_01 = "CFR-2021-title48-vol1.xml"
eCFR_DATASET = HOME_BASE + CFR_VOLUME_01


def print_dict_of_provisions(my_dict):
    item = 0
    for key, value in my_dict.items():
        print(f'{key} {value}')
        print(" ITEM ==> ", item)
        item = item + 1


def print_list_of_provisions(cfr_metadata_list):
    for subpart in cfr_metadata_list:
        for key, value in subpart.items():
            print(f'{key} {value}')
        time.sleep(3)


def getCFRMetaData(reg_xml_file_location):
    # use XSLT to get only two important elements
    # store the results and return
    tree = eTree.parse(reg_xml_file_location)
    root = tree.getroot()
    cfrMetaDataList = []

    for subpart_element in root.findall('.//SUBPART/SECTION'):
        subpart_meta_data = {
            'SECTNO': '',
            'SUBJECT': '',
            'TEXT': ''
        }

        sectno_elements = subpart_element.findall('.//SECTNO')
        if len(sectno_elements) > 0:
            subpart_meta_data['SECTNO'] = ", ".join([element.text for element in sectno_elements])

        subject_elements = subpart_element.findall('.//SUBJECT')
        if len(subject_elements) > 0:
            subpart_meta_data['SUBJECT'] = ", ".join([element.text for element in subject_elements])

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


def main():
    regList_NEW = [eCFR_DATASET]
    for regulation in regList_NEW:
        metadata = getCFRMetaData(regulation)
        print_list_of_provisions(metadata)


if __name__ == '__main__':
    main()

