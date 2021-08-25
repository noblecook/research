import analyze
import classify
import model
import scan
import preprocessor
import clean
import time

FILE_PREFIX_COPPA = 'C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/coppa/'
FILE_PREFIX_HIPAA = 'C:/Users/patri/PycharmProjects/research/PyDevShamroq/data/coppa/'

xml_45_164_306 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-306.xml'
xml_45_164_310 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-310.xml'
xml_45_164_312 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-312.xml'
xml_45_164_510 = FILE_PREFIX_HIPAA + 'CFR-2019-title45-vol2-sec164-510.xml'
xml_16_132_011 = FILE_PREFIX_COPPA + 'CFR-2020-title16-vol1-sec312-11.xml'

# regList = [xml_45_164_306, xml_45_164_310, xml_45_164_312, xml_45_164_510]

regList = [xml_16_132_011]


def getTimeNow():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Current Time =", current_time)
    return t


def shamroq_old(listOfRegulations):
    requirements = []
    getTimeNow()
    for regulation in listOfRegulations:
        analysisResult = analyze.init(regulation)
        classificationResults = classify.init(analysisResult)
        model.init(analysisResult, classificationResults)
    getTimeNow()
    # processingTime = int (stop - start);
    # print("Time to complete = " +  processingTime)
    return requirements


def scanRegulations(reg):
    return scan.init(reg)


def preProcessRegulations(scannedFiles, regulation):
    return preprocessor.init(scannedFiles, regulation)


def cleanRegulations(results):
    return clean.sanitize(results)


def shamroq(listOfRegulations):
    requirements = []
    getTimeNow()
    for regulation in listOfRegulations:
        # scan.init() returns a nested xml structure and stores in scannedFiles
        scannedResults = scanRegulations(regulation)

        # preprocessor.init() returns a dictionary of the CFR
        preProcessedResults = preProcessRegulations(scannedResults, regulation)

        # clean.sanitize() returns a structured dictionary
        cleanedResults = cleanRegulations(preProcessedResults)

        classificationResults = classify.init(cleanedResults)

        model.init(cleanedResults, classificationResults)
    getTimeNow()
    # processingTime = int (stop - start);
    # print("Time to complete = " +  processingTime)
    return requirements


def main():
    print("Number of regulations -->", len(regList))
    print("/------------------------------------------/")
    print("... starting main()")
    print("/------------------------------------------/")
    print("\n")
    shamroq(regList)
    print("\n")
    print("/------------------------------------------/")
    print("... completing main()")
    print("/------------------------------------------/")


if __name__ == '__main__':
    main()
