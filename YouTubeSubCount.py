#!/usr/bin/python
import requests
import json
import time
import os

while True:

 r = requests.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCXUuGvjW1KLq6oqfEX0BieQ&key=AIzaSyC6xLODu34WFpDHdqaQf8Lfmokh5wYX_is')
 j = r.json()

 subs = j['items'][0]['statistics']['subscriberCount']
 views = j['items'][0]['statistics']['viewCount']


 time.sleep(5)
 os.system('clear')
 print "YOUR CHANNEL Channel Stats:"
 print "Total number of subscribers: %s" % (subs)
 print "Total number of views: %s" % (views)
