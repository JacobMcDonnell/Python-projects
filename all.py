import datetime
import time
import os
import requests
import json
import praw

today = datetime.date.today()

ww1start = datetime.date(1914, 7, 28)#WW1 start date
ww1sday = today - ww1start
ww1end = datetime.date(1918, 11, 11)#WW1 end date
ww1eday = today - ww1end

ww2start = datetime.date(1939, 9, 1)#WW2 start date
ww2sday = today - ww2start
ww2end = datetime.date(1945, 9, 2)#WW2 end date
ww2eday = today - ww2end

Koreanwarstart = datetime.date(1950, 6, 25)#Korean War start date
Koreanwarsday = today - Koreanwarstart
Koreanwarend = datetime.date(1953, 7, 27)#Korean War end date
Koreanwareday = today - Koreanwarend

Vietnamwarstart = datetime.date(1955, 11, 1)#Vietnam War start date
Vietnamwarsday = today - Vietnamwarstart
Vietnamwarend = datetime.date(1975, 4, 30)#Vietnam War end date
Vietnamwareday = today - Vietnamwarend

USSRstart = datetime.date(1922, 12, 30)#U.S.S.R. start date
USSRsday = today - USSRstart
USSRend = datetime.date(1991, 12, 25)#U.S.S.R. end date
USSReday = today - USSRend

reddit = praw.Reddit(client_id='NuPI4zj-4u4DgQ', 
                     client_secret='LTYtxrEYiOry61BHrKW6pULDSNY', 
                     user_agent='stats')

me = reddit.redditor('McD223')
linkkarma = me.link_karma
commentkarma = me.comment_karma
totalkarma = linkkarma + commentkarma
while True:
    r = requests.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCXUuGvjW1KLq6oqfEX0BieQ&key=AIzaSyDdh94NZll6tzTUmO17d5nrh0zMuKcajaw')
    j = r.json()
    subs = j['items'][0]['statistics']['subscriberCount']
    views = j['items'][0]['statistics']['viewCount']

    
    time.sleep(5)
    os.system('clear')
    print ('    Important Date Counter')
    print ('------------------------------------')
    print ('WW1 Start:' ,ww1sday.days, 'days ago')
    print ('WW1 End:' ,ww1eday.days, 'days ago')
    print ('------------------------------------')
    print ('WW2 Start:' ,ww2sday.days, 'days ago')
    print ('WW2 End:' ,ww2eday.days, 'days ago')
    print ('------------------------------------')
    print ('Korean War Start:' ,Koreanwarsday.days, 'days ago')
    print ('Korean War End:' ,Koreanwareday.days, 'days ago')
    print ('------------------------------------')
    print ('Vietnam War Start:' ,Vietnamwarsday.days, 'days ago')
    print ('Vietnam War End:' ,Vietnamwareday.days, 'days ago')
    print ('------------------------------------')
    print ('U.S.S.R. Start:' ,USSRsday.days, 'days ago')
    print ('U.S.S.R. End:' ,USSReday.days, 'days ago')
    print ('-------------------------------------------------')
    print (' `-://////////////////////////////::`')
    print ('://////////////////////////////////:')
    print ('`////////////////////////////////////.')
    print ('.//////////////   ///////////////////-')
    print ('-//////////////       ///////////////-')
    print ('-//////////////          ////////////:' ,'McD223 Channel Stats:')
    print ('-//////////////            //////////:' ,'Total number of subscribers:' ,subs)
    print ('-//////////////          ////////////:' ,'Total number of views:' ,views)
    print ('-//////////////       ///////////////-')
    print ('.//////////////   ///////////////////-')
    print ('`////////////////////////////////////.')
    print ('://////////////////////////////////:')
    print (' `-://////////////////////////////::`')
    print ('  ``.....------------:-----.....``')
    print ('-------------------------------------------------')
    print ('McD223 Reddit stats:')
    print ('Link Karma:' ,linkkarma)
    print ('Comment Karma:' ,commentkarma)
    print ('Total Karma:' ,totalkarma)
