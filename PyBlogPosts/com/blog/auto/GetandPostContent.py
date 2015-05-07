'''
Created on May 5, 2015

@author: patri_000
'''
import urllib.request
import urllib.parse
import re
import time
import keyword
import difflib



    
 

'''
    This code segment is used for posting data
    to a website that can be queried for results
'''
def postURL():
    try:
        url = 'http://pythonprogramming.net'
        values = {'s':'basic',
                  'submit':'search'}
        data = urllib.parse.urlencode(values)
        data = data.encode('utf_8')
        req = urllib.request.Request(url, data);
        resp = urllib.request.urlopen(req);
        respData = resp.read();        
        print(respData)
    except Exception as e:
        print(str(e))
        


'''
---- This code segmant getting a page
'''

def getWebPage():
    try:
        webpage = 'https://www.google.com'
        websiteSrcCode = urllib.request.urlopen(webpage)
        print(websiteSrcCode.read())
    except Exception as e:
        print(str(e))


'''
    Headers are added so that webpages will not
    consider the program to be bot. Results are 
    written to a file
'''
def getURL():
    try:
        url = 'https://www.google.com/search?q=test'
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read();
        saveFile = open('withHeaders.txt', 'w')
        saveFile.write(str(respData));
        saveFile.close();
        
        print()
    except Exception as e:
        print(str(e))
        


'''
    This code segment is used for posting data
    to a website that can be queried for results
'''
def parseWebSiteData():
    try:
        url = 'http://tailormade101.com'
        values = {'s':'basic',
                  'submit':'search'}
        data = urllib.parse.urlencode(values)
        data = data.encode('utf_8')
        req = urllib.request.Request(url, data);
        resp = urllib.request.urlopen(req);
        respData = resp.read();        
        
        
        #find all paragraph tags and return the content
        # the . looks for any character except for newline
        # the * looks for 0 or more repetitions
        # the ? looks for 0 or 1 repetitions
        paragraphTags = re.findall(r'<p>(.*?)</p>',str(respData))
        
        for paragraph in paragraphTags:
            print(paragraph)
        
        
    except Exception as e:
        print(str(e))
        

'''
knip
datasif
topsy - entire firehose 12k per year

search/realtime?q=obama&src=hash'
'''

def parseTwitter():
    try:
        twitterPrefix = 'https://twitter.com/search/realtime?q='
        keyword = 'Obama'
        searchSuffix = '&src=hash'
        
        url = twitterPrefix+keyword+searchSuffix
        
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read();
        
        twitterFeed = re.findall(r'<p class="TweetTextSize  js-tweet-text tweet-text" lang="en" data-aria-label-part="0">(.*?)</p>', str(respData))
        print (len(twitterFeed))
        #time.sleep(555)
        for item in twitterFeed:
            #print (item)
            print('-----------------------------------------------')
            print (re.sub(r'<.*?>','', item))
            time.sleep(5)
        
        
        #print(respData)      
        
        
    except Exception as e:
        print(str(e))    



'''
---- This code segmant getting a page
'''

def diffLibComparison():
    try:
        ar1 = [1,2,3,4,5]
        ar2 = [2,3,4,5,6]
        compare = difflib.SequenceMatcher(None, ar1, ar2)
        print(compare.ratio())
    except Exception as e:
        print(str(e))        
        
        
diffLibComparison()       
        
        
        
        
        
    


