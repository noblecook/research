'''
Created on May 29, 2015

@author: Patrick Cook
@summary: Reads rss feed, parses content, post blog, post comment, send to facebook, twitter, and email
12 months in a year (alphabetically)
Consider by state, then by city - alphabetically
how do you get the email addresses (of facebook accounts)
need a list of cities, per state alphabetically, searched,
in facebook; 
that state/city has x thousand people; then create the list
after the list is created, poll the list until exhausted
look for probabilities during that query
'''

from gdata import service
import gdata
import atom

tmtr = "http://tailormadetalkradio.blogspot.com"
ClientID = "838560167308-5839nr6lmdjr1c6gn25hrm8n2tmn3f7v.apps.googleusercontent.com"
ClientSecret = "JbaXSrmKludN5L8D77V-80Te"

blogger_service = service.GDataService('user@example.com', 'secretPassword')


