import os
import json
import requests
import praw #Makes sure we can use the module
import time #now we can use the sleep command to wait a second
#The next part will tell reddit that we are who we are, so that we can
#grab info from our accounts.
reddit = praw.Reddit(client_id='NuPI4zj-4u4DgQ', #Change this to the first string
                     client_secret='LTYtxrEYiOry61BHrKW6pULDSNY', #Change this to the secret string
                     user_agent='stats') #This can be anything, just give a title!

me = reddit.redditor('McD223') #Defines the variable me as our account
linkkarma = me.link_karma #Defines the variable linkkarma as our link karma
commentkarma = me.comment_karma #Defines the variable commentkarma as our comment karma
totalkarma = linkkarma + commentkarma #This will make a variable called totalkarma that will add both of the karma variables together.

#now we can use those three variables in any program! for example lets make a program that tells us our karma every second!

while True:
    time.sleep(5)
    os.system('clear')
    print ('McD223 Reddit stats:')
    print ('Link Karma:' ,linkkarma)
    print ('Comment Karma:' ,commentkarma)
    print ('Total Karma:' ,totalkarma)
