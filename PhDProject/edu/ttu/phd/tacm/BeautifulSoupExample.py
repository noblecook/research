'''
Created on Dec 20, 2018

@author: patcoo
'''
import urllib.request
from bs4 import BeautifulSoup

get = urllib.request.urlopen("https://www.govinfo.gov/bulkdata/ECFR/title-27/ECFR-title27.xml")
html = get.read()

soup = BeautifulSoup(html)

print(soup)