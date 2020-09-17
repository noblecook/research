import analyze
import classify
import model
import time


FILEPREFIX = 'C:/Users/patri/git/research/PyDevShamroq/data/'
xml_45_164_306 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-306.xml'
xml_45_164_310 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-310.xml'
xml_45_164_312 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-312.xml'
xml_45_164_510 = FILEPREFIX+'CFR-2019-title45-vol2-sec164-510.xml'
regList = [xml_45_164_306, xml_45_164_310, xml_45_164_312, xml_45_164_510]
#regListSingle = [xml_45_164_510]


def getTimeNow():
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("Current Time =", current_time)
    
def shamroq(listOfRegulations):
    requirements = []
    getTimeNow()
    for regulation in listOfRegulations:
        analysisResult = analyze.init(regulation)
        classificatonResults = classify.init(analysisResult);
        model.init(classificatonResults);
    
    getTimeNow()
    return requirements
   

def main():
    print("Number of regulations -->", len(regList))
    print("/------------------------------------------/")
    print("... starting main()")
    print("/------------------------------------------/")
    shamroq(regList) 
    print("/------------------------------------------/")
    print("... completing main()")
    print("/------------------------------------------/")

if __name__ == '__main__':
    main()
