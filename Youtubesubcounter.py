import os
import json
import time
import requests


while True:
     r = requests.get('https://www.googleapis.com/youtube/v3/channels?part=statistics&id=UCXUuGvjW1KLq6oqfEX0BieQ&key=AIzaSyDdh94NZll6tzTUmO17d5nrh0zMuKcajaw')
     j = r.json()
     subs = j['items'][0]['statistics']['subscriberCount']
     views = j['items'][0]['statistics']['viewCount']


     time.sleep(5)
     os.system('clear')
     print(' `-://////////////////////////////::`')
     print('://////////////////////////////////:')
     print('`////////////////////////////////////.')
     print('.//////////////   ///////////////////-')
     print('-//////////////       ///////////////-')
     print('-//////////////          ////////////:' ,'McD223 Channel Stats:')
     print('-//////////////            //////////:' ,'Total number of subscribers:' ,subs)
     print('-//////////////          ////////////:' ,'Total number of views:' ,views)
     print('-//////////////       ///////////////-')
     print('.//////////////   ///////////////////-')
     print('`////////////////////////////////////.')
     print('://////////////////////////////////:')
     print(' `-://////////////////////////////::`')
     print('  ``.....------------:-----.....``')
     #print ('McD223 Channel Stats:')
     #print ('Total number of subscribers:' ,subs)
     #print ('Total number of views:' ,views)
