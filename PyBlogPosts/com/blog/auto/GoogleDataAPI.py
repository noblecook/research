'''
Created on May 6, 2015

@author: patri_000
'''
import urllib.request
import urllib.parse
import re
import time


technologyFeed1 = 'http://rss.nytimes.com/services/xml/rss/nyt/Technology.xml'
technologyFeed2 = 'http://www.huffingtonpost.com/feeds/index.xml'

def getURL():
    try:
        url = technologyFeed2;
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17'
        req = urllib.request.Request(url, headers=headers)
        resp = urllib.request.urlopen(req)
        respData = resp.read();
        
        
        titleTags = re.findall(r'<title>(.*?)</title>',str(respData))
        links = re.findall(r'<link.*?href="(.*?)"',str(respData))
                
        #for title in titleTags:
         #   print(title);
        
        for link in links:
            print('visiting ' + link);
            resp = urllib.request.urlopen(link)
            respData = resp.read();     
            print(respData)
            time.sleep(555)
            
            
    except Exception as e:
        print(str(e))
        
getURL()